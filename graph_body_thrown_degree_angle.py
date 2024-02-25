import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
a = int(input("input initial angle = "))
g = 9.8
v = int(input("input initial speed = "))
xmax =  2 * np.cos(np.radians(a)) * np.sin(np.radians(a)) * v**(2)/g
ymax = (v * np.sin(np.radians(a)))**(2)/(2 * g)
x = np.linspace(0, xmax , 100) 
y = x * np.tan(np.radians(a)) - (g * x * x)/(2*np.cos(np.radians(a))*np.cos(np.radians(a))*v*v)
print("X(max) = ",xmax," Y(max) =",ymax)
ax.set_title('График функции')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.plot(x, y)
plt.show()
