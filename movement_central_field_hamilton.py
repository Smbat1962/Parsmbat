import numpy as np
from scipy. integrate import odeint
import matplotlib.pyplot as plt


m = 37
alfa = -25
def f(y, t):
	x, px, y, py = y
	return [px/m, alfa*x*np.sqrt((x**(2) + y**(2)))**(-3), py/m, alfa*y*(x**(2) + y**(2))**(-3/2)]

t = np.linspace( 0, 200, 5000) 
y0 = [1, 3, 7, 5] 
w = odeint(f, y0, t) 
x = w[:,0]
px = w[:,1]
y = w[:,2]
py = w[:,3]
fig = plt.figure(facecolor='white')
plt.plot(t, x, t, y, linewidth=2)
plt.ylabel("x y")
plt.xlabel("t")
plt.grid(True)
plt.show()

fig2 = plt.figure(facecolor='white')
plt.plot(x, y, linewidth=2)
plt.ylabel("y")
plt.xlabel("x")
plt.grid(True)
plt.show()

fig3 = plt.figure(facecolor='white')
plt.plot(t, px, t, py, linewidth=2)
plt.ylabel("px py")
plt.xlabel("t")
plt.grid(True)
plt.show()
