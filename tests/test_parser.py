"""
test_parser module.
"""

from nose.tools import assert_equal
from pork.parser import Parser

class TestParser(object):
    """
    TestParser class.
    """

    def setup(self):
        """
        Setup function.
        """
        self.parser = Parser()

    def teardown(self):
        """
        Teardown function.
        """
        self.parser = None

    def test_tokenize(self):
        """
        Tokenize test function.
        """
        user_input = "hit the uncle otto with the hammer"
        tokens = self.parser.tokenize(user_input)
        assert_equal(tokens[0], "hit")
        assert_equal(tokens[1], "the")
        assert_equal(tokens[2], "uncle")
        assert_equal(tokens[3], "otto")
        assert_equal(tokens[4], "with")
        assert_equal(tokens[5], "the")
        assert_equal(tokens[6], "hammer")

    def test_parse(self):
        """
        Parse test function.
        """
        user_input = "hit the uncle otto with the hammer"
        parsed_input = self.parser.parse(user_input)
        assert_equal(parsed_input, [
            ("verb", "hit"),
            ("stop", "the"),
            ("noun", "uncle"),
            ("noun", "otto"),
            ("stop", "with"),
            ("stop", "the"),
            ("noun", "hammer"),
        ])
