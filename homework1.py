# Задание 1
# Создай гистограмму для случайных данных,
# сгенерированных с помощью функции `numpy.random.normal`.

import numpy as np
import matplotlib.pyplot as plt

# Параметры нормального распределения
mean = 0       # Среднее значение
std_dev = 1    # Стандартное отклонение
num_samples = 1000  # Количество образцов

# Генерация случайных чисел, распределенных по нормальному распределению
data = np.random.normal(mean, std_dev, num_samples)

# Создание гистограммы
plt.figure(figsize=(8, 6))
plt.hist(data, bins=30, density=True, edgecolor='black')

# Добавление заголовка и меток осей
plt.title('Гистограмма случайных данных, распределенных по нормальному распределению')
plt.xlabel('Значение')
plt.ylabel('Плотность вероятности')

# Отображение гистограммы
plt.show()
