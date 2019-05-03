from spellchecker import SpellChecker
import spacy
import en_core_web_sm

class NormalizeText:
    def __init__(self,
                 check_whitespace=False,
                 check_spelling=False,
    ):
        self.check_spelling = check_spelling
        self.check_whitespace = check_whitespace
        self.text = None
        self.initialize_spellchecker()

    def initialize_spellchecker(self, words=[], add_ner=False):
        """
        * Initializes the spellchecker and allows for 
        words that are proper knowns.
        Parameters
        ----------
        words - a custom list of words to not adjust
        add_ner - add all words found in the text that are named entities
        to the list of words to not adjust
        """
        if add_ner:
            doc = nlp(self.text)
            words += [entity.text
                      for entity in doc.ents]
        self.check_spelling = True
        self.spell_checker = SpellChecker()
        self.spell_checker.word_frequency.load_words(words)
        
    def correct_spelling(self):
        """
        * Corrects the spelling of likely misspelled words.
        * Initialized with initialize_spellchecker method.
        * If there are spellings you want to not be corrected, 
        call initialize_spellchecker explicitly.
        * Called from the transform method.
        """
        tokens = self.text.split()
        misspelled = self.spell_checker.unknown(tokens)
        self.text = " ".join(
            [self.spell_checker.correction(word)
             for word in misspelled]
        )
            
    def correct_whitespace(self):
        """
        Corrects the whitespace in text, so that 
        there is one white space between each word.
        """
        self.text = ' '.join(self.text.strip().split())
        
    def fit(self, text):
        """
        save the text to the model for preprocessing
        
        Parameters
        ----------
        text - the text to be transformed by transform method
        saved to [OBJECT NAME].text
        """
        self.text = text

    def transform(self):
        """
        calls all transformers that have been specified
        requires you to call [OBJECT NAME].text first
        """
        if not self.text:
            raise Exception("fit some text first with the fit method")
        if self.check_whitespace:
            self.correct_whitespace()
        if self.check_spelling:
            self.correct_spelling()
        return self.text
            
    def fit_transform(self, text):
        self.fit(text)
        return self.transform()
