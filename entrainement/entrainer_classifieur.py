import os
import sys

import joblib
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix, f1_score, make_scorer
from sklearn.model_selection import StratifiedKFold, cross_val_score, train_test_split
from sklearn.pipeline import Pipeline

if sys.stdout.encoding.lower() != "utf-8":
    sys.stdout.reconfigure(encoding="utf-8")

DOSSIER = os.path.dirname(os.path.abspath(__file__))
CHEMIN_CSV = os.path.join(DOSSIER, "dataset_pertinence.csv")
CHEMIN_MODELE = os.path.join(DOSSIER, "modele_pertinence.pkl")


def charger_donnees():
    df = pd.read_csv(CHEMIN_CSV)
    df["extrait"] = df["extrait"].fillna("")
    df["sujet"] = df["sujet"].fillna("")
    df["texte"] = df["sujet"] + " " + df["extrait"]
    return df["texte"], df["label"]


def nouveau_pipeline():
    return Pipeline([
        ("tfidf", TfidfVectorizer(min_df=2)),
        ("clf", LogisticRegression(class_weight="balanced", max_iter=1000, random_state=42)),
    ])


def evaluer_par_validation_croisee(X, y, k=5):
    """F1 sur la classe UTILE par validation croisée : plus fiable qu'un seul split vu le peu d'exemples UTILE."""
    skf = StratifiedKFold(n_splits=k, shuffle=True, random_state=42)
    scorer_utile = make_scorer(f1_score, pos_label="UTILE", zero_division=0)
    scores = cross_val_score(nouveau_pipeline(), X, y, cv=skf, scoring=scorer_utile)
    print(f"F1 (classe UTILE) en validation croisée ({k} folds) : {scores.mean():.2f} ± {scores.std():.2f}")
    print(f"  Détail par fold : {[round(s, 2) for s in scores]}")


def main():
    X, y = charger_donnees()
    print(f"Dataset : {len(X)} exemples ({(y == 'UTILE').sum()} UTILE / {(y == 'INUTILE').sum()} INUTILE)\n")

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, stratify=y, random_state=42
    )
    print(f"Train : {len(X_train)} exemples ({(y_train == 'UTILE').sum()} UTILE)")
    print(f"Test  : {len(X_test)} exemples ({(y_test == 'UTILE').sum()} UTILE)\n")

    pipeline_eval = nouveau_pipeline()
    pipeline_eval.fit(X_train, y_train)
    y_pred = pipeline_eval.predict(X_test)

    print("=== Résultat sur le test set (20%, non vu à l'entraînement) ===")
    print(classification_report(y_test, y_pred, zero_division=0))

    labels = ["UTILE", "INUTILE"]
    matrice = confusion_matrix(y_test, y_pred, labels=labels)
    print("Matrice de confusion (lignes=réel, colonnes=prédit) :")
    print("           prédit UTILE  prédit INUTILE")
    for label, ligne in zip(labels, matrice):
        print(f"réel {label:8s} {ligne[0]:>10d}  {ligne[1]:>13d}")
    print()

    evaluer_par_validation_croisee(X, y)

    # Modèle final : réentraîné sur 100% des données (train+test) pour l'artefact sauvegardé,
    # maintenant que l'évaluation ci-dessus a donné une estimation honnête de sa fiabilité.
    pipeline_final = nouveau_pipeline()
    pipeline_final.fit(X, y)
    joblib.dump(pipeline_final, CHEMIN_MODELE)
    print(f"\nModèle final (entraîné sur 100% des données) sauvegardé dans {CHEMIN_MODELE}")


if __name__ == "__main__":
    main()
