import itertools

class ParseText:
    def __init__(self, corpus=None):
        self.corpus = corpus

    def tfidf(self, text):
        # implement this:
        # https://www2.cs.duke.edu/courses/spring14/compsci290/assignments/lab02.html
        pass

    def generate_list_combinations_unordered(self, first: list, second: list):
        iterator = map(''.join,
                       itertools.chain(
                           itertools.product(first, second),
                           itertools.product(second, first)
                       ))
        return list(iterator)

    def generate_list_combinations_ordered(self, first: list, second: list):
        iterator = map(''.join, itertools.product(first, second))
        return list(iterator)

    def combine_lists(self, lists, ordered=True):
        if ordered:
            generate_list_combinations = self.generate_list_combinations_ordered
        else:
            generate_list_combinations = self.generate_list_combinations_unordered
        final_list = lists[0]
        num_lists = len(lists)
        for index in range(1, num_lists):
            final_list = generate_list_combinations(
                final_list,
                lists[index]
            )
        return final_list

    def match_lists(self, lists: list, text, ordered=True):
        """
        search a piece of text for all possible
        combinations of all tokens of a set of lists.
        Assumes tokens appear contigiously.

        Parameters
        ----------
        lists - a list of lists containing different tokens
        ordered [optional] - whether or not the tokens appear in 
        the order passed in, ordered assumes they do,
        unordered tries every possible combination.

        Output
        ------
        Returns all matching substrings
        """
        substrings = combine_lists(lists, ordered=ordered)
        text = "".join(text)
        found_substrings = []
        for substring in substrings:
            if substring in text:
                found_substrings.append(substring)
        return found_substrings

    # to do
    # add spell checker
    # add tfidf
    # add text summarization
    # add topic modeling, as well as topic assignment,
    # from a topic model
    # add build your own NER chuncker
    # add build your own POS tagger
    # add some embedding functionality
