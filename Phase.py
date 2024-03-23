import numpy as np
import matplotlib.pyplot as plt



# Setting the grid for visualization
u1, u3 = np.meshgrid(np.linspace(-5, 5, 20), np.linspace(-5, 5, 20))
u2, u4 = np.meshgrid(np.linspace(-5, 5, 20), np.linspace(-5, 5, 20))

# Calculating the derivatives for the u1, u3 plane with u2 = 0
du1_dt = u3
du3_dt = -8/3*u1 + 2*0  # Simplification: Setting u2 = 0

# Calculating the derivatives for the u2, u4 plane with u1 = 0
du2_dt = u4
du4_dt = 4/3*0 - 2*u2  # Simplification: Setting u1 = 0

# Normalizing vectors for better visualization
norm1 = np.sqrt(du1_dt**2 + du3_dt**2)
norm2 = np.sqrt(du2_dt**2 + du4_dt**2)
du1_dt_norm, du3_dt_norm = du1_dt / norm1, du3_dt / norm1
du2_dt_norm, du4_dt_norm = du2_dt / norm2, du4_dt / norm2

# Plotting the slope fields
fig, axs = plt.subplots(1, 2, figsize=(14, 6))

# u1, u3 slope field
axs[0].quiver(u1, u3, du1_dt_norm, du3_dt_norm, norm1)
axs[0].set_title('Phase Portrait in the $u_1, v_1$ plane')
axs[0].set_xlabel('$u_1$')
axs[0].set_ylabel('$v_1$')
axs[0].axis('equal')

# u2, u4 slope field
axs[1].quiver(u2, u4, du2_dt_norm, du4_dt_norm, norm2)
axs[1].set_title('Phase Portrait in the $u_2, v_2$ plane')
axs[1].set_xlabel('$u_2$')
axs[1].set_ylabel('$v_2$')
axs[1].axis('equal')

plt.tight_layout()
plt.savefig('Part c Phase Portraits')
plt.show()





