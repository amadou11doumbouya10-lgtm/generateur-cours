import sys
from chercheur import collecter_infos
from generateur import (
    generer_cours,
    sauvegarder_cours,
    suggerer_cours_lies,
    generer_plan_programme,
    initialiser_programme,
    sauvegarder_module,
)

if sys.stdout.encoding.lower() != "utf-8":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stdin.reconfigure(encoding="utf-8")


def cours_simple(sujet):
    """Génère un cours unique sur un sujet, puis propose des suites possibles."""
    infos = collecter_infos(sujet)
    cours = generer_cours(infos)
    chemin = sauvegarder_cours(sujet, cours)

    print("\n" + "=" * 50)
    print(" Cours généré avec succès !")
    print(f" Fichier : {chemin}")
    print("=" * 50)

    print("\n APERÇU (100 premiers mots) :")
    print("-" * 40)
    mots = cours.split()[:100]
    print(" ".join(mots) + "...")

    proposer_suite(sujet)


def proposer_suite(sujet):
    """Propose des sujets connexes ou la transformation du sujet en programme complet."""
    print("\n Recherche de sujets connexes...")
    try:
        suggestions = suggerer_cours_lies(sujet)
    except Exception:
        suggestions = []

    if suggestions:
        print("\n Sujets connexes suggérés :")
        for i, s in enumerate(suggestions, start=1):
            print(f"   {i}. {s}")

    print("\n Que veux-tu faire ?")
    if suggestions:
        print("   [numéro]  Générer ce cours connexe")
    print("   P         Transformer ce sujet en programme complet multi-modules")
    print("   Entrée    Revenir au menu principal (nouveau sujet)")
    choix = input("> ").strip()

    if choix.upper() == "P":
        programme_complet(sujet)
    elif choix.isdigit() and suggestions and 1 <= int(choix) <= len(suggestions):
        cours_simple(suggestions[int(choix) - 1])


def programme_complet(sujet):
    """Génère un programme complet multi-modules sur un sujet, module par module."""
    print(f"\n Conception d'un programme complet sur : {sujet}")
    try:
        plan = generer_plan_programme(sujet)
    except Exception as e:
        print(f" Impossible de générer le plan du programme : {e}")
        return

    modules = plan.get("modules", [])
    if not modules:
        print(" Le plan généré ne contient aucun module. Abandon.")
        return

    print(f"\n Programme : {plan.get('titre_programme', sujet)}")
    for i, m in enumerate(modules, start=1):
        print(f"   {i}. {m.get('titre', '')}")

    dossier = initialiser_programme(sujet, plan)

    chemins = []
    for i, module in enumerate(modules, start=1):
        titre_module = module.get("titre") or f"{sujet} - partie {i}"
        print(f"\n--- Module {i}/{len(modules)} : {titre_module} ---")
        try:
            infos = collecter_infos(titre_module)
            cours = generer_cours(infos)
            chemin = sauvegarder_module(dossier, i, module, cours)
            chemins.append(chemin)
        except Exception as e:
            print(f" Erreur sur ce module, passage au suivant : {e}")

    print("\n" + "=" * 50)
    print(" Programme complet généré avec succès !")
    print(f" Dossier : {dossier}")
    print(f" {len(chemins)}/{len(modules)} modules générés.")
    print("=" * 50)


def main():
    print("=" * 50)
    print("   GÉNÉRATEUR DE COURS AUTOMATISATION")
    print("=" * 50)

    while True:
        sujet = input("\nSur quel sujet veux-tu un cours ? (Q pour quitter)\n> ").strip()

        if not sujet or sujet.upper() == "Q":
            print("\n À bientôt !")
            break

        print("\n Que veux-tu générer ?")
        print("   1. Un cours simple sur ce sujet")
        print("   2. Un programme complet multi-modules sur ce sujet")
        mode = input("> ").strip()

        if mode == "2":
            programme_complet(sujet)
        else:
            cours_simple(sujet)


if __name__ == "__main__":
    main()
