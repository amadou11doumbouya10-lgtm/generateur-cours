# Module 2 : Principes de base du Machine Learning

# Cours de Principes de base du Machine Learning
## Introduction et définition claire
Le Machine Learning (ML) est un sous-domaine de l'intelligence artificielle (IA) qui consiste à développer des algorithmes et des modèles capables d'apprendre à partir de données et de prendre des décisions sans être explicitement programmés. L'objectif principal du ML est de permettre aux machines de réaliser des tâches qui normalement nécessiteraient une intelligence humaine, telles que la reconnaissance d'images, la compréhension du langage naturel et la prédiction de résultats.

## Pourquoi utiliser cette technologie (cas d'usage concrets)
Le ML est utilisé dans de nombreux domaines tels que :

* La reconnaissance d'images pour les systèmes de sécurité et les applications de réalité augmentée
* La compréhension du langage naturel pour les assistants vocaux et les chatbots
* La prédiction de résultats pour les systèmes de recommandation et les analyses de marché
* La détection d'anomalies pour les systèmes de sécurité et les applications de surveillance

Exemples concrets :

* Les assistants vocaux tels que Siri, Google Assistant et Alexa utilisent le ML pour comprendre les commandes vocales et répondre en conséquence
* Les applications de reconnaissance d'images telles que Facebook et Google Photos utilisent le ML pour identifier les personnes et les objets dans les images
* Les systèmes de recommandation tels que Netflix et Amazon utilisent le ML pour suggérer des films et des produits aux utilisateurs en fonction de leurs préférences

## Installation et prérequis
Pour commencer avec le ML, vous aurez besoin de :

* Python 3.x (la version la plus récente)
* Une bibliothèque de ML telle que scikit-learn ou TensorFlow
* Un environnement de développement intégré (IDE) tel que PyCharm ou Visual Studio Code
* Des données pour entraîner et tester vos modèles

Vous pouvez installer les bibliothèques de ML à l'aide de pip :
```bash
pip install scikit-learn
pip install tensorflow
```
## Concepts fondamentaux
### Données
Les données sont les informations utilisées pour entraîner et tester les modèles de ML. Les données peuvent être sous forme de tableaux, d'images, de texte, etc.

### Modèles
Les modèles sont les algorithmes et les structures de données utilisés pour apprendre à partir des données et faire des prédictions. Les modèles peuvent être linéaires ou non linéaires, supervisés ou non supervisés.

### Entraînement
L'entraînement est le processus de mise à jour des paramètres du modèle pour minimiser l'erreur entre les prédictions et les valeurs réelles.

### Évaluation
L'évaluation est le processus de mesure de la performance du modèle sur des données de test.

### Hyperparamètres
Les hyperparamètres sont les paramètres du modèle qui doivent être ajustés manuellement pour améliorer la performance du modèle.

## Exemples de code commentés
### Exemple 1 : Régression linéaire simple
```python
# Importer les bibliothèques nécessaires
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Générer des données aléatoires
np.random.seed(0)
X = np.random.rand(100, 1)
y = 3 * X + 2 + np.random.randn(100, 1) / 1.5

# Créer un modèle de régression linéaire
model = LinearRegression()

# Entraîner le modèle
model.fit(X, y)

# Faire des prédictions
y_pred = model.predict(X)

# Afficher les résultats
plt.scatter(X, y)
plt.plot(X, y_pred, color='red')
plt.show()
```
### Exemple 2 : Classification binaire
```python
# Importer les bibliothèques nécessaires
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# Charger le jeu de données Iris
iris = load_iris()
X = iris.data[:, :2]  # Nous n'utilisons que les deux premières caractéristiques
y = iris.target

# Diviser les données en entraînement et test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Créer un modèle de régression logistique
model = LogisticRegression()

# Entraîner le modèle
model.fit(X_train, y_train)

# Faire des prédictions
y_pred = model.predict(X_test)

# Afficher les résultats
print("Précision :", model.score(X_test, y_test))
```
## Exercices pratiques avec énoncés
1. Entraîner un modèle de régression linéaire pour prédire les prix des maisons en fonction de leur superficie.
2. Créer un modèle de classification binaire pour prédire si un client va acheter un produit en fonction de son âge et de son sexe.
3. Entraîner un modèle de clustering pour regrouper des clients en fonction de leurs habitudes d'achat.

## Erreurs courantes et comment les éviter
1. **Sous-ajustement** : Le modèle est trop simple et ne peut pas capturer les relations complexes dans les données.
 * Solution : Augmenter la complexité du modèle ou ajouter plus de données.
2. **Sur-ajustement** : Le modèle est trop complexe et sur-ajuste les données d'entraînement.
 * Solution : Utiliser des techniques de régularisation telles que la régression ridge ou l'élagage.
3. **Données déséquilibrées** : Les classes sont déséquilibrées, ce qui peut affecter la performance du modèle.
 * Solution : Utiliser des techniques telles que la rééchantillonnage ou la pondération des classes.

## Ressources pour aller plus loin
1. **Livres** :
 * "Python Machine Learning" de Sebastian Raschka
 * "Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow" de Aurélien Géron
2. **Cours en ligne** :
 * "Machine Learning" de Andrew Ng sur Coursera
 * "Deep Learning" de Ian Goodfellow sur Udacity
3. **Communautés** :
 * Kaggle : une plateforme de compétition de ML
 * Reddit : r/MachineLearning et r/AskScience