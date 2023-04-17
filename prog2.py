import numpy as np
import matplotlib.pyplot as plt

# создаем переменные
x0 = 1
v0 = 0
omega = 2

t = np.linspace(0, 10, 100)
x = x0 * np.cos(omega * t) + v0 / omega * np.sin(omega * t)
y = np.random.normal(0, 1, len(t))
z = x + y

fig, axs = plt.subplots(3, sharex=True)
fig.suptitle('Гармонический осцилятор с шумом')
axs[0].plot(t, x)
axs[0].set(ylabel='Отклонение, м')
axs[1].plot(t, y)
axs[1].set(ylabel='Шум')
axs[2].plot(t, z)
axs[2].set(xlabel='Время, с', ylabel='Отклонение с шумом, м')
plt.show()
