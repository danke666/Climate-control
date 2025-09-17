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
