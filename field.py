import time

from firepoint import Fire
import utils


maps = {1: '🟩',
        2: '🚁',
        3: '🔥',
        4: '🟦',
        5: '🟫',
        6: '🏠',
        7: '🚑',
        8: '☁️',
        9: '🛠️',
        }


def gen_clouds(cloud):
    cloud.gen_clouds()

class Field:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.field = [[5 for _ in range(self.x)] for _ in range(self.y)]
        self.list_of_fire = []
        self.old_field = self.field
        self.hel_x = 10
        self.hel_y = 10
        self.cell_under_hel = 6
        self.field[10][10] = 6

    def gen_forest(self):                                   # количество вызовов функции вынести в main.py
        rnx, rny = utils.rand(self.x, self.y)
        self.field[rny][rnx] = 1

    def grow_tree(self):  # количество вызовов функции вынести в main.py
        rnx, rny = utils.rand(self.x, self.y)
        if self.field[rny][rnx] == 5:  # если клетка пуста (земля)
            self.field[rny][rnx] = 1

    def gen_water(self):                                    # количество вызовов функции вынести в main.py
        rnx, rny = utils.rand(self.x, self.y)
        self.field[rny][rnx] = 4
        for i in range(50):
            dx, dy = utils.rand_next()
            rnx, rny = rnx + dx, rny + dy
            if 0 < rnx < self.x and 0 < rny < self.y and self.field[rny][rnx] != 4:
                self.field[rny][rnx] = 4

    def gen_ambulance(self):
        rnx, rny = utils.rand(self.x, self.y)
        self.field[rny][rnx] = 7

    def gen_workshop(self):
        rnx, rny = utils.rand(self.x, self.y)
        self.field[rny][rnx] = 9

    def gen_fire(self):                                     # количество вызовов функции вынести в main.py
        x, y = utils.rand(self.x, self.y)
        if self.field[y][x] == 1:                           # если в клетке дерево
            fire = Fire(x, y)                               # создаем экземпляр огня по координатам клетки
            self.field[y][x] = 3                            # вносим огонь в матрицу поля
            self.list_of_fire.append(fire)                  # вносим экземпляр огня в список огней

    def check_fire(self):
        for fire in self.list_of_fire:
            if fire.time_check():                           # если дерево горит > 10 секунд
                x, y = fire.coord_flame()
                self.field[y][x] = 5                        # удаляем дерево с карты
                self.list_of_fire.remove(fire)              # удаляем огонь из списка

    def move_helicopter(self, dx, dy):
        if (dx != 0 or dy != 0) and 0 <= dy + self.hel_y < self.y and 0 <= dx + self.hel_x < self.x:
            self.field[self.hel_y][self.hel_x] = self.cell_under_hel
            self.hel_x += dx
            self.hel_y += dy
            self.cell_under_hel = self.field[self.hel_y][self.hel_x]
            self.field[self.hel_y][self.hel_x] = 2

    def show_field(self, cloud):
        print('🟨' * (self.x + 2))
        for i in range(self.y):
            print('🟨', end='')
            for j in range(self.x):
                if self.field[i][j] == 2:                 # Первый приоритет для вертолета
                    print('🚁', end='')
                elif cloud.sky[i][j] == 1:                # Второй приоритет для облаков
                    print('☁️️', end='')
                elif self.field[i][j] == 5:
                    print('🟫', end='')
                elif self.field[i][j] == 1:
                    print('🌳', end='')
                elif self.field[i][j] == 4:
                    print('🟦', end='')
                elif self.field[i][j] == 3:
                    print('🔥', end='')
                elif self.field[i][j] == 7:
                    print('🚑', end='')
                elif self.field[i][j] == 6:
                    print('🏠', end='')
            print('🟨', end='')
            print()
        print('🟨' * (self.x + 2))

