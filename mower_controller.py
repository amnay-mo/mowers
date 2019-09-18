class MowerController:
    def __init__(self, lawn, mowers):
        self.lawn = lawn
        self.mowers = mowers
        for m in self.mowers:
            self.lawn.insert(m)

    def run(self):
        for m in self.mowers:
            m.run_actions()
        return self.mowers
