from input_parser import InputParser
from orientation import Orientation
from io import StringIO


def test_can_parse_lawn_size():
    reader = StringIO('5 5\n1 2 N\nLFLFLFLFF\n3 3 E\nFFRFFRFRRF\n')
    parser = InputParser(reader)
    parser.parse()
    assert parser.lawn is not None
    assert len(parser.mowers) == 2
    assert parser.mowers[0].x == 1
    assert parser.mowers[0].y == 2
    assert parser.mowers[0].orientation == Orientation.NORTH
    assert parser.mowers[1].x == 3
    assert parser.mowers[1].y == 3
    assert parser.mowers[1].orientation == Orientation.EAST
