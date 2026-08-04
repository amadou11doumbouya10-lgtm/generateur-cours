# Module 2 : Apprentissage automatique avec Python

# Cours d'Apprentissage Automatique avec Python
## Introduction et Définition

L'apprentissage automatique (AA) est un sous-domaine de l'intelligence artificielle (IA) qui permet aux machines d'apprendre à partir de données sans être explicitement programmées. Il s'agit d'un champ en constante évolution, avec des applications variées dans des domaines tels que la reconnaissance d'images, la prédiction de séries temporelles, la classification de texte, etc.

Python est un langage de programmation idéal pour l'apprentissage automatique en raison de sa simplicité, de sa flexibilité et de l'existence de nombreuses bibliothèques dédiées à l'AA, telles que scikit-learn, TensorFlow et PyTorch.

## Pourquoi Utiliser l'Apprentissage Automatique ?

L'apprentissage automatique offre de nombreuses possibilités pour améliorer les processus, automatiser les tâches et prendre des décisions éclairées sur la base de données. Voici quelques cas d'usage concrets :

- **Classification de spam** : les algorithmes d'apprentissage automatique peuvent être entraînés pour classifier les emails en spam ou non-spam, améliorant ainsi la gestion des boîtes de réception.
- **Reconnaissance d'images** : les modèles d'apprentissage automatique peuvent être utilisés pour reconnaître les objets, les visages et les texte dans les images.
- **Prédiction de ventes** : l'apprentissage automatique peut être appliqué pour prédire les ventes futures sur la base des données historiques.

## Installation et Prérequis

Avant de commencer, assurez-vous d'avoir Python installé sur votre machine. Vous pouvez télécharger la dernière version de Python depuis le [site officiel de Python](https://www.python.org/).

Vous aurez également besoin d'installer des bibliothèques supplémentaires. Vous pouvez les installer en utilisant pip, le gestionnaire de packages Python :

```bash
pip install numpy pandas scikit-learn tensorflow
```

## Concepts Fondamentaux

- **Données d'entraînement** : les données utilisées pour apprendre aux modèles à faire des prédictions.
- **Données de test** : les données utilisées pour évaluer les performances des modèles.
- **Modèle** : une représentation mathématique qui apprend à partir des données d'entraînement et fait des prédictions sur les données de test.
- **Entraînement** : le processus d'apprentissage du modèle à partir des données d'entraînement.

## Exemples de Code Commentés

### Exemple 1 : Classification Simple

```python
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Chargement du jeu de données Iris
iris = load_iris()
X = iris.data
y = iris.target

# Division des données en entraînement et test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Entraînement d'un modèle de régression logistique
model = LogisticRegression()
model.fit(X_train, y_train)

# Prédiction sur les données de test
y_pred = model.predict(X_test)

# Évaluation de la précision du modèle
accuracy = accuracy_score(y_test, y_pred)
print(f"Précision : {accuracy:.2f}")
```

### Exemple 2 : Régression Linéaire

```python
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Génération de données aléatoires pour la régression linéaire
np.random.seed(0)
X = np.random.rand(100, 1)
y = 3 + 2 * X + np.random.randn(100, 1) / 1.5

# Entraînement d'un modèle de régression linéaire
model = LinearRegression()
model.fit(X, y)

# Prédiction
y_pred = model.predict(X)

# Tracé des données et de la droite de régression
plt.scatter(X, y, label="Données")
plt.plot(X, y_pred, color="red", label="Régression linéaire")
plt.legend()
plt.show()
```

## Exercices Pratiques

1. **Classification de chiffres** : utilisez le jeu de données MNIST pour entraîner un modèle de classification de chiffres manuscrits.
2. **Prédiction de prix de logement** : utilisez le jeu de données Boston Housing pour prédire les prix de logement en fonction de caractéristiques telles que le nombre de chambres et la distance au centre-ville.

## Erreurs Courantes et Comment les Éviter

- **Surdimenionnement** : utilisez la régularisation L1 ou L2 pour éviter le surdimensionnement.
- **Sous-dimensionnement** : utilisez des méthodes de sélection de modèles ou de cross-validation pour éviter le sous-dimensionnement.
- **Données déséquilibrées** : utilisez des techniques de rééquilibrage des données, telles que le SMOTE, pour éviter les problèmes de déséquilibre des classes.

## Ressources pour Aller Plus Loin

- **Livres** :
  - "Python Machine Learning" de Sebastian Raschka
  - "Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow" d'Aurélien Géron
- **Cours en ligne** :
  - "Machine Learning" de Andrew Ng sur Coursera
  - "Deep Learning" de Ian Goodfellow, Yoshua Bengio et Aaron Courville sur Coursera
- **Communautés** :
  - Kaggle : une plateforme de concours d'apprentissage automatique
  - Reddit (r/MachineLearning et r/Python) : des communautés actives pour discuter d'apprentissage automatique et de Python.