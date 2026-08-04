import os
import sys
import csv
import json

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from chercheur import chercher_wikipedia, chercher_wikipedia_en
from generateur import client, MODEL

if sys.stdout.encoding.lower() != "utf-8":
    sys.stdout.reconfigure(encoding="utf-8")

NB_SUJETS = int(os.environ.get("NB_SUJETS", 60))
MODE = os.environ.get("MODE", "complet")  # "complet" ou "enrichir"
CHEMIN_CSV = os.path.join(os.path.dirname(os.path.abspath(__file__)), "dataset_pertinence.csv")


def generer_liste_sujets(n):
    """Utilise Groq pour générer une liste variée de sujets (précis, ambigus, ou peu susceptibles d'exister sur Wikipedia)."""
    prompt = f"""Génère une liste de {n} sujets variés pour tester un moteur de recherche Wikipedia, répartis en 4 catégories à peu près égales :
1. Des sujets techniques précis et non ambigus (ex: "Photosynthèse", "Algorithme de tri rapide")
2. Des mots courts et polysémiques qui correspondent souvent à des pages d'homonymie Wikipedia (ex: "Mercure", "Java")
3. Des expressions longues ou formulées comme une question, peu susceptibles de matcher un titre Wikipedia exact (ex: "comment fonctionne le machine learning")
4. Des sujets aléatoires de culture générale (sciences, histoire, technologie, nature)

Réponds UNIQUEMENT avec un objet JSON valide de cette forme exacte, sans texte autour :
{{"sujets": ["sujet 1", "sujet 2"]}}
"""
    reponse = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.9,
        max_tokens=2000,
        response_format={"type": "json_object"},
    )
    data = json.loads(reponse.choices[0].message.content)
    return data.get("sujets", [])


def generer_liste_sujets_ambigus(n):
    """Utilise Groq pour générer des mots RÉELS et bien connus qui correspondent à des pages d'homonymie ou des articles très courts sur Wikipedia.

    Cible spécifiquement la catégorie sous-représentée dans le dataset : extrait non-vide mais peu pertinent.
    """
    prompt = f"""Liste {n} mots ou noms courts, réels et bien connus, qui correspondent à des pages d'homonymie ou à des articles très courts sur Wikipedia (en français et/ou en anglais).

Cible ce type de mots :
- Noms partagés par une planète/un dieu romain/un élément chimique (ex: Mercure, Neptune, Pluton)
- Noms d'entreprises ou de technologies qui sont aussi des mots communs (ex: Java, Python, Amazon, Apple, Orange, Windows, Shell, Swift)
- Prénoms très communs qui ont chacun de nombreuses personnalités homonymes (ex: Jean, Marie, Alexandre)
- Mots courts avec plusieurs sens bien distincts (ex: Avocat, Mercure, Mars)

Utilise UNIQUEMENT de vrais mots existants, pas des expressions inventées.

Réponds UNIQUEMENT avec un objet JSON valide de cette forme exacte, sans texte autour :
{{"sujets": ["mot 1", "mot 2"]}}
"""
    reponse = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.8,
        max_tokens=1500,
        response_format={"type": "json_object"},
    )
    data = json.loads(reponse.choices[0].message.content)
    return data.get("sujets", [])


def juger_extrait(sujet, extrait):
    """Utilise Groq pour juger si un extrait Wikipedia est exploitable pour rédiger un cours."""
    prompt = f"""Voici un extrait récupéré depuis Wikipedia pour le sujet "{sujet}" :

"{extrait}"

Cet extrait est-il un contenu exploitable pour rédiger un cours pédagogique sur "{sujet}" ?
Réponds INUTILE si c'est une page d'homonymie, un texte trop court/vague, ou hors-sujet.
Réponds UTILE si c'est un résumé informatif et pertinent.

Réponds uniquement par un seul mot : UTILE ou INUTILE."""

    reponse = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}],
        temperature=0,
        max_tokens=10,
    )
    texte = reponse.choices[0].message.content.strip().upper()
    # "UTILE" est une sous-chaîne de "INUTILE" : il faut tester INUTILE en premier.
    return "INUTILE" if "INUTILE" in texte else "UTILE"


def construire_dataset(sujets, writer, f):
    """Interroge Wikipedia puis fait juger chaque extrait par Groq, en écrivant chaque ligne immédiatement.

    Écrire (et flush) au fur et à mesure évite de tout perdre si le script est interrompu en cours de route.
    """
    total = len(sujets) * 2
    index = 0
    nb_utile = 0
    nb_total = 0

    for sujet in sujets:
        for langue, chercher in (("fr", chercher_wikipedia), ("en", chercher_wikipedia_en)):
            index += 1
            print(f"[{index}/{total}] {sujet} ({langue})...", end=" ", flush=True)

            extrait = chercher(sujet)

            if not extrait:
                print("vide -> INUTILE")
                writer.writerow([sujet, langue, "", "INUTILE"])
                f.flush()
                nb_total += 1
                continue

            try:
                label = juger_extrait(sujet, extrait)
            except Exception as e:
                print(f"erreur Groq, ignoré ({e})")
                continue

            print(label)
            writer.writerow([sujet, langue, extrait, label])
            f.flush()
            nb_total += 1
            if label == "UTILE":
                nb_utile += 1

    return nb_total, nb_utile


def main():
    if MODE == "enrichir":
        print(f"[Enrichissement] Génération de {NB_SUJETS} sujets ambigus ciblés avec Groq...")
        sujets = generer_liste_sujets_ambigus(NB_SUJETS)
        mode_fichier = "a"
    else:
        print(f"Génération de {NB_SUJETS} sujets variés avec Groq...")
        sujets = generer_liste_sujets(NB_SUJETS)
        mode_fichier = "w"

    print(f"{len(sujets)} sujets générés.\n")

    ecrire_entete = not (mode_fichier == "a" and os.path.exists(CHEMIN_CSV))

    with open(CHEMIN_CSV, mode_fichier, newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if ecrire_entete:
            writer.writerow(["sujet", "langue", "extrait", "label"])
            f.flush()

        nb_total, nb_utile = construire_dataset(sujets, writer, f)

    verbe = "ajoutés" if mode_fichier == "a" else "sauvegardés"
    print(f"\n{nb_total} exemples {verbe} dans {CHEMIN_CSV}")
    print(f"Répartition de ce lot : {nb_utile} UTILE / {nb_total - nb_utile} INUTILE")


if __name__ == "__main__":
    main()
