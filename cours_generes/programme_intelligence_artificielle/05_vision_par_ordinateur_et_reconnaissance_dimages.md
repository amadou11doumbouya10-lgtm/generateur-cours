# Module 5 : Vision par ordinateur et reconnaissance d'images

# Cours de Vision par Ordinateur et Reconnaissance d'Images
## Introduction et Définition
La vision par ordinateur est un domaine de l'intelligence artificielle qui permet aux ordinateurs d'interpréter et de comprendre le contenu d'images et de vidéos. Cela inclut la reconnaissance d'objets, la détection de mouvements, la segmentation d'images, etc. La reconnaissance d'images est une sous-discipline de la vision par ordinateur qui se concentre spécifiquement sur l'identification et la classification d'objets ou de caractéristiques dans les images.

## Pourquoi Utiliser cette Technologie
La vision par ordinateur et la reconnaissance d'images ont de nombreux cas d'usage concrets dans différents domaines tels que :
- **Sécurité** : détection de visages, reconnaissance de plaques d'immatriculation, etc.
- **Santé** : analyse d'images médicales pour le diagnostic de maladies.
- **Industrie** : inspection de produits, suivi de la chaîne de production, etc.
- **Véhicules autonomes** : détection d'obstacles, reconnaissance de panneaux de signalisation, etc.

## Installation et Prérequis
Pour commencer avec la vision par ordinateur et la reconnaissance d'images en Python, vous aurez besoin d'installer les bibliothèques suivantes :
- **OpenCV** : une bibliothèque très populaire pour la vision par ordinateur.
- **TensorFlow** ou **PyTorch** : pour la reconnaissance d'images et l'apprentissage automatique.
- **NumPy** et **Matplotlib** : pour la manipulation et la visualisation de données.

Vous pouvez installer ces bibliothèques en utilisant pip :
```bash
pip install opencv-python tensorflow numpy matplotlib
```

## Concepts Fondamentaux
### 1. Traitement d'Images
Le traitement d'images est le processus de modification d'images pour améliorer leur qualité ou pour en extraire des informations. Cela peut inclure la conversion d'images en niveaux de gris, l'application de filtres pour réduire le bruit, etc.

### 2. Reconnaissance d'Images
La reconnaissance d'images est le processus d'identification et de classification d'objets ou de caractéristiques dans les images. Cela peut être réalisé en utilisant des réseaux de neurones convolutionnels (CNN).

## Exemples de Code Commentés
### Exemple 1 : Lecture et Affichage d'une Image
```python
import cv2

# Charger l'image
img = cv2.imread('image.jpg')

# Afficher l'image
cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

### Exemple 2 : Conversion d'une Image en Niveaux de Gris
```python
import cv2

# Charger l'image
img = cv2.imread('image.jpg')

# Convertir l'image en niveaux de gris
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Afficher l'image en niveaux de gris
cv2.imshow('Image en Niveaux de Gris', gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

### Exemple 3 : Reconnaissance d'Images avec TensorFlow
```python
import tensorflow as tf
from tensorflow import keras
from sklearn.model_selection import train_test_split
from PIL import Image
import numpy as np

# Charger le jeu de données
(x_train, y_train), (x_test, y_test) = keras.datasets.cifar10.load_data()

# Normaliser les données
x_train = x_train / 255.0
x_test = x_test / 255.0

# Créer le modèle
model = keras.models.Sequential([
    keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=x_train.shape[1:]),
    keras.layers.MaxPooling2D((2, 2)),
    keras.layers.Flatten(),
    keras.layers.Dense(64, activation='relu'),
    keras.layers.Dense(10, activation='softmax')
])

# Compiler le modèle
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Entraîner le modèle
model.fit(x_train, y_train, epochs=10, validation_data=(x_test, y_test))
```

## Exercices Pratiques
1. **Exercice 1** : Charger une image et afficher ses propriétés (taille, nombre de canaux, etc.).
2. **Exercice 2** : Convertir une image en niveaux de gris et appliquer un filtre pour réduire le bruit.
3. **Exercice 3** : Créer un modèle de reconnaissance d'images pour classifier des images de chiffres (0-9).

## Erreurs Courantes et Comment les Éviter
- **Erreur 1** : Ne pas importer les bibliothèques nécessaires.
  - **Solution** : Assurez-vous d'importer toutes les bibliothèques nécessaires avant de commencer à coder.
- **Erreur 2** : Ne pas normaliser les données d'entraînement.
  - **Solution** : Normalisez toujours les données d'entraînement pour améliorer la performance du modèle.

## Ressources pour Aller Plus Loin
- **Site Web OpenCV** : [https://opencv.org/](https://opencv.org/)
- **Documentation TensorFlow** : [https://www.tensorflow.org/docs](https://www.tensorflow.org/docs)
- **Cours en Ligne** : [https://www.coursera.org/](https://www.coursera.org/), [https://www.edx.org/](https://www.edx.org/)