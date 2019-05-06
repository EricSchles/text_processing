from text_processing_ml.normalization import NormalizeText

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

def test_correct_spelling_simple():
    norm = NormalizeText()
    norm.initialize_spellchecker()
    assert norm.make_spelling_correction("there") == "there"

def test_add_stopwords():
    norm = NormalizeText()
    norm.add_to_stopwords(words=["goat", "bob", "phil"])
    assert "goat" in norm.stopwords
    assert "bob" in norm.stopwords
    assert "phil" in norm.stopwords

def test_stopwords():
    norm = NormalizeText()
    assert norm.remove_stopwords("the friends play a ball game") == "friends play ball game"

def test_initialize_spellchecker_with_corpus():
    norm = NormalizeText()
    try:
        norm.initialize_spellchecker()
        assert True
    except:
        assert False

def test_spelled_correctly():
    norm = NormalizeText()
    try:
        norm.initialize_spellchecker(words=["the"])
        assert norm.spell_checker.spell_checker.known(["the"])
        assert norm.correctly_spelled("the")
    except:
        assert False
