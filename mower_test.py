from mower import Mower
from orientation import Orientation


def test_mower_str():
    m = Mower(10, 20, Orientation.NORTH, [])
    assert str(m) == '10 20 N'
