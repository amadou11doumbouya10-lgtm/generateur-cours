# Prochaines étapes

Dernière mise à jour : 2026-08-04. État du projet à ce moment-là : l'app (`main.py`) et le pipeline ML (dataset → `entrainer_classifieur.py` → `modele_pertinence.pkl` → filtre dans `chercheur.py`) fonctionnent et sont documentés dans `../CLAUDE.md`. Rien de cassé, rien de bloquant. Les points ci-dessous sont des pistes identifiées mais pas encore faites.

## Étape 3 du plan ML — génération de texte façon nanoGPT

Pas commencée. C'est l'étape la plus ambitieuse du plan initial en 3 temps (régression → réseau de neurones → génération de texte) : entraîner un petit modèle génératif type nanoGPT (projet éducatif d'Andrej Karpathy) sur un corpus réduit, par exemple les cours déjà générés dans `cours_generes/`. Objectif pédagogique pur — il ne rivalisera jamais avec Llama/Groq, mais permet de comprendre de l'intérieur le fonctionnement d'un modèle génératif entraîné à la main. Contrairement à l'Étape 1, elle n'a pas vocation à s'intégrer dans le pipeline existant.

## Améliorations identifiées sur le classifieur de pertinence

- **[RÉSOLU 2026-08-04] Feature sujet+extrait manquante côté production.** `entrainer_classifieur.py` charge maintenant sujet+extrait concaténés (comme `entrainer_reseau.py` le faisait déjà). `chercheur.py` (`extrait_est_pertinent`, lignes 59/177/183) passe désormais le sujet en cohérence avec l'entraînement. `modele_pertinence.pkl` régénéré : F1 = 0.83 ± 0.06 (validation croisée, classe UTILE) sur les 161 exemples du dataset.
- **Dataset encore petit.** 161 exemples dont seulement 29 UTILE. `entrainement/generer_dataset.py` (mode `enrichir`) peut être relancé pour ajouter des exemples, en particulier des cas "extrait non-vide mais inutile" (la catégorie la plus rare).

## Non prévu mais mentionné en passant

Rien d'autre n'est resté ouvert de la conversation — pas de bug connu, pas de tâche à moitié faite en dehors des deux points ci-dessus.
