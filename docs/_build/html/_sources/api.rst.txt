###
API
###


Normalization
=============

_class_ NormalizeText

* Attributes

	* stopwords - a list of english stopwords
	* spell_checker - a spell checker of type spellchecker_ml (see https://github.com:EricSchles/spellchecker_ml for more information)

_method_ add_to_stopwords(words: list)

Add stop words to the stopwords attribute

usage::

	```python
	from text_processing_ml.normalization import NormalizeText

	normalizer = NormalizeText()
	normalizer.add_to_stopwords(["Hello", "there"])
	normalizer.remove_stopwords("Hello there") == ''
	```

_method_ remove_stopwords(text: str) -> str

Remove stop words, those found in stopwords attribute.

usage::

	```python
	from text_processing_ml.normalization import NormalizeText

	normalizer = NormalizeText()
	normalizer.add_to_stopwords(["Hello", "there"])
	normalizer.remove_stopwords("Hello there") == ''
	```

_method_ normalize_case(text: str) -> str

convert text to lower case

usage::

	```python

	from text_processing_ml.normalization import NormalizeText

	normalizer = NormalizeText()
	normalizer.normalize_case("Hello") # returns "hello"
	```

_method_ initialize_spellchecker(corpus: str, corpus_name: str, words: list, ner_text: str)

Initialize the spellchecker with text to ignore and a corpus to train on, for more directed text correction

usage::

	```python

	from text_processing_ml.normalization import NormalizeText

	with open("corpus.txt", "r") as f:
		corpus = f.read()

	normalizer = NormalizeText()
	normalizer.initialize_spellchecker(corpus=text, corpus_name="corpus", words=["Hello", "there"], ner_text=text)
	normalizer.make_spelling_correction("Hello there friendz") # returns "Hello there friends"
	```

_method_ strip_punctuation(word: str, return_punctuation: bool) -> str

strips out the punctuation from a word. If return_punctuation is True then the punctuation is returned as well, separately.

usage::

	```python

	from text_processing_ml.normalization import NormalizeText

	normalizer = NormalizeText()
	normalizer.strip_punctuation("Hello,") # returns Hello
	normalizer.strip_punctuation("Hello,", return_punctuation) # returns (Hello, ",")
	```

_method_ correctly_spelled(word: str) -> bool

Checks if the word is correctly spelled, provided the word appears in spellchecker_ml's dictionary of words.  Returns False otherwise

usage::

	```python

	from text_processing_ml.normalization import NormalizeText

	normalizer = NormalizeText()
	normalizer.correctly_spelled("Helo") #returns False
	```

_method_ make_spelling_correction(text: str) -> str

Correct the spelling of a piece of text using a hidden markov model (for now).

usage::

	```python

	from text_processing_ml.normalization import NormalizeText

	normalizer = NormalizeText()
	normalizer.initialize_spellchecker(corpus=text, corpus_name="corpus", words=["Hello", "there"], ner_text=text)
	normalizer.make_spelling_correction("Hello there friendz") # returns "Hello there friends"
	```

_method_ correct_whitespace(text: str) -> str

Normalizes the white space to one space per token.

usage::

	```python

	from text_processing_ml.normalization import NormalizeText

	normalizer = NormalizeText()
	normalizer.correct_whitespace(" Hello  there friends  \t whatever") 
	# returns Hello there friends whatever
	```

Matching
========


Parsing
=======

_class_ ParseText

* Attributes
	* stemmer - a Porter Stemmer from nltk
	* normalizer - the normalizer found elsewhere in the project

_method_  stem_tokens(tokens: list) -> list

Returns a list of stemmed tokens.  Stemming is the process of getting the root word of a word.

Example:

runs -> run
jumping -> jump
flying -> fly

usage::

	```python
	from text_processing_ml.parsing import ParseText

	parser = ParseText()
	parser.stem_tokens("Hello there friends".split()) # returns Hello there friend
	```

_method_ tokenize(text: str) -> list

Tokenize and stem a string of words into stemmed tokens.

useage::

	```python
	from text_processing_ml.parsing import ParseText

	parser = ParseText()
	parser.tokenize("Hello there friends") # ["Hello", "there", "friend"]
	```

_method_ normalize_text(text: str) -> str

Normalize the a piece of text by lower casing it and removing punctuation

