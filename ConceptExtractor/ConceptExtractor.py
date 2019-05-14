from QuestionConceptExtractor.ConceptExtractor.ExceptionalTokens import *
from QuestionConceptExtractor.Germanet.Germanet import *

nlp = spacy.load('de')

class ConceptExtractor:
    """ This class is used to extract concepts from a given sentence. The definition of concepts is very shallow and
    we include all terms that are not stop words, punctuations, etc. However, this class further provides options for users
    to extract nouns as concepts and only concepts that are defined in Germanet."""
    def __init__(self):
        # en_stop = set(nltk.corpus.stopwords.words('de'))
        nlp = spacy.load('de')


    def extract(self, sentence):
        """This method reads a sentence, removes all the stop words, and punctuations. It also remove abbreviations and nonContentBearing
        terms that are supplied by the user or the default terms initially indentified in ExceptionalTokens.py class"""

        tokens=self.tokenize(sentence)
        tokens=self.tokenize_and_remove_stopword(sentence)
        tokens= self.remove_abbreviations(tokens)
        tokens= self.remove_nonConceptBearingTokens(tokens)
        return tokens



    def extract_nouns_only_as_concept (self, sentence):
        """This method reads a sentence, removes all the stop words, and punctuations. It also remove abbreviations and nonContentBearing
               terms that are supplied by the user or the default terms initially indentified in ExceptionalTokens.py class.

            Additionally it filters terms that do not appear as a NOUN. It uses Spacy part of speech to identify the nouns"""

        tokens = self.tokenize(sentence)
        tokens = self.tokenize_and_remove_stopword(sentence)
        tokens = self.remove_abbreviations(tokens)
        tokens = self.remove_nonConceptBearingTokens(tokens)
        tokens  = self.filterNouns(tokens)
        return tokens


    def extract_germanet_concepts_only (self, sentence):
        tokens = self.tokenize(sentence)
        tokens = self.tokenize_and_remove_stopword(sentence)
        tokens = self.remove_abbreviations(tokens)
        tokens = self.remove_nonConceptBearingTokens(tokens)
        tokens = self.filterGermanetConcepts(tokens)
        return tokens

    def tokenize(self, text):
        """ This method tokenizes a piece of text and returns all the tokens of the text"""
        tokens = []
        text = nlp(text)
        for token in text:
            tokens.append(token)
        return tokens

    def tokenize_and_remove_stopword(self, text):
        """ This method tokenizes a piece of text, removes stop words and punctuations and returns all the tokens of the text"""
        tokens=[]
        text = nlp(text)
        for token in text:
            tokens.append(token)

        tokens = [token for token in tokens if not token.is_stop]
        tokens = [token for token in tokens if not token.is_punct]
        return tokens

    def remove_abbreviations(self, tokens):
        """This method removes abbreviations and acronyms tokens identified by linguists who are working on specific linguistic data"""
        exceptions=ExceptionalTokens()
        tokens = [token for token in tokens if str(token).lower() not in exceptions.getAbbreviations()]
        return tokens


    def remove_nonConceptBearingTokens(self, tokens):
        """This method removes non Concept Bearing tokens identified by linguists who are working on specific linguistic data"""
        exceptions = ExceptionalTokens()
        tokens = [token for token in tokens if str(token).lower() not in exceptions.getNonConceptBearingTerms()]
        return tokens

    def filterNouns(self, tokens):
        """This method selects terms whose part of speech is a Noun and treat them as concepts."""

        tokens = [token for token in tokens if token.pos_ in ['NOUN']]
        return tokens

    def filterGermanetConcepts(self, tokens):
        """This method checks if the token is represented in Germanet and if there is an entry for it, it represent it as a concept."""
        gn=Germanet()
        tokens = [token for token in tokens if len(gn.getSynonyms(str(token).capitalize()))>0]
        return tokens