"""
room module.
"""

class Room(object):
    """
    Room class.
    """
    def __init__(self, p_name, p_desc, p_bits=None):
        """
        Init function.
        """
        self.name = p_name
        self.desc = p_desc
        self.bits = p_bits

class RoomExit(object):
    """
    Room exit class.
    """
    def __init__(self, p_exit, p_room, p_when=None):
        """
        Initialization function.
        """
        self.exit = p_exit
        self.room = p_room
        self.when = p_when

class RoomRoutine(object):
    """
    Room routine class.
    """
    def __init__(self, p_action, p_object=None, p_engine=None, p_when=None):
        """
        Initialization function.
        """
        self.action = p_action
        self.object = p_object
        self.engine = p_engine
        self.when = p_when
