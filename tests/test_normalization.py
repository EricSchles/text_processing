from text_processing.normalization import NormalizeText

def test_strip_punctuation():
    norm = NormalizeText()
    word, punctuation = norm.strip_punctuation("Hello,",
                                               return_punctuation=True)
    assert word == "Hello"
    assert punctuation == ","

def test_correct_whitespace():
    norm = NormalizeText()
    assert norm.correct_whitespace("Hello there  friends") == "Hello there friends"

def test_case_normalization():
    norm = NormalizeText()
    assert norm.normalize_case("HELLO THeRe FRiENDS") == "hello there friends"

def test_initialize_spellchecker_simple():
    norm = NormalizeText()
    try:
        norm.initialize_spellchecker()
        assert True
    except:
        assert False

def test_add_stopwords():
    norm = NormalizeText()
    norm.add_to_stopwords(words=["goat", "bob", "phil"])
    assert norm.remove_stopwords("Hey bob, get the goat from phil") == "Hey"

