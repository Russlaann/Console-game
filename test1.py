import time
for i in range(101):
    print(f'\r🔶 Процент загрузки ... {i} % 🟧🟨🟩🟦🟪🟫', end='')
    time.sleep(.01)

for i in range(101):
    print(f"\rПрогресс: [{('█' * (i//2)):<50}] {i}%", end="", flush=True)
    time.sleep(0.1)
print()  # Перенос строки в конце

spinner = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]

for i in range(50):
    frame = spinner[i % len(spinner)]
    print(f"\r{frame} Загрузка...", end="", flush=True)
    time.sleep(0.1)
print("\r✅ Готово!")

frames = [
    "🟥🟧🟨🟩🟦🟪",
    "🟧🟨🟩🟦🟪🟥",
    "🟨🟩🟦🟪🟥🟧",
    "🟩🟦🟪🟥🟧🟨"
]

try:
    while True:
        for frame in frames:
            print(f"\r{frame}", end="", flush=True)
            time.sleep(0.3)
except KeyboardInterrupt:
    print("\n🎉 Анимация остановлена")