import matplotlib.pyplot as plt
import numpy as np

m = np.sqrt(2/3)
n = np.sqrt(3/2)


def solutions_u1(t, co):
    sol = co[0] * -3 * np.sin(2*t) + co[1] * 3 * np.cos(2*t) + co[2] * n * np.sin(m*t) + co[3] * -n * np.cos(m*t)
    return sol


def solutions_v1(t, co):
    sol = co[0] * -6 * np.sin(2*t) + co[1] * 6 * np.sin(2*t) + co[2] * np.cos(m*t) + co[3] * np.sin(m*t)
    return sol


co = [3/10, -1/5, 4/5, -(8 * np.sqrt(6))/15]  # u(0)
t_vals = np.linspace(-5, 5, 500)
x_vals = solutions_u1(t_vals, co)
y_vals = solutions_v1(t_vals, co)
plt.plot(x_vals, y_vals, label=r'Solution curve ($\vec{u(0)}$)')


plt.title(r'Solutions Plot with ICs \vec{u(0)}')


plt.legend()

plt.xlabel(r'$u_1$')
plt.ylabel(r'$u_3$')
plt.show()
