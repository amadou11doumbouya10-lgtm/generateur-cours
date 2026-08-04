# Module 3 : Implémentation de modèles de Machine Learning avec scikit-learn

# Introduction à l'Implémentation de Modèles de Machine Learning avec scikit-learn
## Définition et Introduction
L'apprentissage automatique (Machine Learning) est un domaine de l'intelligence artificielle qui consiste à développer des algorithmes capables d'apprendre à partir de données et de prendre des décisions ou faire des prédictions sans être explicitement programmés. Scikit-learn est une bibliothèque Python populaire pour l'apprentissage automatique qui fournit des outils pour diverses tâches, allant de la classification et de la régression à la clustering et à la sélection de features.

## Pourquoi Utiliser Scikit-learn ?
Scikit-learn est utilisé pour une variété de cas d'usage concrets tels que :
- **Classification** : Pour prédire une catégorie ou un étiquetage à partir de données. Par exemple, classer des emails comme spam ou non-spam.
- **Régression** : Pour prédire une valeur numérique continue. Par exemple, prédire le prix d'une maison en fonction de caractéristiques telles que la superficie, le nombre de chambres, etc.
- **Clustering** : Pour regrouper des données similaires ensemble. Par exemple, regrouper des clients en fonction de leurs préférences d'achat.
- **Sélection de features** : Pour identifier les features les plus importantes dans un jeu de données.

## Installation et Prérequis
Pour utiliser scikit-learn, vous devez avoir Python installé sur votre machine. Vous pouvez installer scikit-learn en utilisant pip :
```bash
pip install -U scikit-learn
```
Assurez-vous également d'avoir les bibliothèques suivantes installées : NumPy, SciPy, et Matplotlib.

## Concepts Fondamentaux
### 1. Types de Problèmes
- **Classification** : Problème de prédiction où la cible est catégorique.
- **Régression** : Problème de prédiction où la cible est numérique.
### 2. Évaluation des Modèles
- **Précision** : Nombre de véritables positifs divisé par la somme des véritables positifs et des faux positifs.
- **Rappel** : Nombre de véritables positifs divisé par la somme des véritables positifs et des faux négatifs.
- **F1-score** : Moyenne harmonique de la précision et du rappel.

## Exemples de Code Commentés
### Exemple 1 : Classification avec Iris Dataset
```python
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Chargement du dataset Iris
iris = load_iris()
X = iris.data
y = iris.target

# Division en données d'entraînement et de test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Création et entraînement du modèle
model = LogisticRegression()
model.fit(X_train, y_train)

# Prédiction
y_pred = model.predict(X_test)

# Évaluation
accuracy = accuracy_score(y_test, y_pred)
print(f"Précision : {accuracy:.2f}")
```

### Exemple 2 : Régression avec un Dataset Simple
```python
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Génération de données aléatoires pour la régression
np.random.seed(0)
X = np.random.rand(100, 1)
y = 3 + 2 * X + np.random.randn(100, 1)

# Création et entraînement du modèle
model = LinearRegression()
model.fit(X, y)

# Prédiction
y_pred = model.predict(X)

# Visualisation
plt.scatter(X, y, label='Données')
plt.plot(X, y_pred, color='red', label='Régression linéaire')
plt.legend()
plt.show()
```

## Exercices Pratiques
1. **Classification de Fruits** : Utilisez un dataset de caractéristiques de fruits (par exemple, poids, taille, couleur) pour prédire le type de fruit.
2. **Prédiction de la Consommation d'Énergie** : À partir d'un dataset contenant des informations sur les caractéristiques d'un bâtiment (superficie, nombre d'étages, etc.) et sa consommation d'énergie, entraînez un modèle pour prédire la consommation d'énergie d'un nouveau bâtiment.

## Erreurs Courantes et Comment les Éviter
- **Sous-ajustement (Underfitting)** : Le modèle est trop simple et ne capture pas bien les relations dans les données. Solution : Augmenter la complexité du modèle ou utiliser la régularisation.
- **Surdajustement (Overfitting)** : Le modèle est trop complexe et sur-apprend les données d'entraînement. Solution : Utiliser la régularisation, augmenter la taille du dataset, ou utiliser des techniques de cross-validation.

## Ressources pour Aller Plus Loin
- **Documentation Scikit-learn** : [https://scikit-learn.org/stable/](https://scikit-learn.org/stable/)
- **Cours et Tutorials** : Kaggle, Coursera, edX offrent des cours et des compétitions pour apprendre et pratiquer l'apprentissage automatique.
- **Livres** : "Python Machine Learning" de Sebastian Raschka, "Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow" d'Aurélien Géron.