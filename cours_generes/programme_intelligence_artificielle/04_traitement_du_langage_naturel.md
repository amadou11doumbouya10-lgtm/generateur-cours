# Module 4 : Traitement du langage naturel

# Cours de Traitement du Langage Naturel (TLN) avec Python
## Introduction et définition
Le Traitement du Langage Naturel (TLN) est une discipline qui vise à développer des systèmes capables de comprendre, d'interpréter et de générer du langage humain. Cette technologie permet aux ordinateurs de traiter et d'analyser des données textuelles pour en extraire des informations pertinentes.

## Pourquoi utiliser cette technologie ?
Le TLN a de nombreux cas d'usage concrets, notamment :

* **Analyse de sentiments** : déterminer si un texte est positif, négatif ou neutre
* **Reconnaissance d'entités nommées** : identifier les noms de personnes, de lieux et d'organisations dans un texte
* **Classification de texte** : classer des textes en catégories prédéfinies (par exemple, spam/non-spam)
* **Traduction automatique** : traduire des textes d'une langue à une autre

## Installation et prérequis
Pour commencer à utiliser le TLN avec Python, vous aurez besoin de :

* **Python 3.x** : la dernière version de Python
* **NLTK** (Natural Language Toolkit) : une bibliothèque Python pour le TLN
* **spaCy** : une autre bibliothèque Python pour le TLN

 Vous pouvez installer ces bibliothèques en utilisant pip :
```bash
pip install nltk spacy
```
## Concepts fondamentaux
Voici quelques concepts fondamentaux du TLN :

* **Tokenisation** : le processus de division d'un texte en mots ou tokens
* **Lemmatisation** : le processus de réduction d'un mot à sa forme de base (par exemple, "running" -> "run")
* **Étiquetage part-of-speech** : le processus d'identification de la partie du discours d'un mot (par exemple, nom, verbe, adjectif)

## Exemples de code commentés
### Tokenisation
```python
import nltk
from nltk.tokenize import word_tokenize

texte = "Bonjour, comment allez-vous?"
tokens = word_tokenize(texte)
print(tokens)  # ["Bonjour,", "comment", "allez-vous?"]
```
### Lemmatisation
```python
import nltk
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()
mot = "running"
lemme = lemmatizer.lemmatize(mot)
print(lemme)  # "run"
```
### Étiquetage part-of-speech
```python
import spacy

nlp = spacy.load("fr_core_news_sm")
texte = "Le chat est sur le canapé."
doc = nlp(texte)
for token in doc:
    print(token.text, token.pos_)  # ("Le", "DET"), ("chat", "NOUN"), etc.
```
## Exercices pratiques
1. Écrivez un programme qui tokenise un texte et affiche les tokens.
2. Écrivez un programme qui lemmatise un mot et affiche la forme de base.
3. Écrivez un programme qui étiquette les parties du discours d'un texte et affiche les résultats.

## Erreurs courantes et comment les éviter
* **Erreur de tokenisation** : assurez-vous de bien configurer le tokeniseur pour éviter les erreurs de tokenisation.
* **Erreur de lemmatisation** : assurez-vous d'utiliser le bon lemmatiseur pour la langue que vous traitez.
* **Erreur d'étiquetage** : assurez-vous d'utiliser le bon modèle d'étiquetage pour la langue que vous traitez.

## Ressources pour aller plus loin
* **NLTK** : la documentation officielle de NLTK
* **spaCy** : la documentation officielle de spaCy
* **Cours de TLN** : des cours en ligne pour apprendre le TLN avec Python

J'espère que ce cours vous a été utile pour commencer à apprendre le Traitement du Langage Naturel avec Python ! N'hésitez pas à me poser des questions si vous avez besoin d'aide supplémentaire.