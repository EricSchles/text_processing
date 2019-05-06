from text_processing_ml.parsing import ParseText

def test_stemmer():
    parser = ParseText()
    try:
        parser.stem_tokens(["Hello", "there"])
        assert True
    except:
        assert False

def test_tokenize():
    parser = ParseText()
    assert len(parser.tokenize("Hello there")) == 2

def test_normalize_text():
    parser = ParseText()
    assert parser.normalize_text("HeLLo, there") == "hello there"

def test_tfidf():
    parser = ParseText()

    try:
        parser.tfidf(
            ["""text is in here and it is a good idea to understand that we are processing this text""",
             """there is text in here too and it is the kind of text that generates ideas but is also possible."""])
        assert True
    except:
        assert False
