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
        user_input = "HIT THE UNCLE OTTO WITH THE HAMMER"
        tokens = self.parser.tokenize(user_input)
        assert_equal(tokens[0], "HIT")
        assert_equal(tokens[1], "THE")
        assert_equal(tokens[2], "UNCLE")
        assert_equal(tokens[3], "OTTO")
        assert_equal(tokens[4], "WITH")
        assert_equal(tokens[5], "THE")
        assert_equal(tokens[6], "HAMMER")

    def test_parse(self):
        """
        Parse test function.
        """
        user_input = "HIT THE UNCLE OTTO WITH THE HAMMER"
        parsed_input = self.parser.parse(user_input)
        assert_equal(parsed_input["prsa"], "HIT")
        assert_equal(parsed_input["prso"], "UNCLE OTTO")
        assert_equal(parsed_input["prsi"], "HAMMER")
