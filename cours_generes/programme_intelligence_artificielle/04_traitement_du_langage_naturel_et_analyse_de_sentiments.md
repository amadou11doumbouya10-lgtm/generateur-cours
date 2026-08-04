# Module 4 : Traitement du langage naturel et analyse de sentiments

# Introduction au Traitement du Langage Naturel et Analyse de Sentiments
## Définition et Introduction
Le Traitement du Langage Naturel (TLN) est un domaine de l'intelligence artificielle qui vise à permettre aux ordinateurs de comprendre, d'interpréter et de générer du langage humain. L'Analyse de Sentiments est une sous-discipline du TLN qui se concentre sur l'identification et la classification des émotions et des sentiments exprimés dans un texte.

## Pourquoi Utiliser cette Technologie ?
Le TLN et l'Analyse de Sentiments ont de nombreux cas d'usage concrets, tels que :
* L'analyse de la satisfaction client à partir de commentaires en ligne
* La détection de la fraude dans les réseaux sociaux
* La recommandation de produits en fonction des préférences des utilisateurs
* La surveillance de la santé mentale à partir de données de réseaux sociaux

## Installation et Prérequis
Pour commencer avec le TLN et l'Analyse de Sentiments en Python, vous aurez besoin de :
* Python 3.8 ou supérieur
* La bibliothèque NLTK (Natural Language Toolkit)
* La bibliothèque spaCy
* La bibliothèque scikit-learn

Vous pouvez installer ces bibliothèques en utilisant pip :
```bash
pip install nltk spacy scikit-learn
```

## Concepts Fondamentaux
### Le Traitement du Langage Naturel
Le TLN implique plusieurs étapes :
1. **Tokenisation** : découper le texte en mots ou tokens
2. **Suppression des stop-words** : supprimer les mots communs sans signification (comme "le", "la", "les")
3. **Lemmatisation** : réduire les mots à leur forme de base (comme "courir" au lieu de "courais")
4. **Vectorisation** : représenter les mots sous forme de vecteurs numériques

### L'Analyse de Sentiments
L'Analyse de Sentiments implique :
1. **La classification** : classer les textes en fonction de leur sentiment (positif, négatif, neutre)
2. **La régulation** : identifier les émotions et les sentiments exprimés dans le texte

## Exemples de Code Commentés
### Tokenisation et Suppression des Stop-words
```python
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

texte = "Je suis très heureux de vous voir!"
tokens = word_tokenize(texte)
stop_words = set(stopwords.words('french'))

tokens_filtres = [token for token in tokens if token.lower() not in stop_words]
print(tokens_filtres)
```

### Lemmatisation
```python
import spacy

nlp = spacy.load('fr_core_news_sm')
texte = "Je suis très heureux de vous voir!"
doc = nlp(texte)

lemmes = [token.lemma_ for token in doc]
print(lemmes)
```

### Vectorisation
```python
from sklearn.feature_extraction.text import TfidfVectorizer

textes = ["Je suis très heureux de vous voir!", "Je suis très triste aujourd'hui."]
vectorizer = TfidfVectorizer()

vecteurs = vectorizer.fit_transform(textes)
print(vecteurs.toarray())
```

### Classification de Sentiments
```python
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import TfidfVectorizer

textes = ["Je suis très heureux de vous voir!", "Je suis très triste aujourd'hui."]
sentiments = [1, 0]  # 1 pour positif, 0 pour négatif

vectorizer = TfidfVectorizer()
vecteurs = vectorizer.fit_transform(textes)

clf = MultinomialNB()
clf.fit(vecteurs, sentiments)

nouveau_texte = "Je suis très heureux de vous revoir!"
nouveau_vecteur = vectorizer.transform([nouveau_texte])
prediction = clf.predict(nouveau_vecteur)
print(prediction)
```

## Exercices Pratiques
1. Écrivez un programme qui tokenise un texte et supprime les stop-words.
2. Écrivez un programme qui réalise une lemmatisation sur un texte.
3. Écrivez un programme qui vectorise un texte et classe les sentiments.

## Erreurs Courantes et Comment les Éviter
* **Erreur de tokenisation** : assurez-vous de bien configurer la tokenisation pour votre langue.
* **Erreur de classification** : assurez-vous de bien étiqueter vos données et de choisir le bon modèle de classification.

## Ressources pour Aller Plus Loin
* **NLTK** : documentation officielle
* **spaCy** : documentation officielle
* **scikit-learn** : documentation officielle
* **Cours en ligne** : Stanford CS224D, Coursera NLP Specialization

Note : Ce cours est un aperçu général du Traitement du Langage Naturel et de l'Analyse de Sentiments. Pour une compréhension plus approfondie, il est recommandé de consulter les ressources supplémentaires et de pratiquer avec des exercices concrets.