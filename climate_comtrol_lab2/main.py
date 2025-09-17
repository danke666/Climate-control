from date import temperatures
from climate_control import climate_control

# Тестирование на всех днях
results = {}
actions = {}
for day, t in temperatures.items():
    final_t, action = climate_control(day, t)
    results[day] = final_t
    actions[day] = action
    print("---")

# Вывод итоговой таблицы
print("\nИтоговая табилца:")
print(
    "| День          | Исходная t (°С) | Коррекция                  | Итоговая t (°С) |"
)
print(
    "|---------------|-----------------|----------------------------|-----------------|"
)
for day, initian_t in temperatures.items():
    final_t = results[day]
    action = actions[day]
    print(f"| {day:<13} | {initian_t:^15} | {action:<26} | {final_t:^15} |")
