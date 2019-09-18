from lawn import Lawn
from mower_action import MowerAction
from orientation import Orientation
from mower import Mower


class InputParser:
    def __init__(self, input_reader):
        self.mowers = []
        self.lawn = None
        self.input_reader = input_reader

    def parse(self):
        self._parse_lawn()
        self._parse_mowers()
        return (self.lawn, self.mowers)

    def _parse_lawn(self):
        line = self.input_reader.readline().strip()
        lawn_values = line.split(' ')
        lawn_width, lawn_length = int(
            lawn_values[0]) + 1, int(lawn_values[1]) + 1
        self.lawn = Lawn(lawn_width, lawn_length)

    def _parse_mowers(self):
        for mower_line in self.input_reader:
            if mower_line == '':
                break
            mower_line_values = mower_line.strip().split(' ')
            mower_x, mower_y, mower_o = int(mower_line_values[0]), int(
                mower_line_values[1]), self._parse_orientation(mower_line_values[2])
            mower_actions_line = next(self.input_reader).strip()
            mower_actions = self._parse_actions(mower_actions_line)
            mower = Mower(mower_x, mower_y, mower_o, mower_actions)
            self.mowers.append(mower)

    @staticmethod
    def _parse_orientation(orientation_str):
        if orientation_str == 'N':
            return Orientation.NORTH
        if orientation_str == 'S':
            return Orientation.SOUTH
        if orientation_str == 'W':
            return Orientation.WEST
        if orientation_str == 'E':
            return Orientation.EAST
        else:
            raise ValueError(
                'invalid orientation token: {}'.format(orientation_str))

    @staticmethod
    def _parse_actions(actions_str):
        actions = []
        for c in actions_str:
            if c == 'F':
                actions.append(MowerAction.FORWARD)
            elif c == 'R':
                actions.append(MowerAction.RIGHT)
            elif c == 'L':
                actions.append(MowerAction.LEFT)
            else:
                raise ValueError('invalid action token: \'{}\''.format(c))
        return actions
