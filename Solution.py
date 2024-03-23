import matplotlib.pyplot as plt
import numpy as np


m = np.sqrt(2/3)
n = np.sqrt(3/2)

def solutions_1(t):
    sol = -3*np.sin(2*t) + 3*np.cos(2*t)
    return sol


def solutions_2(t):
    sol = 2*np.sin(2*t) - 2 * np.cos(2*t)
    return sol


def solutions_3(t):
    sol = -6*np.cos(2*t) - 6*np.sin(2*t)
    return sol

def solutions_4(t):
    sol = 4*np.cos(2*t) + 4*np.sin(2*t)
    return sol


x_vals = np.linspace(0, 3*np.pi, 500)


plt.title(r'Solution Plot for $\vec{u}^{(2)}(t)$')

plt.plot(x_vals, solutions_1(x_vals), label=r'$u_1(t)$')
plt.plot(x_vals, solutions_2(x_vals), label=r'$u_2(t)$')
plt.plot(x_vals, solutions_3(x_vals), label=r'$u_3(t)$')
plt.plot(x_vals, solutions_4(x_vals), label=r'$u_4(t)$')

plt.legend()

plt.xlabel("t")
plt.ylabel(r'$\vec{u}^{(1)}(t)$')
plt.savefig('Part_c_solution for m_2 and n_2.png')
plt.show()

