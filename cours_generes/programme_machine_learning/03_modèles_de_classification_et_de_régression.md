# Module 3 : Modèles de classification et de régression

# Modèles de Classification et de Régression
## Introduction et Définition
Les modèles de classification et de régression sont des techniques fondamentales dans le domaine de l'apprentissage automatique (ou machine learning). La classification est le processus d'affectation d'une étiquette ou d'une catégorie à un objet ou à un ensemble de données, tandis que la régression est utilisée pour prédire une valeur numérique continue.

## Pourquoi Utiliser Cette Technologie
Les modèles de classification et de régression sont utilisés dans de nombreux cas d'usage concrets :

*   **Classification** :
    *   Reconnaissance d'images : Les modèles de classification sont utilisés pour identifier les objets ou les personnes dans les images.
    *   Analyse de sentiments : Les modèles de classification sont utilisés pour déterminer si un texte est positif, négatif ou neutre.
    *   Détection de spams : Les modèles de classification sont utilisés pour identifier les emails ou les messages qui sont des spams.
*   **Régression** :
    *   Prévision de la demande : Les modèles de régression sont utilisés pour prédire la demande future d'un produit ou d'un service.
    *   Analyse de la relation entre les variables : Les modèles de régression sont utilisés pour étudier la relation entre différentes variables, telles que la relation entre la consommation d'un produit et le revenu.
    *   Prévision des prix : Les modèles de régression sont utilisés pour prédire les prix futurs d'un produit ou d'un service.

## Installation et Prérequis
Pour utiliser les modèles de classification et de régression, vous devez avoir installé les bibliothèques suivantes :

*   `scikit-learn` : une bibliothèque populaire pour l'apprentissage automatique en Python.
*   `pandas` : une bibliothèque pour la manipulation et l'analyse de données.
*   `numpy` : une bibliothèque pour les calculs numériques.

Vous pouvez installer ces bibliothèques en utilisant pip :

```bash
pip install scikit-learn pandas numpy
```

## Concepts Fondamentaux
### Classification
La classification est le processus d'affectation d'une étiquette ou d'une catégorie à un objet ou à un ensemble de données. Les modèles de classification sont entraînés sur un ensemble de données étiquetées et peuvent être utilisés pour prédire l'étiquette d'un objet ou d'un ensemble de données inconnu.

#### Exemple de Code
```python
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Charger le jeu de données Iris
iris = load_iris()
X = iris.data
y = iris.target

# Diviser le jeu de données en ensemble d'entraînement et d'évaluation
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Créer un modèle de régression logistique
model = LogisticRegression()

# Entraîner le modèle
model.fit(X_train, y_train)

# Faire des prédictions
y_pred = model.predict(X_test)

# Évaluer le modèle
accuracy = accuracy_score(y_test, y_pred)
print("Précision du modèle : ", accuracy)
```

### Régression
La régression est utilisée pour prédire une valeur numérique continue. Les modèles de régression sont entraînés sur un ensemble de données et peuvent être utilisés pour prédire la valeur d'une variable cible.

#### Exemple de Code
```python
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Générer un jeu de données de régression
X, y = make_regression(n_samples=100, n_features=1, noise=0.1)

# Diviser le jeu de données en ensemble d'entraînement et d'évaluation
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Créer un modèle de régression linéaire
model = LinearRegression()

# Entraîner le modèle
model.fit(X_train, y_train)

# Faire des prédictions
y_pred = model.predict(X_test)

# Évaluer le modèle
mse = mean_squared_error(y_test, y_pred)
print("Erreur quadratique moyenne : ", mse)
```

## Exercices Pratiques
1.  **Classification** : Utilisez le jeu de données Iris pour entraîner un modèle de classification qui prédit l'espèce d'une fleur en fonction de ses caractéristiques (longueur et largeur des sépales et des pétales).
2.  **Régression** : Utilisez le jeu de données Boston pour entraîner un modèle de régression qui prédit le prix d'une maison en fonction de ses caractéristiques (nombre de chambres, superficie, etc.).

## Erreurs Courantes et Comment les Éviter
*   **Sous-ajustement** : Le modèle est trop simple et ne peut pas capturer les relations complexes dans les données. Solution : Utiliser un modèle plus complexe ou augmenter la taille de l'ensemble d'entraînement.
*   **Sure-ajustement** : Le modèle est trop complexe et s'ajuste trop aux données d'entraînement. Solution : Utiliser une régularisation ou réduire la taille de l'ensemble d'entraînement.
*   **Biais de sélection** : Le modèle est entraîné sur un ensemble de données qui n'est pas représentatif de la population cible. Solution : Utiliser un échantillonnage aléatoire ou collecter des données qui sont représentatives de la population cible.

## Ressources pour Aller Plus Loin
*   **Livres** :
    *   "Python Machine Learning" de Sebastian Raschka
    *   "Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow" de Aurélien Géron
*   **Cours en ligne** :
    *   "Machine Learning" de Andrew Ng sur Coursera
    *   "Deep Learning" de Ian Goodfellow sur Coursera
*   **Communautés en ligne** :
    *   Kaggle
    *   Reddit (r/MachineLearning et r/AskScience)