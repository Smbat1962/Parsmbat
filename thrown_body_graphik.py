import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
n = int(input("input quantity experiments = "))
a = []
for i in range(n):
    a += [int(input("input initial angle = "))] 
v = []
for i in range(n):
    v += [int(input("input initial speed = "))] 
g = 9.8
xmax =  2 * np.cos(np.radians(a)) * np.sin(np.radians(a)) * v*v/g
ymax = (v * np.sin(np.radians(a)))**(2)/(2 * g)
x = np.linspace(0, xmax , 100) 
y = x * np.tan(np.radians(a)) - (g * x**(2))/(2*(np.cos(np.radians(a))*v)**(2))
print("X(max) = ",xmax," Y(max) =",ymax)
ax.set_title('Graph function')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.plot(x, y)
plt.grid(True)
plt.show()
