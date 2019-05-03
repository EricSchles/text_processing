from text_processing.normalization import NormalizeText

def test_correct_whitespace():
    norm = NormalizeText(check_whitespace=True)
    norm.fit("Hello there friends")
    assert norm.transform() == "Hello there friends"

def test_case_normalization():
    norm = NormalizeText(norm_case=True)
    norm.fit("Hello there friends")
    assert norm.transform() == "hello there friends"

def test_initialize_spellchecker_simple():
    norm = NormalizeText(check_spelling=True)
    try:
        norm.initialize_spellchecker()
        assert True
    except:
        assert False
