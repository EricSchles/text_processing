from text_processing_ml.matching import MatchText

def test_generate_list_combinations_ordered():
    matcher = MatchText()
    assert matcher.generate_list_combinations_ordered(["he"], ["tr"]) == ["hetr"]

def test_combine_lists():
    matcher = MatchText()
    result = matcher.combine_lists([["he"], ["tr"]])
    result.sort()
    answer = ["hetr", "he"]
    answer.sort()
    assert result == answer

def test_match_lists():
    matcher = MatchText()
    result = matcher.match_lists([["he"], ["tr"]], "Hello there hetr", -1)
    result.sort()
    answer = ["hetr", "he"]
    answer.sort()
    assert result == answer
