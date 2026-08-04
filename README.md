# Générateur de cours automatisé

Système qui génère automatiquement des cours pédagogiques complets sur n'importe quel sujet, en combinant recherche documentaire (Wikipedia) et génération de contenu par IA (Groq / Llama 3.3 70B).

## Fonctionnalités

- **Génération de cours simple ou de programme complet multi-modules** sur n'importe quel sujet
- **Recherche contextuelle automatique** sur Wikipedia (FR + EN) avant génération, via l'API de recherche officielle (`opensearch`) pour trouver l'article le plus pertinent, même quand le titre exact n'est pas connu — avec un repli automatique sur une version nettoyée du sujet (tournures comme "Introduction aux fondamentaux de...") si la première recherche ne trouve rien
- **Filtre de pertinence par Machine Learning** : un modèle de classification (régression logistique, scikit-learn) entraîné pour détecter automatiquement si un extrait Wikipedia trouvé est réellement pertinent pour le sujet demandé, ou s'il s'agit d'un cas d'homonymie hors-sujet (ex : chercher "Pluton" le personnage Disney et tomber sur la planète naine)
- **Erreurs réseau explicites, jamais silencieuses** : chaque échec Wikipedia (statut HTTP non-200, timeout, erreur réseau, JSON invalide) est identifié et journalisé précisément, plutôt que traité comme un simple "aucun résultat"
- **Suggestion de sujets connexes** après génération d'un cours
- Sauvegarde automatique en fichiers Markdown, un dossier par programme multi-modules

## Architecture

```
generateur-cours/
├── main.py                          # Interface en ligne de commande
├── chercheur.py                     # Recherche Wikipedia + filtre de pertinence ML
├── generateur.py                    # Génération de contenu via Groq
├── entrainement/
│   ├── generer_dataset.py           # Génération du dataset d'entraînement (Groq + Wikipedia)
│   ├── dataset_pertinence.csv       # Dataset annoté (sujet, extrait, label UTILE/INUTILE)
│   ├── entrainer_classifieur.py     # Entraînement du modèle de production (régression logistique)
│   ├── entrainer_reseau.py          # Expérimentation réseau de neurones (PyTorch, non utilisé en prod)
│   └── modele_pertinence.pkl        # Modèle entraîné, chargé par chercheur.py
├── tests/
│   └── test_recherche.py            # Script manuel pour tester la recherche Wikipedia seule, sans appeler Groq
├── cours_generes/                   # Sortie des cours générés
├── .env.example                     # Modèle du fichier .env attendu
└── requirements.txt
```

## Le modèle de pertinence — détails techniques

Le cœur du filtre ML repose sur un pipeline scikit-learn :

```python
Pipeline([
    ("tfidf", TfidfVectorizer(min_df=2)),
    ("clf", LogisticRegression(class_weight="balanced", max_iter=1000)),
])
```

**Feature d'entrée** : `sujet + " " + extrait` — le modèle voit à la fois le sujet demandé et l'extrait trouvé, ce qui lui permet de détecter les décalages (extrait bien écrit mais hors-sujet), et pas seulement la qualité intrinsèque du texte.

**Performance** : F1 = 0.83 ± 0.06 sur la classe UTILE (validation croisée à 5 folds), sur un dataset de 161 exemples (29 UTILE / 132 INUTILE, `class_weight` équilibré pour compenser le déséquilibre).

**Limite connue** : le dataset reste petit — une des prochaines étapes est de l'enrichir (`entrainement/generer_dataset.py`, mode `enrichir`) pour améliorer la robustesse du modèle, en particulier sur la catégorie la plus rare (extrait non-vide mais hors-sujet).

## Installation

```bash
git clone https://github.com/amadou11doumbouya10-lgtm/generateur-cours.git
cd generateur-cours
pip install -r requirements.txt
```

Copie `.env.example` vers `.env` et renseigne ta clé Groq ([console.groq.com](https://console.groq.com)) :
```
GROQ_API_KEY=ta_clé_ici
```

## Utilisation

```bash
python main.py
```

Suis les instructions interactives pour générer un cours simple ou un programme complet multi-modules.

## Réentraîner le modèle de pertinence

```bash
python entrainement/entrainer_classifieur.py
```

Régénère `modele_pertinence.pkl` à partir de `dataset_pertinence.csv`, avec un rapport precision/recall/F1 et une évaluation par validation croisée affichés dans le terminal.

Pour étendre le dataset avant réentraînement :
```bash
python entrainement/generer_dataset.py
```
Contrôlé par deux variables d'environnement : `NB_SUJETS` (60 par défaut) et `MODE` (`complet`, la valeur par défaut, écrase le dataset existant ; `enrichir` ajoute des lignes ciblées sur des sujets ambigus/homonymes).

## Stack technique

- **Python** 3.9+
- **Groq API** (Llama 3.3 70B) — génération de contenu
- **Wikipedia API** (REST + opensearch) — recherche documentaire
- **scikit-learn** — modèle de classification (TF-IDF + régression logistique)
- **PyTorch** — expérimentations complémentaires (réseau de neurones)

## Auteur

Amadou Doumbouya — [Vision Amah](https://vision-amah.vercel.app)
