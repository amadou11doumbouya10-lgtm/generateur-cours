# Module 2 : Compréhension de l'algorithme K-Means

# Compréhension de l'algorithme K-Means
=====================================

## Introduction et définition claire
-------------------------------

L'algorithme K-Means est une technique de classification non supervisée qui permet de regrouper des données similaires en clusters. Il est couramment utilisé pour l'analyse de données, la reconnaissance de formes et la compression de données. L'algorithme K-Means est simple à mettre en œuvre et rapide à exécuter, ce qui en fait un outil populaire pour les applications de traitement de données.

## Pourquoi utiliser cette technologie (cas d'usage concrets)
--------------------------------------------------------

L'algorithme K-Means est utile dans de nombreux cas d'usage, tels que :

*   **Analyse de clientèle** : pour regrouper les clients en fonction de leurs caractéristiques démographiques et de leurs habitudes d'achat.
*   **Reconnaissance de formes** : pour identifier les formes et les modèles dans les données.
*   **Compression de données** : pour réduire la quantité de données en regroupant les données similaires.
*   **Recommandation de produits** : pour suggérer des produits aux clients en fonction de leurs préférences.

## Installation et prérequis
---------------------------

Pour utiliser l'algorithme K-Means en Python, vous devez avoir installé les bibliothèques suivantes :

*   **NumPy** : pour les opérations numériques.
*   **SciPy** : pour les algorithmes scientifiques.
*   **Scikit-learn** : pour les algorithmes de machine learning, y compris K-Means.

 Vous pouvez installer ces bibliothèques en utilisant pip :

```bash
pip install numpy scipy scikit-learn
```

## Concepts fondamentaux
----------------------

L'algorithme K-Means repose sur les concepts suivants :

*   **Cluster** : un groupe de données similaires.
*   **Centroïde** : le point central d'un cluster.
*   **Distance** : la distance entre deux points.

L'algorithme K-Means fonctionne de la manière suivante :

1.  **Initialisation** : les centroïdes sont initialisés de manière aléatoire.
2.  **Assignation** : chaque donnée est assignée au cluster dont le centroïde est le plus proche.
3.  **Mise à jour** : les centroïdes sont mis à jour en fonction des données assignées à chaque cluster.
4.  **Répétition** : les étapes 2 et 3 sont répétées jusqu'à convergence.

## Exemples de code commentés
---------------------------

### Exemple 1 : K-Means simple

```python
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Génération de données aléatoires
np.random.seed(0)
donnees = np.random.rand(100, 2)

# Création d'un modèle K-Means
modele = KMeans(n_clusters=3)

# Entraînement du modèle
modele.fit(donnees)

# Prédictions
predictions = modele.predict(donnees)

# Affichage des résultats
plt.scatter(donnees[:, 0], donnees[:, 1], c=predictions)
plt.show()
```

### Exemple 2 : K-Means avec évaluation

```python
import numpy as np
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt

# Génération de données aléatoires
np.random.seed(0)
donnees = np.random.rand(100, 2)

# Création d'un modèle K-Means
modele = KMeans(n_clusters=3)

# Entraînement du modèle
modele.fit(donnees)

# Prédictions
predictions = modele.predict(donnees)

# Évaluation du modèle
score = silhouette_score(donnees, predictions)
print("Score de silhouette : ", score)

# Affichage des résultats
plt.scatter(donnees[:, 0], donnees[:, 1], c=predictions)
plt.show()
```

## Exercices pratiques avec énoncés
----------------------------------

1.  **Exercice 1** : implémentez l'algorithme K-Means pour regrouper les données suivantes en 2 clusters :
    *   Données : \[(1, 2), (2, 3), (3, 4), (4, 5), (5, 6)\]
    *   Centroïdes initiaux : \[(1, 2), (5, 6)\]
2.  **Exercice 2** : utilisez l'algorithme K-Means pour identifier les clusters dans les données suivantes :
    *   Données : \[(1, 1), (1, 2), (2, 1), (2, 2), (10, 10), (10, 11), (11, 10), (11, 11)\]
    *   Nombre de clusters : 2

## Erreurs courantes et comment les éviter
--------------------------------------

*   **Erreur 1** : choix du nombre de clusters incorrect.
    *   Solution : utilisez la méthode du coude ou la méthode de silhouette pour déterminer le nombre optimal de clusters.
*   **Erreur 2** : initialisation des centroïdes incorrecte.
    *   Solution : utilisez la méthode de initialisation K-Means++ pour améliorer la convergence de l'algorithme.

## Ressources pour aller plus loin
----------------------------------

*   **Livre** : "Pattern Recognition and Machine Learning" de Christopher Bishop.
*   **Cours en ligne** : "Machine Learning" de Andrew Ng sur Coursera.
*   **Bibliothèque Python** : Scikit-learn pour les algorithmes de machine learning, y compris K-Means.