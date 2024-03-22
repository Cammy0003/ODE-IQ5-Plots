import matplotlib.pyplot as plt
import numpy as np


def solutions_1(t):
    sol = np.cos(2*t) + np.sin(2*t)
    return sol


def solutions_2(t):
    sol = -2*np.sin(2*t) + 2*np.cos(2*t)
    return sol


x_vals = np.linspace(0, 3*np.pi, 500)


plt.title(r'Solution Plot for $\vec{u}^{(1)}(t)$')

plt.plot(x_vals, solutions_1(x_vals), label=r'$u_1(t)$ and $u_2(t)$')

plt.plot(x_vals, solutions_2(x_vals), label=r'$u_3(t)$ and $u_4(t)$')

plt.legend()

plt.xlabel("t")
plt.ylabel(r'$\vec{u}^{(1)}(t)$')
plt.show()
