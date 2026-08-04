import os
import re
import json
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

MODEL = "llama-3.3-70b-versatile"


def slugifier(texte):
    """Transforme un texte libre en nom de fichier sûr (sans ponctuation ni caractères interdits)."""
    texte = texte.strip().lower()
    texte = re.sub(r"[^\w\s-]", "", texte, flags=re.UNICODE)
    texte = re.sub(r"\s+", "_", texte)
    return texte or "sans_titre"


def generer_cours(infos):
    """Utilise Groq pour générer un cours complet à partir des infos collectées."""
    sujet = infos["sujet"]
    contexte = f"""
Informations Wikipedia (français) :
{infos['wikipedia_fr']}

Informations Wikipedia (anglais) :
{infos['wikipedia_en']}
"""

    prompt = f"""Tu es un expert en automatisation Python et en pédagogie.

À partir des informations suivantes sur le sujet "{sujet}", crée un cours complet en français.

{contexte}

Le cours doit contenir :
1. Introduction et définition claire
2. Pourquoi utiliser cette technologie (cas d'usage concrets)
3. Installation et prérequis
4. Concepts fondamentaux (avec explications simples)
5. Exemples de code commentés (du plus simple au plus avancé)
6. Exercices pratiques avec énoncés
7. Erreurs courantes et comment les éviter
8. Ressources pour aller plus loin

Utilise le format Markdown. Sois concret, pédagogique et donne beaucoup d'exemples de code Python.
"""

    print("\n Génération du cours avec Groq...")
    reponse = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=4000,
    )

    return reponse.choices[0].message.content


def suggerer_cours_lies(sujet, nb_suggestions=5):
    """Utilise Groq pour suggérer des sujets de cours connexes à explorer ensuite."""
    prompt = f"""Un apprenant vient de terminer un cours sur "{sujet}".

Suggère {nb_suggestions} sujets connexes qu'il pourrait explorer ensuite pour progresser, du plus complémentaire au plus avancé. Chaque sujet doit être court (quelques mots) et assez précis pour devenir le titre d'un nouveau cours.

Réponds UNIQUEMENT avec un objet JSON valide de cette forme exacte, sans texte ni commentaire autour :
{{"suggestions": ["sujet 1", "sujet 2"]}}
"""

    reponse = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=400,
        response_format={"type": "json_object"},
    )

    data = json.loads(reponse.choices[0].message.content)
    return data.get("suggestions", [])


def generer_plan_programme(sujet, nb_modules=6):
    """Utilise Groq pour concevoir un programme de formation complet, découpé en modules progressifs."""
    prompt = f"""Tu es un architecte pédagogique expert en Python et en automatisation.

Conçois un programme de formation complet et progressif sur le sujet "{sujet}", découpé en {nb_modules} modules, du plus simple au plus avancé.

Réponds UNIQUEMENT avec un objet JSON valide de cette forme exacte, sans texte ni commentaire autour :
{{
  "titre_programme": "Titre général du programme",
  "modules": [
    {{"titre": "Titre du module 1", "description": "Ce que couvre ce module, en une phrase"}}
  ]
}}
"""

    print("\n Conception du programme avec Groq...")
    reponse = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.6,
        max_tokens=1500,
        response_format={"type": "json_object"},
    )

    return json.loads(reponse.choices[0].message.content)


def sauvegarder_cours(sujet, contenu):
    """Sauvegarde le cours dans un fichier Markdown."""
    nom_fichier = slugifier(sujet) + ".md"
    chemin = f"cours_generes/{nom_fichier}"

    with open(chemin, "w", encoding="utf-8") as f:
        f.write(f"# Cours : {sujet}\n\n")
        f.write(contenu)

    print(f"\n Cours sauvegardé dans : {chemin}")
    return chemin


def initialiser_programme(sujet, plan):
    """Crée le dossier du programme et y sauvegarde son sommaire."""
    dossier = f"cours_generes/programme_{slugifier(sujet)}"
    os.makedirs(dossier, exist_ok=True)

    with open(f"{dossier}/00_sommaire.md", "w", encoding="utf-8") as f:
        f.write(f"# Programme complet : {plan.get('titre_programme', sujet)}\n\n")
        f.write(f"Programme généré automatiquement sur le sujet **{sujet}**.\n\n")
        f.write("## Sommaire des modules\n\n")
        for i, module in enumerate(plan.get("modules", []), start=1):
            f.write(f"{i}. **{module.get('titre', '')}** — {module.get('description', '')}\n")

    return dossier


def sauvegarder_module(dossier, index, module, contenu):
    """Sauvegarde le cours d'un module du programme dans son propre fichier."""
    nom_fichier = f"{index:02d}_{slugifier(module.get('titre') or f'module_{index}')}.md"
    chemin = f"{dossier}/{nom_fichier}"

    with open(chemin, "w", encoding="utf-8") as f:
        f.write(f"# Module {index} : {module.get('titre', '')}\n\n")
        f.write(contenu)

    return chemin
