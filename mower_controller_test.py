from mower_controller import MowerController
from mower import Mower
from lawn import Lawn
from orientation import Orientation
from mower_action import MowerAction


def test_mower_controller():
    m1 = Mower(
        1, 2, Orientation.NORTH,
        [
            MowerAction.LEFT,
            MowerAction.FORWARD,
            MowerAction.LEFT,
            MowerAction.FORWARD,
            MowerAction.LEFT,
            MowerAction.FORWARD,
            MowerAction.LEFT,
            MowerAction.FORWARD,
            MowerAction.FORWARD,
        ]
    )
    m2 = Mower(
        3, 3, Orientation.EAST,
        [
            MowerAction.FORWARD,
            MowerAction.FORWARD,
            MowerAction.RIGHT,
            MowerAction.FORWARD,
            MowerAction.FORWARD,
            MowerAction.RIGHT,
            MowerAction.FORWARD,
            MowerAction.RIGHT,
            MowerAction.RIGHT,
            MowerAction.FORWARD,
        ]
    )
    lawn = Lawn(6, 6)
    controller = MowerController(lawn, [m1, m2])
    controller.run()
    assert m1.x == 1
    assert m1.y == 3
    assert m1.orientation == Orientation.NORTH
    assert m2.x == 5
    assert m2.y == 1
    assert m2.orientation == Orientation.EAST
