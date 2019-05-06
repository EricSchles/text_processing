###
API
###


Normalization
=============

__class__ NormalizeText

* Attributes

	* stopwords - a list of english stopwords
	* spell_checker - a spell checker of type spellchecker_ml (see https://github.com:EricSchles/spellchecker_ml for more information)

__method__ add_to_stopwords(words: list)

Add stop words to the stopwords attribute

usage::

	```
	from text_processing_ml.normalization import NormalizeText

	normalizer = NormalizeText()
	normalizer.add_to_stopwords(["Hello", "there"])
	normalizer.remove_stopwords("Hello there") == ''
	```

__method__ remove_stopwords(text: str) -> str

Remove stop words, those found in stopwords attribute.

usage::

	```
	from text_processing_ml.normalization import NormalizeText

	normalizer = NormalizeText()
	normalizer.add_to_stopwords(["Hello", "there"])
	normalizer.remove_stopwords("Hello there") == ''
	```

__method__ normalize_case(text: str) -> str

convert text to lower case

usage::

	```

	from text_processing_ml.normalization import NormalizeText

	normalizer = NormalizeText()
	normalizer.normalize_case("Hello") # returns "hello"
	```

__method__ initialize_spellchecker(corpus: str, corpus_name: str, words: list, ner_text: str)

Initialize the spellchecker with text to ignore and a corpus to train on, for more directed text correction

usage::

	```

	from text_processing_ml.normalization import NormalizeText

	with open("corpus.txt", "r") as f:
		corpus = f.read()

	normalizer = NormalizeText()
	normalizer.initialize_spellchecker(corpus=text, corpus_name="corpus", words=["Hello", "there"], ner_text=text)
	normalizer.make_spelling_correction("Hello there friendz") # returns "Hello there friends"
	```

__method__ strip_punctuation(word: str, return_punctuation: bool) -> str

strips out the punctuation from a word. If return_punctuation is True then the punctuation is returned as well, separately.

usage::

	```

	from text_processing_ml.normalization import NormalizeText

	normalizer = NormalizeText()
	normalizer.strip_punctuation("Hello,") # returns Hello
	normalizer.strip_punctuation("Hello,", return_punctuation) # returns (Hello, ",")
	```

__method__ correctly_spelled(word: str) -> bool

Checks if the word is correctly spelled, provided the word appears in spellchecker_ml's dictionary of words.  Returns False otherwise

usage::

	```

	from text_processing_ml.normalization import NormalizeText

	normalizer = NormalizeText()
	normalizer.correctly_spelled("Helo") #returns False
	```

__method__ make_spelling_correction(text: str) -> str

Correct the spelling of a piece of text using a hidden markov model (for now).

usage::

	```

	from text_processing_ml.normalization import NormalizeText

	normalizer = NormalizeText()
	normalizer.initialize_spellchecker(corpus=text, corpus_name="corpus", words=["Hello", "there"], ner_text=text)
	normalizer.make_spelling_correction("Hello there friendz") # returns "Hello there friends"
	```

__method__ correct_whitespace(text: str) -> str

Normalizes the white space to one space per token.

usage::

	```

	from text_processing_ml.normalization import NormalizeText

	normalizer = NormalizeText()
	normalizer.correct_whitespace(" Hello  there friends  \t whatever") 
	# returns Hello there friends whatever
	```

Matching
========


Parsing
=======

__class__ ParseText

* Attributes
	* stemmer - a Porter Stemmer from nltk
	* normalizer - the normalizer found elsewhere in the project

__method__  stem_tokens(tokens: list) -> list

Returns a list of stemmed tokens.  Stemming is the process of getting the root word of a word.

Example:

runs -> run
jumping -> jump
flying -> fly

usage::

	```
	from text_processing_ml.parsing import ParseText

	parser = ParseText()
	parser.stem_tokens("Hello there friends".split()) # returns Hello there friend
	```

__method__ tokenize(text: str) -> list

Tokenize and stem a string of words into stemmed tokens.

usage::

	```
	from text_processing_ml.parsing import ParseText

	parser = ParseText()
	parser.tokenize("Hello there friends") # ["Hello", "there", "friend"]
	```

__method__ normalize_text(text: str) -> str

Normalize the a piece of text by lower casing it and removing punctuation

usage::

	```
	from text_processing_ml.parsing import ParseText

	parser = ParseText()
	parser.normalize_text("Hello there, friend") # returns hello there friend
	```

__method__ tfidf(documents: list) 

Returns the Term frequency given the inverse document frequency

usage::
	
	```
	from text_processing_ml.parsing import ParseText

	parser = ParseText()
	parser.tfidf(["Hello there friends", "How are you doing?", "what's up"])
	# returns the term frequency matrix
	```

	
