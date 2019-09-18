from orientation import Orientation
from mower_action import MowerAction


class Mower:
    def __init__(self, x, y, orientation, actions):
        self.x, self.y, self.orientation = x, y, orientation
        self.lawn = None
        self.actions = actions

    def run_actions(self):
        for action in self.actions:
            if action == MowerAction.FORWARD:
                self.move_forward()
            elif action == MowerAction.RIGHT:
                self.rotate_right()
            elif action == MowerAction.LEFT:
                self.rotate_left()

    def is_done(self):
        return len(self.actions) == 0

    def rotate_right(self):
        self.orientation = Orientation.rotate_right(self.orientation)

    def rotate_left(self):
        self.orientation = Orientation.rotate_left(self.orientation)

    def move_forward(self):
        if self.orientation == Orientation.NORTH:
            self.move_north()
        elif self.orientation == Orientation.SOUTH:
            self.move_south()
        elif self.orientation == Orientation.WEST:
            self.move_west()
        elif self.orientation == Orientation.EAST:
            self.move_east()

    def move_north(self):
        if self.lawn.can_occupy(self.x, self.y+1):
            self.lawn.free(self.x, self.y)
            self.lawn.occupy(self.x, self.y+1)
            self.y += 1

    def move_south(self):
        if self.lawn.can_occupy(self.x, self.y-1):
            self.lawn.free(self.x, self.y)
            self.lawn.occupy(self.x, self.y-1)
            self.y -= 1

    def move_west(self):
        if self.lawn.can_occupy(self.x-1, self.y):
            self.lawn.free(self.x, self.y)
            self.lawn.occupy(self.x-1, self.y)
            self.x -= 1

    def move_east(self):
        if self.lawn.can_occupy(self.x+1, self.y):
            self.lawn.free(self.x, self.y)
            self.lawn.occupy(self.x+1, self.y)
            self.x += 1

    def __str__(self):
        return f"{self.x} {self.y} {self.orientation}"
