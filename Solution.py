import matplotlib.pyplot as plt
import numpy as np


m = np.sqrt(2/3)
n = np.sqrt(3/2)


def solutions_1(t):
    sol = n*np.sin(m*t) - n*np.cos(m*t)
    return sol


def solutions_2(t):
    sol = n*np.sin(m*t) - n*np.cos(m*t)
    return sol


def solutions_3(t):
    sol = np.cos(m*t) + np.sin(m*t)
    return sol

def solutions_4(t):
    sol = np.cos(m*t) + np.sin(m*t)
    return sol


x_vals = np.linspace(0, 3*np.pi, 500)


plt.title(r'Solution Plot for $\vec{u}^{(1)}(t)$')

plt.plot(x_vals, solutions_1(x_vals), label=r'$u_1(t) = u_2(t)$')
plt.plot(x_vals, solutions_3(x_vals), label=r'$u_3(t) = u_4(t)$')

plt.legend()

plt.xlabel("t")
plt.ylabel(r'$\vec{u}^{(1)}(t)$')
# plt.savefig('Part_c_solution for m_2 and n_2.png')
plt.show()

