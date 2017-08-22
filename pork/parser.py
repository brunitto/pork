"""
parser module.
"""

class Parser(object):
    """
    Parser class.
    """

    def __init__(self):
        """
        Initialization function.
        """
        self.lexicon = [
            ("verb", "hit"),
            ("verb", "call"),
            ("verb", "yell"),
            ("noun", "uncle"),
            ("noun", "otto"),
            ("noun", "hammer"),
            ("noun", "funny"),
            ("noun", "farm"),
            ("stop", "the"),
            ("stop", "in"),
            ("stop", "with"),
        ]

    def tokenize(self, user_input):
        """
        Tokenize function.
        """
        return user_input.split(" ")

    def parse(self, user_input):
        """
        Parse function.
        """
        result = []
        words = self.tokenize(user_input)
        for word in words:
            for item in self.lexicon:
                if word == item[1]:
                    result.append(item)
                    break
            else:
                result.append(("error", word))
        return result
