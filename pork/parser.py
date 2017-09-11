"""
parser module.
"""

import string

class ParserException(Exception):
    """
    Parser exception class.
    """
    pass

class HandledInput(object):
    """
    Handled input class.
    """

    def __init__(self, p_action, p_object=None):
        """
        Initialization function.
        """
        self.action = p_action
        self.object = p_object

class Parser(object):
    """
    Parser class.
    """

    def __init__(self):
        """
        Initialization function.
        """
        self.stops = ["THE", "THROUGH"]

    def tokenize(self, p_user_input):
        """
        Tokenize function.
        """
        # Split the user input by spaces and return
        return p_user_input.split(" ")

    def clean(self, p_tokens):
        """
        Clean function.
        """
        # For each stop word, try to remove it from tokens
        for stop in self.stops:
            try:
                p_tokens.remove(stop)
            except ValueError:
                continue

        return p_tokens

    def handle(self, p_user_input):
        """
        Handle function.
        """
        tokens = self.clean(self.tokenize(p_user_input))

        # If there are two or more tokens, assume that the first is the action
        # and the second is the object
        if len(tokens) >= 2:
            p_action = tokens[0]
            p_object = tokens[1]
        # If there are only one token, assume that is the action
        elif len(tokens) == 1:
            p_action = tokens[0]
            p_object = None
        # Raise an exception otherwise
        else:
            raise ParserException("INVALID INPUT.")

        # Return a custom object containing the action and object
        return HandledInput(p_action=p_action, p_object=p_object)
