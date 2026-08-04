# Module 6 : Déploiement et optimisation de modèles d'IA

# Déploiement et optimisation de modèles d'IA
## Introduction et définition claire
Le déploiement et l'optimisation de modèles d'IA sont des étapes cruciales dans le processus de développement d'applications intelligentes. Le déploiement consiste à mettre en production un modèle d'IA entraîné, tandis que l'optimisation vise à améliorer les performances du modèle pour qu'il puisse être utilisé de manière efficace dans des environnements réels.

## Pourquoi utiliser cette technologie (cas d'usage concrets)
Les modèles d'IA sont utilisés dans de nombreux domaines, tels que :
* La reconnaissance d'images pour la sécurité et la surveillance
* La prédiction de la demande pour les entreprises de vente en ligne
* La détection de la fraude pour les banques et les institutions financières
* La recommandation de contenu pour les plateformes de streaming

## Installation et prérequis
Pour commencer, il est nécessaire d'avoir :
* Python 3.8 ou supérieur installé sur votre système
* Une connaissance de base de la programmation Python
* Une bibliothèque d'apprentissage automatique telle que scikit-learn ou TensorFlow

## Concepts fondamentaux
### 1. Entraînement d'un modèle
L'entraînement d'un modèle consiste à utiliser un jeu de données pour ajuster les paramètres du modèle afin qu'il puisse faire des prédictions précises.

```python
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# Charger le jeu de données iris
iris = load_iris()
X = iris.data
y = iris.target

# Diviser le jeu de données en entraînement et test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Entraîner un modèle de régression logistique
modele = LogisticRegression()
modele.fit(X_train, y_train)
```

### 2. Déploiement d'un modèle
Le déploiement d'un modèle consiste à mettre en production le modèle entraîné pour qu'il puisse être utilisé pour faire des prédictions sur de nouvelles données.

```python
from sklearn.externals import joblib

# Enregistrer le modèle entraîné
joblib.dump(modele, 'modele_entraîné.pkl')

# Charger le modèle entraîné
modele_chargé = joblib.load('modele_entraîné.pkl')

# Utiliser le modèle pour faire des prédictions
nouvelles_données = [[5.1, 3.5, 1.4, 0.2]]
prédictions = modele_chargé.predict(nouvelles_données)
```

### 3. Optimisation d'un modèle
L'optimisation d'un modèle consiste à ajuster les hyperparamètres du modèle pour améliorer ses performances.

```python
from sklearn.model_selection import GridSearchCV

# Définir les hyperparamètres à optimiser
paramètres = {'C': [0.1, 1, 10]}

# Effectuer une recherche grid pour optimiser les hyperparamètres
recherche = GridSearchCV(LogisticRegression(), paramètres, cv=5)
recherche.fit(X_train, y_train)

# Obtenir le modèle avec les hyperparamètres optimisés
modele_optimisé = recherche.best_estimator_
```

## Exemples de code commentés
### Exemple 1 : Entraînement d'un modèle de classification
```python
# Charger le jeu de données iris
from sklearn.datasets import load_iris
iris = load_iris()
X = iris.data
y = iris.target

# Diviser le jeu de données en entraînement et test
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Entraîner un modèle de régression logistique
from sklearn.linear_model import LogisticRegression
modele = LogisticRegression()
modele.fit(X_train, y_train)

# Évaluer les performances du modèle
from sklearn.metrics import accuracy_score
prédictions = modele.predict(X_test)
print('Précision du modèle :', accuracy_score(y_test, prédictions))
```

### Exemple 2 : Déploiement d'un modèle de prédiction
```python
# Enregistrer le modèle entraîné
from sklearn.externals import joblib
joblib.dump(modele, 'modele_entraîné.pkl')

# Charger le modèle entraîné
modele_chargé = joblib.load('modele_entraîné.pkl')

# Utiliser le modèle pour faire des prédictions
nouvelles_données = [[5.1, 3.5, 1.4, 0.2]]
prédictions = modele_chargé.predict(nouvelles_données)
print('Prédiction du modèle :', prédictions)
```

## Exercices pratiques avec énoncés
1. Entraîner un modèle de classification pour prédire la probabilité que un client achète un produit en fonction de son âge, de son sexe et de son revenu.
2. Déployer un modèle de prédiction pour prédire la valeur d'une maison en fonction de ses caractéristiques (nombre de pièces, superficie, emplacement).
3. Optimiser un modèle de régression linéaire pour prédire la consommation d'énergie d'un bâtiment en fonction de la température extérieure et de la météo.

## Erreurs courantes et comment les éviter
* Erreur de sur-ajustement : utiliser une régularisation (L1 ou L2) pour éviter que le modèle ne soit trop spécialisé dans les données d'entraînement.
* Erreur de sous-ajustement : utiliser un modèle plus complexe ou augmenter la taille de l'ensemble d'entraînement.
* Erreur de sélection de modèle : utiliser une méthode de sélection de modèle (par exemple, cross-validation) pour choisir le meilleur modèle pour le problème.

## Ressources pour aller plus loin
* Livres : "Python Machine Learning" de Sebastian Raschka, "Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow" de Aurélien Géron
* Cours en ligne : "Machine Learning" de Andrew Ng sur Coursera, "Deep Learning" de Ian Goodfellow sur Udacity
* Bibliothèques : scikit-learn, TensorFlow, Keras, PyTorch