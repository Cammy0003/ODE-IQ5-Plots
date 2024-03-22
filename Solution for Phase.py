import matplotlib.pyplot as plt
import numpy as np


def solutions_u1(t, co):
    sol = co[0] * np.cos(2*t) + co[1] * np.sin(2*t) + co[2] * np.cos(np.sqrt(2/3) * t) + co[3] * np.sin(np.sqrt(2/3) * t)
    return sol


def solutions_v1(t, co):
    sol = co[0] * (-2)*np.sin(2*t) + co[1] * 2*np.cos(2*t) - co[2] * np.sqrt(2/3) * np.sin(np.sqrt(2/3) * t) + co[3] * np.sqrt(2/3) * np.cos(np.sqrt(2/3) * t)
    return sol


co = [1, 1, 1, 1]  # c = 1
t_vals = np.linspace(-5, 5, 500)
x_vals = solutions_u1(t_vals, co)
y_vals = solutions_v1(t_vals, co)
plt.plot(x_vals, y_vals, label=r'Solution curve ($C_n = 1$)')

co = [1, 2, 3, 4]  # c = 1, 2, 3, 4
t_vals = np.linspace(-5, 5, 500)
x_vals = solutions_u1(t_vals, co)
y_vals = solutions_v1(t_vals, co)
plt.plot(x_vals, y_vals, label=r'Solution curve ($C_n = 1$)')

co = [3, 3, 1, 2]  # c = 3, 3, 1, 2
t_vals = np.linspace(-5, 5, 500)
x_vals = solutions_u1(t_vals, co)
y_vals = solutions_v1(t_vals, co)
plt.plot(x_vals, y_vals, label=r'Solution curve ($C_n = 1$)')

plt.title(r'Solutions Plot in $u_1, u_3$ plane')

plt.plot(x_vals, y_vals, label=r'Solution curve ($C_n = 1$)')


plt.legend()

plt.xlabel(r'$u_1$')
plt.ylabel(r'$u_3$')
plt.show()
