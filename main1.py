import os
import time
import keyboard
import  pickle

from keyboard import record

from cloud import Cloud
from field import gen_clouds
from field import Field
from helicopt import Helic


def save_game():
    save_data = {
        'field': field,
        'cloud': cloud,
        'helic': helic,
        'tick': tick,
        'amount_current': amount_current,
        'amount_begin': amount_begin,
        'volume': volume,
        'trees_saved': trees_saved,
        'trees_burned': trees_burned,
        'map_size': (x, y)
    }

    with open('save.dat', 'wb') as f:
        pickle.dump(save_data, f)
    print("Игра сохранена")
    time.sleep(1)


def load_game():
    global field, cloud, helic, tick, amount_current, amount_begin
    global volume, trees_saved, trees_burned, x, y
    with open('save.dat', 'rb') as f:
        load_data = pickle.load(f)

    # Восстанавливаем все объекты
    field = load_data['field']
    cloud = load_data['cloud']
    helic = load_data['helic']
    tick = load_data['tick']
    amount_current = load_data['amount_current']
    amount_begin = load_data['amount_begin']
    volume = load_data['volume']
    trees_saved = load_data['trees_saved']
    trees_burned = load_data['trees_burned']
    x, y = load_data['map_size']
    print("Игра загружена")
    time.sleep(1)
    return True

amount_current = 1
amount_max = 3
volume = 1
volume_max = 3
amount_of_water = 0
trees_saved = 0
trees_burned = 0
tick = 1
my_record = 0

load = input('Загрузить последнюю сохраненную игру? Нажмите Y/N: ')
if load.upper() in ['Y', 'Н']:  # Y или русская Н
    load_game()
    print("Загрузка игры...")
else:
    x = 30
    y = 20
    field = Field(x, y)
    helic = Helic(15, 6)
    cloud = Cloud(x, y)
    for i in range(int(x * y)):
        field.gen_forest()
    for i in range(3):
        field.gen_water()
    for i in range(1):
        field.gen_fire()
    field.gen_ambulance()


while True:
    os.system('cls')
    print(f"Кадр: {tick}")
    print(f'Вертолетов осталось:  {amount_current} из {amount_max}')
    print(f'Количество воды {amount_of_water}. Емкость бака: {volume} из {volume_max} тонн')
    print(f'Деревьев потушено: {trees_saved}  Деревьев сгорело: {trees_burned}')
    print(f'Рекорд {my_record} спасенных деревьев')
    print('5 спасенных деревьев можно обменять на 1 дополнительный вертолет в Больнице')
    print('5 спасенных деревьев можно обменять 1 дополнительную тонну объема бака для воды')
    dx = dy = 0

    if keyboard.is_pressed('up'):
        dx, dy = 0, -1
    elif keyboard.is_pressed('down'):
        dx, dy = 0, 1
    elif keyboard.is_pressed('left'):
        dx, dy = -1, 0
    elif keyboard.is_pressed('right'):
        dx, dy = 1, 0
    elif keyboard.is_pressed('Q') or keyboard.is_pressed('q'):
        print('Игра завершена')
        break
    elif keyboard.is_pressed('S') or keyboard.is_pressed('s'):
        save_game()
        time.sleep(2)

    '''Блок проверки на столкновение с облаком'''
    if cloud.sky[field.hel_y][field.hel_x] == 1 and field.hel_x != 10 and field.hel_y != 10:
        print('Вертолет разбился в тумане!')
        amount_current -= 1
        amount_of_water = 0
        field.field[field.hel_y][field.hel_x] = field.cell_under_hel
        if amount_current > 0:
            field.hel_x = 10
            field.hel_y = 10
            field.cell_under_hel = field.field[field.hel_y][field.hel_x]
            field.field[field.hel_y][field.hel_x] = 2
            print('Новый вертолет на базе')
            time.sleep(2)
        else:
            print('Все вертолёты уничтожены')
            time.sleep(2)
            break

    '''Блок тушения пожара'''
    if field.cell_under_hel == 3 and amount_of_water > 0:
        field.cell_under_hel = 1
        trees_saved += 1
        amount_of_water -= 1
        my_record += 1
        print('Пожар потушен. Спасено 1 дерево')
        time.sleep(1)

    '''Блок забора воды'''
    if field.cell_under_hel == 4:
        amount_of_water = volume


    '''Больница. Покупка дополнительных вертолетов за деревья'''
    if field.cell_under_hel == 7 and amount_current < amount_max:
        amount_current += 1
        trees_saved -= 5

    '''Мастерская. Увеличение бака'''
    if field.cell_under_hel == 9 and volume < volume_max and trees_saved >= 5:
        volume += 1
        trees_saved -= 5


    '''Отрисовка экрана'''

    field.grow_tree()                               # рост нового дерева
    if tick % 20 == 0:
        field.gen_fire()
    field.check_fire()
    if tick % 20 == 0:
        gen_clouds(cloud)
    field.move_helicopter(dx, dy)                   # функция вертолета должна вызываться последней
    field.show_field(cloud)

    print('Для сохранения игры нажмите <S>  Для выхода нажмите <Q> или ESC')



    tick += 1
    time.sleep(.1)


