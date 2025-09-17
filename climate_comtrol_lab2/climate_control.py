import time
import random


# Ф-ция климат-контроля для одного дня
def climate_control(day, t):
    print(f"{day}: Исходная температура {t}°С")

    # Определение интервала коррекции на основе отклонения
    # Середина диапозона - 21°С
    deviation = abs(t - 21)
    if deviation > 3:
        interval = 0.5  # 30 минут (в часах)
        print("Значительное отклонение! Интервал корреции: 30 минут")
    else:
        interval = 1  # 1 час
        print("Интервал коррекции: 1 час")

    # Иммитация ожидания интервала (для теста: 1 секунда = 1 час)
    time.sleep(interval)  # Симуляция: sleep в секундах вместо часов

    corrected_t = t
    action = " "
    while corrected_t < 20 or corrected_t > 22:
        if corrected_t < 20:
            corr = random.randint(2, 3)  # Случайная коррекция 2-3°С
            corrected_t += corr
            action += f"обогрев на {corr}°С; "
        elif corrected_t > 22:
            corr = random.randint(2, 3)
            corrected_t -= corr
            action += f"охлаждение на {corr}°С; "

        print(f"{day}: {action.strip('; ')} -> {corrected_t}°С")

        # Иммитация задержки 15-20 минут для повтороной проверки
        # В тесте 0.25-0.33 секунды
        check_delay = random.uniform(15, 20) / 60  # В часах
        time.sleep(
            check_delay * 60 / 60
        )  # Симуляция в секундах (упрощено до 0.25 секунд)
        print(
            f"{day}: Проверка через 15-20 минут... Текущая температура: {corrected_t}°С"
        )

    if action == "":
        print(f"{day}: Температура в норме, коррекция не нужна.")

    return corrected_t, action.strip("; ") if action else "Нет"
