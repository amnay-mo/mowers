from orientation import Orientation

def test_rotating_left_from_south_returns_east():
    o = Orientation.SOUTH
    assert Orientation.rotate_left(o) == Orientation.EAST
