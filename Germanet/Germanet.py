
import nltk
import json
from nltk.wsd import lesk
import csv
import re

# get synsets and their
from nltk.corpus import wordnet as wn
from pygermanet import load_germanet
import spacy

class Germanet:
    """This code is used to find all synonym words of a given word.
    The words that are searched here are nouns. If you are interested searching verbs
    please use str(lemmatisedWord) instead of str(lemmatisedWord).capitalize()

    To run this code you need to load germanet data using mongodb using pygerman. See details of how to run germanet here
    https://pypi.org/project/pygermanet/
    mkdir -p ./mongodb
    mongod --dbpath ./mongodb"""


    gn = load_germanet()

    def lematise(self, word):
        """This method returns the lemmatised form of the word if it has lemmatised form, otherwise returns
        the word as it is."""

        if word!="":

            return self.gn.lemmatise(word)

    def getSynonyms(self, word):
        """This method returns the written representation(orth) of all the possible synsets of the given word."""

        synonymSynset=[]

        synonymWords= set()

        for lemmatisedWord in self.lematise(word):
            synsets=self.gn.synsets(str(lemmatisedWord).capitalize())

            for synset in synsets:
                synonymSynset.append(synset)


        for synset in synonymSynset:
            for lemma in synset.lemmas:

                synonymWords.add(lemma.orthForm.strip())

        return synonymWords




