# Module 2 : Prétraitement des données et visualisation

# Prétraitement des données et visualisation
## Introduction et définition claire
Le prétraitement des données et la visualisation sont des étapes essentielles dans l'analyse de données. Le prétraitement des données consiste à nettoyer, transformer et préparer les données pour qu'elles soient prêtes à être analysées, tandis que la visualisation permet de représenter les données sous forme graphique pour mieux les comprendre et identifier les tendances.

## Pourquoi utiliser cette technologie (cas d'usage concrets)
Le prétraitement des données et la visualisation sont utilisés dans de nombreux domaines, tels que :
* L'analyse de données pour les entreprises : pour analyser les ventes, les dépenses, les revenus, etc.
* La recherche scientifique : pour analyser les données expérimentales, les données de simulation, etc.
* La santé : pour analyser les données médicales, les données de patients, etc.

Exemples concrets :
* Un entreprise de vente en ligne souhaite analyser ses ventes pour identifier les produits les plus vendus et les régions les plus rentables.
* Un chercheur en physique souhaite analyser les données de simulation pour comprendre le comportement d'un système complexe.
* Un hôpital souhaite analyser les données de patients pour identifier les facteurs de risque de maladies chroniques.

## Installation et prérequis
Pour suivre ce cours, vous aurez besoin de :
* Python 3.x installé sur votre ordinateur
* La bibliothèque Pandas pour le prétraitement des données
* La bibliothèque Matplotlib pour la visualisation des données

Vous pouvez installer ces bibliothèques en utilisant pip :
```bash
pip install pandas matplotlib
```

## Concepts fondamentaux
### Nettoyage des données
Le nettoyage des données consiste à supprimer les données manquantes, les données dupliquées, les données incorrectes, etc.

Exemple de code :
```python
import pandas as pd

# Création d'un dataframe
data = {'Nom': ['Jean', 'Marie', 'Pierre', 'Jean'],
        'Age': [25, 31, 42, 25]}
df = pd.DataFrame(data)

# Suppression des données dupliquées
df = df.drop_duplicates()

print(df)
```

### Transformation des données
La transformation des données consiste à modifier les données pour les rendre plus exploitables.

Exemple de code :
```python
import pandas as pd

# Création d'un dataframe
data = {'Nom': ['Jean', 'Marie', 'Pierre'],
        'Age': [25, 31, 42]}
df = pd.DataFrame(data)

# Transformation de l'âge en catégorie
df['Catégorie'] = pd.cut(df['Age'], bins=[0, 30, 60], labels=['Jeune', 'Adulte', 'Senior'])

print(df)
```

### Visualisation des données
La visualisation des données consiste à représenter les données sous forme graphique.

Exemple de code :
```python
import matplotlib.pyplot as plt
import pandas as pd

# Création d'un dataframe
data = {'Nom': ['Jean', 'Marie', 'Pierre'],
        'Age': [25, 31, 42]}
df = pd.DataFrame(data)

# Création d'un graphique à barres
plt.bar(df['Nom'], df['Age'])
plt.xlabel('Nom')
plt.ylabel('Age')
plt.title('Âge des personnes')
plt.show()
```

## Exemples de code commentés
### Exemple 1 : Analyse des ventes
```python
import pandas as pd
import matplotlib.pyplot as plt

# Création d'un dataframe
data = {'Produit': ['A', 'B', 'C', 'A', 'B', 'C'],
        'Vente': [100, 200, 300, 150, 250, 350]}
df = pd.DataFrame(data)

# Calcul du total des ventes par produit
df_group = df.groupby('Produit')['Vente'].sum()

# Création d'un graphique à barres
plt.bar(df_group.index, df_group.values)
plt.xlabel('Produit')
plt.ylabel('Vente')
plt.title('Ventes par produit')
plt.show()
```

### Exemple 2 : Analyse des dépenses
```python
import pandas as pd
import matplotlib.pyplot as plt

# Création d'un dataframe
data = {'Mois': ['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin'],
        'Dépense': [1000, 1200, 1500, 1800, 2000, 2200]}
df = pd.DataFrame(data)

# Calcul du total des dépenses par mois
df_group = df.groupby('Mois')['Dépense'].sum()

# Création d'un graphique à ligne
plt.plot(df_group.index, df_group.values)
plt.xlabel('Mois')
plt.ylabel('Dépense')
plt.title('Dépenses par mois')
plt.show()
```

## Exercices pratiques
1. Créez un dataframe avec les données suivantes :
 * Nom : Jean, Marie, Pierre
 * Age : 25, 31, 42
 * Ville : Paris, Lyon, Marseille
Calculez le total des personnes par ville et représentez les résultats sous forme graphique.
2. Créez un dataframe avec les données suivantes :
 * Produit : A, B, C
 * Vente : 100, 200, 300
 * Coût : 50, 100, 150
Calculez le bénéfice par produit et représentez les résultats sous forme graphique.

## Erreurs courantes et comment les éviter
* Erreur de syntaxe : vérifiez que votre code est correctement écrit et que les indentations sont correctes.
* Erreur de type : vérifiez que les variables ont le bon type de données.
* Erreur de logique : vérifiez que votre code fait ce que vous voulez qu'il fasse.

## Ressources pour aller plus loin
* Documentation Pandas : <https://pandas.pydata.org/docs/>
* Documentation Matplotlib : <https://matplotlib.org/stable/index.html>
* Cours en ligne : <https://www.datacamp.com/courses/pandas-tutorial-python>
* Livres : "Python pour les données" de Wes McKinney, "Data Analysis with Python" de Wes McKinney et Hadley Wickham.