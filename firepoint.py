import time

import utils

class Fire:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.timer = time.time()


    def time_check(self):
        return time.time() - self.timer > 10   # Дерево горит более 10 секунд ?


    def coord_flame(self):
        return self.x, self.y