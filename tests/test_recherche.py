"""Petit script pour tester uniquement la recherche Wikipedia, sans passer par Groq."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

if sys.stdout.encoding.lower() != "utf-8":
    sys.stdout.reconfigure(encoding="utf-8")

from chercheur import collecter_infos

sujets_test = [
    "Introduction aux fondamentaux de l'IA",
    "Principes de base du Machine Learning",
    "Apprentissage automatique avec Python",
]

for sujet in sujets_test:
    print("=" * 60)
    infos = collecter_infos(sujet)
    print(f"Aperçu FR: {infos['wikipedia_fr'][:150]}")
    print()
