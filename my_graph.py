import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
ax.set_title('График функции')
ax.set_xlabel('x')
ax.set_ylabel('y')
x = np.linspace(0, 1, 100) 
y1 = np.exp(x**2) + np.exp(-x**2)
y2 = x**2
y3 = np.sin(x)
ax.plot(x, y1, x, y2, x, y3)
plt.show()
x = np.linspace(0, 2, 100)

plt.figure()
plt.plot(x, x**2, x, np.exp(x), x, x**3)
plt.show()