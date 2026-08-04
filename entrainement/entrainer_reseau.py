"""
Étape 2 (Option B) — Réseau de neurones "from scratch" avec PyTorch.
Réseau volontairement petit + régularisé, avec suivi train/test à chaque
epoch pour observer le compromis biais-variance.

Prérequis : pip install torch scikit-learn pandas
"""

import os
import sys

import pandas as pd
import torch
import torch.nn as nn
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split

if sys.stdout.encoding.lower() != "utf-8":
    sys.stdout.reconfigure(encoding="utf-8")

torch.manual_seed(42)

CHEMIN_CSV = os.path.join(os.path.dirname(os.path.abspath(__file__)), "dataset_pertinence.csv")


class ClassifieurCours(nn.Module):
    """
    Réseau volontairement petit : input -> 8 -> 1.
    Avec ~128 exemples d'entraînement, on veut rester très en dessous
    du nombre d'exemples en paramètres, et on ajoute du dropout pour
    régulariser la seule couche cachée.
    """

    def __init__(self, input_dim, dropout=0.5):
        super().__init__()
        self.fc1 = nn.Linear(input_dim, 8)
        self.dropout = nn.Dropout(dropout)
        self.fc2 = nn.Linear(8, 1)
        self.relu = nn.ReLU()

    def forward(self, x):
        x = self.relu(self.fc1(x))
        x = self.dropout(x)
        return self.fc2(x)  # logits bruts


def charger_dataset(chemin):
    df = pd.read_csv(chemin)
    df["texte"] = df["sujet"].fillna("") + " " + df["extrait"].fillna("")
    return df


def evaluer(modele, X, y_true, critere):
    """Calcule perte + rapport de classification sur un jeu donné, sans backprop."""
    modele.eval()
    with torch.no_grad():
        logits = modele(X)
        perte = critere(logits, y_true).item()
        probas = torch.sigmoid(logits)
        y_pred = (probas >= 0.5).int().numpy().flatten()
    return perte, y_pred


def entrainer():
    df = charger_dataset(CHEMIN_CSV)
    print(f"Dataset chargé : {len(df)} exemples")
    print(df["label"].value_counts())

    y_bin = (df["label"] == "UTILE").astype(int)

    X_train, X_test, y_train, y_test = train_test_split(
        df["texte"], y_bin,
        test_size=0.2, random_state=42, stratify=y_bin
    )

    # max_features réduit : moins de dimensions en entrée = moins de paramètres à apprendre
    vectorizer = TfidfVectorizer(max_features=300, ngram_range=(1, 2))
    X_train_vec = vectorizer.fit_transform(X_train).toarray()
    X_test_vec = vectorizer.transform(X_test).toarray()

    X_train_t = torch.tensor(X_train_vec, dtype=torch.float32)
    y_train_t = torch.tensor(y_train.values, dtype=torch.float32).unsqueeze(1)
    X_test_t = torch.tensor(X_test_vec, dtype=torch.float32)
    y_test_t = torch.tensor(y_test.values, dtype=torch.float32).unsqueeze(1)

    modele = ClassifieurCours(input_dim=X_train_vec.shape[1], dropout=0.5)

    nb_params = sum(p.numel() for p in modele.parameters())
    print(f"\nNombre de paramètres du réseau : {nb_params}")
    print(f"Nombre d'exemples d'entraînement : {len(y_train)}")
    print(f"Ratio paramètres/exemples : {nb_params / len(y_train):.1f}x\n")

    nb_inutile = (y_train == 0).sum()
    nb_utile = (y_train == 1).sum()
    pos_weight = torch.tensor([nb_inutile / max(nb_utile, 1)], dtype=torch.float32)
    critere = nn.BCEWithLogitsLoss(pos_weight=pos_weight)

    # weight_decay = régularisation L2, équivalent en esprit à la régularisation
    # qu'on ajouterait à J(w,b) pour pénaliser les poids trop grands
    optimizer = torch.optim.Adam(modele.parameters(), lr=0.001, weight_decay=1e-3)

    NUM_EPOCHS = 200
    historique = {"epoch": [], "perte_train": [], "perte_test": []}

    for epoch in range(NUM_EPOCHS):
        modele.train()
        optimizer.zero_grad()
        sorties = modele(X_train_t)
        perte_train = critere(sorties, y_train_t)
        perte_train.backward()
        optimizer.step()

        if epoch % 10 == 0 or epoch == NUM_EPOCHS - 1:
            perte_test, _ = evaluer(modele, X_test_t, y_test_t, critere)
            historique["epoch"].append(epoch)
            historique["perte_train"].append(perte_train.item())
            historique["perte_test"].append(perte_test)
            print(f"Epoch {epoch:4d} | Perte train : {perte_train.item():.4f} | Perte test : {perte_test:.4f}")

    # Repère visuel simple : si perte_test remonte pendant que perte_train continue
    # de baisser, c'est le signe classique de surapprentissage
    print("\n--- Repère surapprentissage ---")
    ecarts = [t - e for e, t in zip(historique["perte_train"], historique["perte_test"])]
    if ecarts[-1] > ecarts[len(ecarts) // 2] * 1.5:
        print("[!] L'écart train/test se creuse en fin d'entraînement : signe de surapprentissage.")
    else:
        print("[OK] L'écart train/test reste stable : pas de signe évident de surapprentissage.")

    perte_finale, y_pred = evaluer(modele, X_test_t, y_test_t, critere)
    print("\n=== Rapport de classification (jeu de test) ===")
    print(classification_report(y_test, y_pred, target_names=["INUTILE", "UTILE"]))
    print("=== Matrice de confusion ===")
    print(confusion_matrix(y_test, y_pred))

    return modele, vectorizer, historique


if __name__ == "__main__":
    entrainer()
