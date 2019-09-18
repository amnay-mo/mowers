from enum import Enum


class Orientation(Enum):
    NORTH = 'N'
    SOUTH = 'S'
    WEST = 'W'
    EAST = 'E'

    @classmethod
    def rotate_left(cls, o):
        if o == cls.NORTH:
            return cls.WEST
        elif o == cls.WEST:
            return cls.SOUTH
        elif o == cls.SOUTH:
            return cls.EAST
        elif o == cls.EAST:
            return cls.NORTH

    @classmethod
    def rotate_right(cls, o):
        if o == cls.NORTH:
            return cls.EAST
        elif o == cls.EAST:
            return cls.SOUTH
        elif o == cls.SOUTH:
            return cls.WEST
        elif o == cls.WEST:
            return cls.NORTH

    def __str__(self):
        return self.value
