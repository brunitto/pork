"""
test_room module.
"""

from nose.tools import assert_equal
from pork.room import Room
from pork.room import RoomExit
from pork.room import RoomRoutine

class TestRoom(object):
    """
    TestRoom class.
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

    def test_room_init(self):
        """
        Room init test function.
        """
        room = Room(p_name="DARK_ROOM", p_desc="This is a dark room, you can't see anything.")
        assert_equal(room.name, "DARK_ROOM")
        assert_equal(room.desc, "This is a dark room, you can't see anything.")
        assert_equal(room.bits, None)

        room = Room(p_name="DARK_ROOM", p_desc="This is a dark room, you can't see anything.", p_bits=["DARK"])
        assert_equal(room.name, "DARK_ROOM")
        assert_equal(room.desc, "This is a dark room, you can't see anything.")
        assert_equal(room.bits, ["DARK"])

    def test_room_exit_init(self):
        """
        Room exit init test function.
        """
        room_exit = RoomExit(p_exit="NORTH", p_room="DARK_CORRIDOR")
        assert_equal(room_exit.exit, "NORTH")
        assert_equal(room_exit.room, "DARK_CORRIDOR")
        assert_equal(room_exit.when, None)

        room_exit = RoomExit(p_exit="SOUTH", p_room="DARK_CELLAR", p_when="CELLAR_DOOR_IS_OPEN")
        assert_equal(room_exit.exit, "SOUTH")
        assert_equal(room_exit.room, "DARK_CELLAR")
        assert_equal(room_exit.when, "CELLAR_DOOR_IS_OPEN")

    def test_room_routine_init(self):
        """
        Room routine init test function.
        """
        room_routine = RoomRoutine(p_action="WAIT")
        assert_equal(room_routine.action, "WAIT")
        assert_equal(room_routine.object, None)
        assert_equal(room_routine.engine, None)
        assert_equal(room_routine.when, None)

        room_routine = RoomRoutine(p_action="USE", p_object="LANTERN")
        assert_equal(room_routine.action, "USE")
        assert_equal(room_routine.object, "LANTERN")
        assert_equal(room_routine.engine, None)
        assert_equal(room_routine.when, None)

        room_routine = RoomRoutine(p_action="USE", p_object="LANTERN", p_engine=[("TELL", "YOU USE THE LANTERN, THE ROOM BECOMES CLEAR")])
        assert_equal(room_routine.action, "USE")
        assert_equal(room_routine.object, "LANTERN")
        assert_equal(room_routine.engine, [("TELL", "YOU USE THE LANTERN, THE ROOM BECOMES CLEAR")])
        assert_equal(room_routine.when, None)

        room_routine = RoomRoutine(p_action="USE", p_object="LANTERN", p_engine=[("TELL", "YOU USE THE LANTERN, THE ROOM BECOMES CLEAR")], p_when="ROOM_IS_CLEAR")
        assert_equal(room_routine.action, "USE")
        assert_equal(room_routine.object, "LANTERN")
        assert_equal(room_routine.engine, [("TELL", "YOU USE THE LANTERN, THE ROOM BECOMES CLEAR")])
        assert_equal(room_routine.when, "ROOM_IS_CLEAR")
