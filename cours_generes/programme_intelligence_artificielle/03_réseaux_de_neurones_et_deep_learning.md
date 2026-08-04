# Module 3 : Réseaux de neurones et deep learning

# Réseaux de neurones et deep learning
## Introduction et définition claire
Les réseaux de neurones et le deep learning sont des techniques d'apprentissage automatique (ou machine learning) qui permettent de créer des modèles capables de traiter et d'analyser de grandes quantités de données, notamment des images, des sons et des textes. Ces techniques sont inspirées du fonctionnement du cerveau humain et permettent de résoudre des problèmes complexes tels que la reconnaissance d'images, la traduction automatique et la prédiction de séries temporelles.

## Pourquoi utiliser cette technologie (cas d'usage concrets)
Les réseaux de neurones et le deep learning ont de nombreux cas d'usage concrets, notamment :
* La reconnaissance d'images : les réseaux de neurones peuvent être utilisés pour reconnaître les objets et les personnes dans les images.
* La traduction automatique : les réseaux de neurones peuvent être utilisés pour traduire les textes d'une langue à une autre.
* La prédiction de séries temporelles : les réseaux de neurones peuvent être utilisés pour prédire les valeurs futures d'une série temporelle.
* La détection de fraudes : les réseaux de neurones peuvent être utilisés pour détecter les transactions frauduleuses.

## Installation et prérequis
Pour utiliser les réseaux de neurones et le deep learning en Python, vous devez avoir installé les bibliothèques suivantes :
* TensorFlow ou PyTorch pour la création et l'entraînement des réseaux de neurones.
* NumPy et Pandas pour la manipulation des données.
* Matplotlib et Seaborn pour la visualisation des données.

 Vous pouvez installer ces bibliothèques en utilisant pip :
```bash
pip install tensorflow numpy pandas matplotlib seaborn
```
ou
```bash
pip install torch numpy pandas matplotlib seaborn
```

## Concepts fondamentaux
### 1. Les neurones
Un neurone est une unité de calcul qui prend en entrée une ou plusieurs valeurs, les traite et produit une sortie. Les neurones sont les briques de base des réseaux de neurones.

### 2. Les couches
Les couches sont des ensembles de neurones qui travaillent ensemble pour traiter les données. Les couches peuvent être de différents types, tels que les couches de convolution, les couches de pooling, les couches de flatten, etc.

### 3. L'apprentissage
L'apprentissage est le processus par lequel le réseau de neurones apprend à partir des données. Il existe deux types d'apprentissage : l'apprentissage supervisé et l'apprentissage non supervisé.

### 4. L'entraînement
L'entraînement est le processus par lequel le réseau de neurones est entraîné sur les données d'entraînement. L'entraînement peut être réalisé en utilisant différentes méthodes, telles que la régression linéaire, la régression logistique, etc.

## Exemples de code commentés
### 1. Exemple de code pour la création d'un réseau de neurones simple
```python
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Création du modèle
model = Sequential()

# Ajout d'une couche de neurones
model.add(Dense(64, activation='relu', input_shape=(784,)))

# Ajout d'une couche de sortie
model.add(Dense(10, activation='softmax'))

# Compilation du modèle
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
```

### 2. Exemple de code pour l'entraînement d'un réseau de neurones
```python
import numpy as np
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Chargement des données
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Normalisation des données
x_train = x_train.astype('float32') / 255
x_test = x_test.astype('float32') / 255

# Création du modèle
model = Sequential()

# Ajout d'une couche de neurones
model.add(Dense(64, activation='relu', input_shape=(784,)))

# Ajout d'une couche de sortie
model.add(Dense(10, activation='softmax'))

# Compilation du modèle
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Entraînement du modèle
model.fit(x_train, y_train, epochs=10, batch_size=128, validation_data=(x_test, y_test))
```

## Exercices pratiques avec énoncés
### 1. Créer un réseau de neurones pour la reconnaissance d'images
Créez un réseau de neurones pour la reconnaissance d'images en utilisant le jeu de données MNIST. Le réseau de neurones doit avoir deux couches de neurones et une couche de sortie.

### 2. Entraîner un réseau de neurones pour la prédiction de séries temporelles
Entraînez un réseau de neurones pour la prédiction de séries temporelles en utilisant le jeu de données de ventes de produits. Le réseau de neurones doit avoir trois couches de neurones et une couche de sortie.

## Erreurs courantes et comment les éviter
### 1. Erreur de sur-entraînement
L'erreur de sur-entraînement se produit lorsque le réseau de neurones est entraîné trop longtemps et commence à sur-ajuster les données d'entraînement. Pour éviter cette erreur, vous pouvez utiliser la technique de régularisation ou de dropout.

### 2. Erreur de sous-entraînement
L'erreur de sous-entraînement se produit lorsque le réseau de neurones n'est pas entraîné suffisamment longtemps et ne parvient pas à apprendre les modèles dans les données. Pour éviter cette erreur, vous pouvez augmenter le nombre d'époques d'entraînement ou utiliser une méthode d'optimisation différente.

## Ressources pour aller plus loin
### 1. Livres
* "Deep Learning" de Ian Goodfellow, Yoshua Bengio et Aaron Courville
* "Python Machine Learning" de Sebastian Raschka

### 2. Cours en ligne
* "Deep Learning" de Andrew Ng sur Coursera
* "Machine Learning" de Caltech sur edX

### 3. Sites web
* [www.tensorflow.org](http://www.tensorflow.org)
* [www.pytorch.org](http://www.pytorch.org)
* [www.kaggle.com](http://www.kaggle.com)