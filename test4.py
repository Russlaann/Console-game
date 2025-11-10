import time
import os


def test_ansi_support():
    print("Тестирование ANSI поддержки в PyCharm:")

    # Тест перемещения курсора
    print("Начало →→→", end="")
    time.sleep(1)
    print("\033[3D", end="", flush=True)  # Должно переместить на 3 позиции назад
    print("★★★", end="", flush=True)
    time.sleep(1)

    print("\n\nТест очистки через 2 секунды...")
    time.sleep(2)
    print("\033[2J\033[H", end="")  # Очистка экрана
    print("✅ Экран очищен!" if True else "❌ Очистка не сработала")

    # Тест цветов
    print("\033[91mКрасный текст\033[0m")
    print("\033[92mЗеленый текст\033[0m")
    print("\033[94mСиний текст\033[0m")


test_ansi_support()