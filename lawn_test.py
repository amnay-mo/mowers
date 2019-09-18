from orientation import Orientation
from lawn import Lawn, LawnPositionError
from mower import Mower
from pytest import raises


def test_can_insert_mower():
    l = Lawn(10, 10)
    m = Mower(x=0, y=0, orientation=Orientation.NORTH, actions=[])
    l.insert(mower=m)


def test_inserting_in_occupied_position_raises_ValueError():
    l = Lawn(10, 10)
    m = Mower(x=0, y=0, orientation=Orientation.NORTH, actions=[])
    l.insert(mower=m)
    with raises(LawnPositionError):
        l.insert(mower=m)
