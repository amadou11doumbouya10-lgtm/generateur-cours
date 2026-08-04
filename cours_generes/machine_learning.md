# Cours : Machine learning

# Cours d'apprentissage automatique avec Python
## Introduction et définition claire

L'apprentissage automatique, également appelé apprentissage artificiel ou apprentissage statistique, est un champ d'étude de l'intelligence artificielle qui vise à donner aux ordinateurs la capacité d'« apprendre » à partir de données. Cela signifie que les ordinateurs peuvent améliorer leurs performances pour résoudre des tâches sans être explicitement programmés pour chacune. L'apprentissage automatique repose sur des approches mathématiques et statistiques pour créer des modèles dont l'erreur statistique moyenne est la plus faible possible.

## Pourquoi utiliser cette technologie (cas d'usage concrets)

L'apprentissage automatique a de nombreuses applications concrètes dans des domaines tels que :

* La reconnaissance d'images et de sons
* La prédiction de valeurs (par exemple, les prix des actions ou les prévisions météorologiques)
* La classification de données (par exemple, la détection de spams dans les e-mails)
* La recommandation de produits ou de contenus
* La conduite autonome des véhicules

Voici quelques exemples concrets d'utilisation de l'apprentissage automatique :

* Les assistants virtuels comme Siri, Google Assistant ou Alexa utilisent l'apprentissage automatique pour comprendre les commandes vocales et répondre aux questions.
* Les plateformes de réseaux sociaux comme Facebook ou Instagram utilisent l'apprentissage automatique pour personnaliser les contenus et les publicités en fonction des préférences des utilisateurs.
* Les entreprises de vente en ligne comme Amazon utilisent l'apprentissage automatique pour recommander des produits aux clients en fonction de leurs achats précédents.

## Installation et prérequis

Pour commencer avec l'apprentissage automatique en Python, vous aurez besoin d'installer les bibliothèques suivantes :

* `scikit-learn` pour les algorithmes d'apprentissage automatique
* `numpy` pour les calculs numériques
* `pandas` pour la manipulation de données
* `matplotlib` pour la visualisation de données

Vous pouvez installer ces bibliothèques en utilisant `pip` :
```bash
pip install scikit-learn numpy pandas matplotlib
```
## Concepts fondamentaux

Voici quelques concepts fondamentaux de l'apprentissage automatique :

* **Données d'entraînement** : les données utilisées pour entraîner le modèle
* **Données de test** : les données utilisées pour évaluer les performances du modèle
* **Modèle** : l'algorithme d'apprentissage automatique qui est entraîné sur les données d'entraînement
* **Hyperparamètres** : les paramètres du modèle qui doivent être ajustés pour optimiser les performances

## Exemples de code commentés

### Exemple 1 : Classification de données

Dans cet exemple, nous allons utiliser l'algorithme de classification `LogisticRegression` pour prédire si un client va acheter un produit ou non en fonction de son âge et de son revenu.
```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Chargement des données
data = pd.read_csv('data.csv')

# Séparation des données en entraînement et test
X_train, X_test, y_train, y_test = train_test_split(data[['age', 'revenu']], data['achat'], test_size=0.2, random_state=42)

# Entraînement du modèle
model = LogisticRegression()
model.fit(X_train, y_train)

# Prédiction sur les données de test
y_pred = model.predict(X_test)

# Évaluation des performances
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy : {accuracy:.2f}')
```
### Exemple 2 : Régression linéaire

Dans cet exemple, nous allons utiliser l'algorithme de régression linéaire `LinearRegression` pour prédire le prix d'un appartement en fonction de sa superficie.
```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Chargement des données
data = pd.read_csv('data.csv')

# Séparation des données en entraînement et test
X_train, X_test, y_train, y_test = train_test_split(data[['superficie']], data['prix'], test_size=0.2, random_state=42)

# Entraînement du modèle
model = LinearRegression()
model.fit(X_train, y_train)

# Prédiction sur les données de test
y_pred = model.predict(X_test)

# Évaluation des performances
mse = mean_squared_error(y_test, y_pred)
print(f'MSE : {mse:.2f}')
```
## Exercices pratiques

1. Utilisez l'algorithme de classification `DecisionTreeClassifier` pour prédire si un client va acheter un produit ou non en fonction de son âge, de son revenu et de son sexe.
2. Utilisez l'algorithme de régression linéaire `LinearRegression` pour prédire le prix d'un appartement en fonction de sa superficie et de son emplacement.

## Erreurs courantes et comment les éviter

* **Sous-ajustement** : le modèle est trop simple et ne parvient pas à capturer les relations entre les variables.
 + Solution : augmenter la complexité du modèle ou ajouter plus de données d'entraînement.
* **Sur-ajustement** : le modèle est trop complexe et se spécialise sur les données d'entraînement.
 + Solution : diminuer la complexité du modèle ou utiliser des techniques de régularisation.
* **Données déséquilibrées** : les classes sont déséquilibrées, ce qui peut affecter les performances du modèle.
 + Solution : utiliser des techniques de rééchantillonnage ou de pondération des classes.

## Ressources pour aller plus loin

* **Livres** :
 + "Python Machine Learning" de Sebastian Raschka
 + "Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow" de Aurélien Géron
* **Cours en ligne** :
 + "Machine Learning" de Coursera
 + "Deep Learning" de Coursera
* **Communautés** :
 + Kaggle
 + Reddit (r/MachineLearning et r/AskScience)