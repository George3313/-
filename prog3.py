import numpy as np
import matplotlib.pyplot as plt

# Задаём параметры модели
mass = 1  # Масса, кг
omega = np.sqrt(1 / mass)  # Частота собственных колебаний
gamma = 0.2 * omega  # Коэффициент затухания
u0, v0 = 1, 0  # Начальные условия - смещение и скорость
stop = 8  # Временной интервал для остановки колебаний

# Вычисляем значения на временном интервале [0, 50]
t = np.linspace(0, 50, 500)
u1 = np.exp(-gamma / (2 * mass) * t)
u2 = np.cos(omega * np.sqrt(1 - (gamma / (2 * mass * omega)) ** 2) * t)
u3 = np.sin(omega * np.sqrt(1 - (gamma / (2 * mass * omega)) ** 2) * t)
u = u1 * (u0 * u2 + (v0 + gamma / (2 * mass) * u0) * u3)

# Обрезаем значения после времени stop
mask = t <= stop
t_stop = t[mask]
u_stop = u[mask]

# Создаём график
fig, ax = plt.subplots()
ax.plot(t, u, label='Смещение')
ax.axvline(x=stop, color='r', linestyle='--', label='Остановка колебаний')
ax.set_xlabel('Время, с')
ax.set_ylabel('Смещение, м')
ax.set_title('Гармонический осциллятор с затуханием')
ax.legend()
plt.show()
