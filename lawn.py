class LawnPositionError(ValueError):
    pass


class Lawn:
    def __init__(self, width, length):
        self.width, self.length = width, length
        self.occupied_positions = set()

    def insert(self, mower):
        mower.lawn = self
        self.occupy(mower.x, mower.y)

    def occupy(self, x, y):
        if x > self.width or y > self.length:
            raise LawnPositionError('mower position beyond lawn size')
        if (x, y) in self.occupied_positions:
            raise LawnPositionError('position is already occupied')
        self.occupied_positions.add((x, y))

    def _is_within_lawn(self, x, y):
        return x < self.width and y < self.length

    def _is_vacant(self, x, y):
        return (x, y) not in self.occupied_positions

    def can_occupy(self, x, y):
        return self._is_within_lawn(x, y) and self._is_vacant(x, y)

    def free(self, x, y):
        self.occupied_positions.remove((x, y))
