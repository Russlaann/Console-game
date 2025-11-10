import random
import utils


class Cloud:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.sky = self.create_initial_sky()


    def create_initial_sky(self):                   # 0 - нет облака, 1 - есть облако, 2 - молния
        sky = [[0 for _ in range(self.x)] for _ in range(self.y)]
        for i in range(self.y):
            for j in range(self.x):
                cell = random.randint(0, 100)
                if cell < 95:
                    sky[i][j] = 0
                else:
                    sky[i][j] = 1

        return sky


    def gen_clouds(self):                                  # формирует в столбце 0 случайные облака
        for i in self.sky:                                 # удаляем последний столбец
            i.pop()
            cell = random.randint(0, 100)
            if cell < 95:
                i.insert(0, 0)
            else:
                i.insert(0, 1)


        return self.sky                                     # возвращаем матрицу неба







