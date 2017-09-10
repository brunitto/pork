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
        pass

    def teardown(self):
        """
        Teardown function.
        """
        pass

    def test_tokenize(self):
        """
        Tokenize test function.
        """
        parser = Parser()

        user_input = "GET THE KEY"
        tokens = parser.tokenize(user_input)
        assert_equal(tokens[0], "GET")
        assert_equal(tokens[1], "THE")
        assert_equal(tokens[2], "KEY")

    def test_clean(self):
        """
        Clean test function.
        """
        parser = Parser()

        user_input = "GET THE KEY"
        tokens = parser.tokenize(user_input)
        clean_tokens = parser.clean(tokens)
        assert_equal(clean_tokens[0], "GET")
        assert_equal(clean_tokens[1], "KEY")

    def test_handle(self):
        """
        Handle test function.
        """
        parser = Parser()

        user_input = "GET THE KEY"
        handled_input = parser.handle(user_input)
        assert_equal(handled_input.action, "GET")
        assert_equal(handled_input.object, "KEY")

        user_input = "LOOK THROUGH THE WINDOW"
        handled_input = parser.handle(user_input)
        assert_equal(handled_input.action, "LOOK")
        assert_equal(handled_input.object, "WINDOW")

        user_input = "SLEEP"
        handled_input = parser.handle(user_input)
        assert_equal(handled_input.action, "SLEEP")
        assert_equal(handled_input.object, None)

        user_input = "OPEN THE RED DOOR USING THE BLUE KEY"
        handled_input = parser.handle(user_input)
        assert_equal(handled_input.action, "OPEN")
        assert_equal(handled_input.object, "RED")
