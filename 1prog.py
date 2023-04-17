import numpy as np
import matplotlib.pyplot as plt

# создаем переменные
x0 = 1  # м
v0 = 0  # м/с
omega = 2  # рад/с

t = np.linspace(10, 20, 1000)  # с
x = x0 * np.cos(omega * t) + v0 / omega * np.sin(omega * t)

plt.plot(t, x)
plt.xlabel('Время, с')
plt.ylabel('Смещение, м')
plt.show()