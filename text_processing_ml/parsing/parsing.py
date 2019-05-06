import nltk
import string
import os

from ..normalization import NormalizeText
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.stem.porter import PorterStemmer

class ParseText:
    def __init__(self):
        self.stemmer = PorterStemmer()
        self.normalizer = NormalizeText()
        
    def stem_tokens(self, tokens: list) -> list:
        """
        Get the stemms of all tokens.
        
        Parameter
        ---------
        tokens - a list of tokens to be stemmed
        
        Output
        ------
        a list of stemmed tokens
        """
        stemmed = []
        for item in tokens:
            stemmed.append(self.stemmer.stem(item))
        return stemmed

    def tokenize(self, text: str) -> list:
        """
        Tokenizes a string to a list of tokens.
        Typically tokens are separated by a single space.
        """
        tokens = nltk.word_tokenize(text)
        stems = self.stem_tokens(tokens)
        return stems

    def normalize_text(self, text: str) -> str:
        """
        Normalize a piece of text by
        * lower casing the text
        * removing any punctuation
        
        Parameter
        ---------
        text - a string of words to normalize
        
        Output
        ------
        the lower cased text without punctuation
        """
        text = self.normalizer.normalize_case(text)
        return " ".join(
            [self.normalizer.strip_punctuation(word)
             for word in text.split(" ")]
        )
        
    def tfidf(self, documents: list):
        """
        Performs Term Frequency inverse document frequency
        on a set of documents

        Parameter
        ---------
        documents - a list of documents, each document is expected to be a string
        
        Output
        ------
        The resulting term frequency matrix
        """
        documents = [self.normalize_text(document) for document in documents]
        tfidf_vectorizer = TfidfVectorizer(tokenizer=self.tokenize, stop_words='english')
        return tfidf_vectorizer.fit_transform(documents)

    
    # to do
    # add text summarization
    # add topic modeling, as well as topic assignment,
    # from a topic model
    # add build your own NER chuncker
    # add build your own POS tagger
    # add some embedding functionality
