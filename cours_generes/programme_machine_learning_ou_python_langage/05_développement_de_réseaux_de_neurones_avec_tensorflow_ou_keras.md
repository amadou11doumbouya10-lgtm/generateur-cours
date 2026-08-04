# Module 5 : Développement de réseaux de neurones avec TensorFlow ou Keras

# Développement de réseaux de neurones avec TensorFlow ou Keras
## Introduction et définition claire
Les réseaux de neurones sont des modèles d'apprentissage automatique inspirés de la structure et du fonctionnement du cerveau humain. Ils sont composés de couches de neurones artificiels qui traitent et transmettent des informations. TensorFlow et Keras sont deux bibliothèques Python populaires pour développer des réseaux de neurones.

### Définition de TensorFlow
TensorFlow est une bibliothèque open-source développée par Google pour l'apprentissage automatique et le traitement de données. Elle permet de créer des modèles de réseaux de neurones complexes et de les entraîner sur de grandes quantités de données.

### Définition de Keras
Keras est une bibliothèque Python de haut niveau pour l'apprentissage automatique qui peut fonctionner sur TensorFlow, Theano ou Microsoft Cognitive Toolkit (CNTK). Elle permet de créer des modèles de réseaux de neurones de manière simple et intuitive.

## Pourquoi utiliser cette technologie (cas d'usage concrets)
Les réseaux de neurones ont de nombreux cas d'usage concrets, notamment :

*   **Reconnaissance d'images** : les réseaux de neurones peuvent être utilisés pour reconnaître les objets et les personnes dans les images.
*   **Traitement du langage naturel** : les réseaux de neurones peuvent être utilisés pour analyser et comprendre le langage humain.
*   **Prévision de séries temporelles** : les réseaux de neurones peuvent être utilisés pour prédire les valeurs futures d'une série temporelle.
*   **Détection de fraude** : les réseaux de neurones peuvent être utilisés pour détecter les transactions frauduleuses.

## Installation et prérequis
Pour utiliser TensorFlow et Keras, vous devez avoir Python installé sur votre ordinateur. Vous pouvez installer TensorFlow et Keras en utilisant pip :

```bash
pip install tensorflow keras
```

Il est également recommandé d'avoir une carte graphique dédiée pour accélérer les calculs.

## Concepts fondamentaux
### Neurone artificiel
Un neurone artificiel est une unité de traitement qui reçoit des entrées, les traite et transmet les résultats. Il est composé de trois parties :

*   **Somme pondérée** : les entrées sont multipliées par des poids et additionnées.
*   **Fonction d'activation** : la somme pondérée est passée à travers une fonction d'activation qui détermine la sortie du neurone.
*   **Sortie** : la sortie du neurone est transmise aux neurones suivants.

### Couches de neurones
Les couches de neurones sont des groupes de neurones qui traitent les informations de manière coordonnée. Il existe plusieurs types de couches, notamment :

*   **Couche d'entrée** : la couche d'entrée reçoit les données d'entrée.
*   **Couches cachées** : les couches cachées traitent les informations et les transmettent aux couches suivantes.
*   **Couche de sortie** : la couche de sortie produit les résultats finaux.

### Entraînement d'un réseau de neurones
L'entraînement d'un réseau de neurones consiste à ajuster les poids et les biais des neurones pour minimiser l'erreur entre les prédictions et les valeurs réelles. Il existe plusieurs algorithmes d'entraînement, notamment :

*   **Régression linéaire** : l'algorithme d'entraînement ajuste les poids pour minimiser l'erreur moyenne entre les prédictions et les valeurs réelles.
*   **Descende de gradient** : l'algorithme d'entraînement ajuste les poids pour minimiser l'erreur moyenne entre les prédictions et les valeurs réelles en utilisant la dérivée de l'erreur par rapport aux poids.

## Exemples de code commentés
### Exemple 1 : Régression linéaire simple
```python
# Importation des bibliothèques nécessaires
import numpy as np
from tensorflow import keras
from sklearn.model_selection import train_test_split

# Génération de données aléatoires
np.random.seed(0)
X = np.random.rand(100, 1)
y = 3 * X + 2 + np.random.randn(100, 1) / 1.5

# Division des données en entraînement et test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Création du modèle
model = keras.Sequential([
    keras.layers.Dense(1, input_shape=[1])
])

# Compilation du modèle
model.compile(optimizer='sgd', loss='mean_squared_error')

# Entraînement du modèle
model.fit(X_train, y_train, epochs=500, verbose=0)

# Évaluation du modèle
mse = model.evaluate(X_test, y_test)
print(f'MSE : {mse}')
```

### Exemple 2 : Classification de l'iris
```python
# Importation des bibliothèques nécessaires
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from tensorflow import keras

# Chargement du jeu de données Iris
iris = load_iris()
X = iris.data
y = iris.target

# Division des données en entraînement et test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Création du modèle
model = keras.Sequential([
    keras.layers.Dense(10, activation='relu', input_shape=[4]),
    keras.layers.Dense(3, activation='softmax')
])

# Compilation du modèle
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Entraînement du modèle
model.fit(X_train, y_train, epochs=100, verbose=0)

# Évaluation du modèle
test_loss, test_acc = model.evaluate(X_test, y_test)
print(f'Test accuracy : {test_acc}')
```

## Exercices pratiques
1.  **Régression linéaire multiple** : créez un modèle de régression linéaire multiple pour prédire la valeur d'une maison en fonction de ses caractéristiques (nombre de chambres, superficie, etc.).
2.  **Classification de spam** : créez un modèle de classification pour déterminer si un message est un spam ou non en fonction de son contenu.
3.  **Prévision de séries temporelles** : créez un modèle de prévision de séries temporelles pour prédire les ventes d'un produit en fonction des données historiques.

## Erreurs courantes et comment les éviter
1.  **Sous-entraînement** : assurez-vous d'avoir suffisamment de données d'entraînement pour éviter le sous-entraînement.
2.  **Sur-entraînement** : utilisez la régularisation et la validation croisée pour éviter le sur-entraînement.
3.  **Choix du modèle** : choisissez le modèle approprié pour votre problème (régression, classification, etc.).

## Ressources pour aller plus loin
*   **Documentation TensorFlow** : <https://www.tensorflow.org/docs>
*   **Documentation Keras** : <https://keras.io/>
*   **Cours en ligne** : <https://www.coursera.org/specializations/machine-learning>
*   **Livre** : "Deep Learning" de Ian Goodfellow, Yoshua Bengio et Aaron Courville.