import random
import time
import os
import sys

def get_terminal_size():
    try:
        return os.get_terminal_size()
    except OSError:
        return type('Size', (), {'columns': 80, 'lines': 24})()

def random_char():
    return random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789$#@%&*")

def main():
    size = get_terminal_size()
    width = size.columns
    height = size.lines - 1

    # Для каждой колонки: список последних N позиций (хвост)
    trails = [[] for _ in range(width)]
    max_trail = 10  # длина хвоста

    try:
        while True:
            screen = [[' ' for _ in range(width)] for _ in range(height)]

            for x in range(width):
                # Иногда запускаем новую "струю"
                if not trails[x] or (len(trails[x]) < height and random.random() < 0.05):
                    trails[x].insert(0, 0)  # новая голова в строке 0

                # Обновляем все капли в этой колонке
                new_trail = []
                for y in trails[x]:
                    if y < height:
                        new_trail.append(y + 1)
                trails[x] = new_trail

                # Рисуем хвост: голова — яркая, хвост — тусклее
                for i, y in enumerate(trails[x]):
                    if y < height:
                        if i == 0:
                            # Голова — ярко-зелёная
                            screen[y][x] = f"\033[1;32m{random_char()}\033[0m"
                        else:
                            # Хвост — тусклый зелёный
                            screen[y][x] = f"\033[2;32m{random_char()}\033[0m"

            # Вывод
            sys.stdout.write("\033[H")
            for row in screen:
                sys.stdout.write(''.join(row) + '\n')
            sys.stdout.flush()

            time.sleep(0.5)

    except KeyboardInterrupt:
        sys.stdout.write("\033[?25h\033[0m\n")
        print("Система отключена.")

if __name__ == "__main__":
    sys.stdout.write("\033[?25l")  # скрыть курсор
    sys.stdout.flush()
    main()