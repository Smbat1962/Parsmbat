import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
ax.set_title('grafik number radioactive nuclei')
ax.set_xlabel('t')
ax.set_ylabel('N')
t = np.linspace(0, 10**4, 10**4) 
N0 = 10**13
a1 = 5*10**(-4)
a2 = 3*10**(-7)
a3 = 1.4*10**(-13)
N1 = N0 * np.exp(-a1 * t)
N2 = N0 * (np.exp(-a1 * t) - np.exp(-a2 * t)) * a1/(a2 - a1)
N3 = N0 * a1 * a2 * (np.exp(-a1 * t)/(a2 - a1)*(a3 - a1) + np.exp(-a2 * t)/(a1 - a2)*(a3 - a2) + np.exp(-a3 * t)/(a1 - a3)*(a2 - a3))
ax.plot(t, N1, t, N2)
ax.plot(t, N3)
plt.show()
