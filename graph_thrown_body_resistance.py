import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

g = 9.8
lamda = int(input("Enter the air resistance coefficient lamda = "))
beta = int(input("Enter the air resistance coefficient beta = "))
x0 = int(input("Enter the starting coordinate  x0 = "))
y0 = int(input("Enter initial speed v0 = "))
alfa = int(input("Enter initial angle alfa = "))
tm = int(input("Enter researched time = "))
y1 = y0 * np.sin(np.radians(alfa))
y2 = y0 * np.cos(np.radians(alfa))

def z_derivatives(x, t):
    return [x[1], -g - lamda * x[1] - beta * x[1]**(2) * x[1]/abs(x[1])]

def z_derivatives1(x, t):
    return [x[1], - lamda * x[1]]

time = np.arange(0, tm, 1e-3)
position, velocity = odeint(z_derivatives, [x0, y1], time).T 
count = 0
for i in position:
    if i >= 0:
        count += 1
time1 = np.arange(0, count * 1e-3,1e-3)
position0, velocity = odeint(z_derivatives, [x0, y1], time1).T 
position1, velocity = odeint(z_derivatives1, [x0, y2], time1).T   
plt.plot(time1, position0, 'blue', linewidth = 2)
plt.plot(time1, position1, 'orange', linewidth = 2)
plt.xlabel('time (s)')
plt.ylabel('position (cm)')
plt.ticklabel_format(style='sci', axis='x', scilimits=(0,0))
plt.grid(True)
plt.show()

plt.plot(position1, position0, 'red', linewidth = 2)
plt.xlabel('x')
plt.ylabel('y')
plt.ticklabel_format(style='sci', axis='x', scilimits=(0,0))
plt.grid(True)
plt.show()

print(max(position0),max(position1))

