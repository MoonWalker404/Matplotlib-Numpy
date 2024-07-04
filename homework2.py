# Задание 2
# Построй диаграмму рассеяния для двух наборов случайных данных,
# сгенерированных с помощью функции `numpy.random.rand`.

import numpy as np
import matplotlib.pyplot as plt

# Генерация двух наборов случайных данных
x = np.random.rand(100)
y = np.random.rand(100)

# Построение диаграммы рассеяния
plt.figure(figsize=(8, 6))
plt.scatter(x, y, s=20, alpha=0.5)

# Добавление заголовка и меток осей
plt.title('Диаграмма рассеяния случайных данных')
plt.xlabel('X')
plt.ylabel('Y')

# Отображение диаграммы
plt.show()