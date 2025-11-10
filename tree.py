import time

import utils


class Tree():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.timer = time.time()

    def time_cheсk(self):
        return time.time() - self.timer > 10  # Дерево горит более 10 секунд ?

    def coord_flame(self):
        return utils.rand(self.x, self.y)