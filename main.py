import msvcrt
import os
import time
import keyboard
import pickle


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
        'amount_current': lives_left,
        #'amount_begin': amount_begin,
        'volume': volume,
        'trees_saved': trees_saved,
        'trees_burned': trees_burned,
        'my_record': my_record,
        'map_size': (x, y)
    }

    with open('save.dat', 'wb') as f:
        pickle.dump(save_data, f)
    for i in range(101):
        print(f"\rСохраняем игру: [{('█' * (i // 2)):<50}] {i}%", end="", flush=True)
        time.sleep(0.03)


def load_game():
    global field, cloud, helic, tick, lives_left, amount_begin
    global volume, trees_saved, trees_burned, x, y, my_record
    with open('save.dat', 'rb') as f:
        load_data = pickle.load(f)

    # Восстанавливаем все объекты
    field = load_data['field']
    cloud = load_data['cloud']
    helic = load_data['helic']
    tick = load_data['tick']
    lives_left = load_data['amount_current']
    #amount_begin = load_data['amount_begin']
    volume = load_data['volume']
    trees_saved = load_data['trees_saved']
    trees_burned = load_data['trees_burned']
    my_record = load_data['my_record']
    x, y = load_data['map_size']
    for i in range(101):
        print(f"\rЗагружаем игру: [{('█' * (i // 2)):<50}] {i}%", end="", flush=True)
        time.sleep(0.03)
    time.sleep(1)
    return True

lives_left = 1
volume = 1
volume_max = 3
amount_of_water = 0
trees_saved = 0
trees_burned = 0
tick = 1
my_record = 0

os.system('cls')
story = ('Вы пилот пожарного вертолёта. Ваша работа - тушить возгарания участков леса. Забор воды в баки осущетсвляется автоматически после пролета над участком воды🟦\n'
         'Увеличение бака осуществляется на Базе🏠\n'
         'Дополнительные вертолеты можно приобрести за потушенные пожары в Аэропорту✈️.\n'
         'Не влетайте в облака☁️ - вы разобъёте вертолет.️\n\n'
         'Управление:\n'
         'Стрелки - движение\n'
         'P - пауза и меню\n'
         'S - сохранить игру\n'
         'L - загрузить игру\n'
         'Q- выход')
for i in story:
    print(i, end='', flush=True)
    if msvcrt.kbhit():
        while msvcrt.kbhit():
            msvcrt.getch()
        os.system('cls')
        print(story)
        break
    time.sleep(0.05)

print("\n" + "=" * 55)
print('🚁 Загрузить последнюю сохраненную игру? Нажмите Y/N')
print("=" * 55)
print('\033[?25l', end='', flush=True)
load = msvcrt.getch().decode('cp866').lower()
print('\033[?25h')  # Возвращаем курсор
if load.upper() in ['Y', 'Н']:  # Y или русская Н
   #for i in range(101):
   #    print(f"\rЗагружаю сохраненную игру: [{('█' * (i // 2)):<50}] {i}%", end="", flush=True)
   #    time.sleep(0.03)
    try:
        load_game()
    except:
        print('Загрузка не удалась. Возможно еще нет сохраненных игр')
        for i in range(101):
            print(f"\rЗапуск новой игры: [{('█' * (i // 2)):<50}] {i}%", end="", flush=True)
            time.sleep(0.03)
        print()  # Перенос строки в конце
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
    print(f'Статистика - I')
    print(f'Пауза. Правила игры - P')
    print(f'Сохранить игру - S')
    print(f'Загрузить последнюю сохраненную игру - L')


    print(f'Вертолетов осталось:  {lives_left}')
    print(f'Количество воды {amount_of_water}. Емкость бака: {volume} из {volume_max} тонн')
    print(f'Деревьев потушено: {trees_saved}  Деревьев сгорело: {field.trees_burned}')
    print(f'Рекорд {my_record} спасенных деревьев')
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
    elif keyboard.is_pressed('L') or keyboard.is_pressed('l'):
        load_game()
        time.sleep(2)
    elif keyboard.is_pressed('P') or keyboard.is_pressed('p'):
        while msvcrt.kbhit():  # удаляем символы из буфера, чтобы клавиша P не попадала в строку ввода меню
            msvcrt.getch()
        user_choice = 0
        os.system('cls')
        print("\n" + "=" * 40)
        print("    🚁🚁🚁 \033[36mПАУЗА. ПРАВИЛА ИГРЫ\033[0m 🚁🚁🚁")
        print("=" * 40)
        print()
        print('На Базе в этом меню 5 спасенных деревьев🌳 можно обменять на 1 дополнительную тонну объема бака для воды🛠️. Максимум емкость 3 тонны.')
        print('В Аэропорту✈️ в этом меню 5 спасенных деревьев🌳 можно обменять на 1 дополнительный вертолет🚁.')

        print()
        print("\033[32m1. Продолжить игру\033[0m")
        print("2. Загрузить игру")
        print("3. Сохранить игру")
        print("4. Выйти из игры\033[0m")
        if field.hel_x == 10 and field.hel_y == 10:
            print('5. Обменять 5 спасенных деревьев🌳 на 1 дополнительную тонну бака для воды🛠️')
        elif field.cell_under_hel == 7:
            print('5. Обменять 5 спасенных деревьев🌳 на 1 дополнительный вертолет 🚁')
        print("=" * 40)


        user_choice = int(input("Выберите действие [нажмите цифру]: "))
        if user_choice == 1:
            pass
        elif user_choice == 2:
            load_game()
        elif user_choice == 3:
            save_game()
        elif user_choice == 4:
            print('Игра завершена')
            break
        elif field.hel_x == 10 and field.hel_y == 10 and user_choice == 5:
            if trees_saved >= 5:
                if volume < 3:
                    trees_saved -= 5
                    volume += 1
                else:
                    os.system('cls')
                    print("\n" + "🟦" * 40)
                    print("\n        🛠️🛠️🛠️ \033[1;33mУ вас уже максимальная ёмкость бака - 3 тонны\033[0m 🛠️🛠️🛠️       \n")
                    print("🟦" * 40)
                    input()
            else:
                os.system('cls')
                print("\n" + "🟦" * 40)
                print(
                    "\n        🛠️🛠️🛠️ \033[1;33mНедостаточно спасенных деревьев\033[0m 🛠️🛠️🛠️       \n")
                print("🟦" * 40)
                input()

        elif field.cell_under_hel == 7 and user_choice == 5:
            if trees_saved >= 5:
                lives_left += 1
                trees_saved -= 5


    '''Блок проверки на столкновение с облаком'''
    if cloud.sky[field.hel_y][field.hel_x] == 1 and not(field.hel_x == 10 and field.hel_y == 10):
        print('Вертолет разбился в тумане!')
        lives_left -= 1
        amount_of_water = 0
        field.field[field.hel_y][field.hel_x] = field.cell_under_hel
        if lives_left > 0:
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


    '''Отрисовка экрана'''

    field.grow_tree()                               # рост нового дерева
    if tick % 20 == 0:
        field.gen_fire()
    field.check_fire()

    if tick % 20 == 0:
        gen_clouds(cloud)
    field.move_helicopter(dx, dy)                   # перемещение вертолета
    field.show_field(cloud)

    print('Для сохранения игры нажмите <S>  Для выхода нажмите <Q> или ESC')



    tick += 1
    time.sleep(.1)


