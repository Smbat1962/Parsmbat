import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
a = (np.pi)/3
g = 9.8
v = 12
xmax =  2 * np.cos(a) * np.sin(a) * v**(2)/g
ymax = (v * np.sin(a))**(2)/(2 * g)
x = np.linspace(0, xmax , 100) 
y = x * np.tan(a) - (g * x * x)/(2*np.cos(a)*np.cos(a)*v*v)
print("X(max) = ",xmax," Y(max) =",ymax)
ax.set_title('График функции')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.plot(x, y)
plt.show()
