import math
import numpy as np
from scipy. integrate import odeint
import matplotlib.pyplot as plt
from sympy import solve
from sympy.abc import r

 
E = -1
M = 3
m = 4
alfa = - 3

ls = solve(-E + alfa/r + M**(2)/(2*m*r**(2)))
rmin = ls[0]
print(rmin)
rmax = ls[1]
print(rmax)
r = np.linspace( 0.3, 10, 100) 
pot = alfa/r + M**(2)/(2*m*r**(2))
ener = []
for i in r:
    ener += [E]
fig = plt.figure(facecolor='white')
plt.plot(r, pot, r, ener, linewidth=2)
plt.ylabel("pot and ener")
plt.xlabel("r")
plt.grid(True)
plt.show()


def f(y, t):
	r, fi = y
	return [(2*E/m - 2*alfa/(r*m) - (M/(m*r))**(2))**(1/2), (M/m)*r**(-2)]
stop = math.floor(-alfa*np.pi*np.sqrt(m/(2*abs(E)**(3)))/2)
t = np.linspace( 0, stop  , 1000) 
y0 = [rmin + 0.1, 0] 
w = odeint(f, y0, t) 
r = w[:,0]
fi = w[:,1]
fig = plt.figure(facecolor='white')
plt.plot(t, r, t, fi, linewidth=2)
plt.ylabel("r and fi")
plt.xlabel("t")
plt.grid(True)
plt.show()
print(r[-1])
print(fi[-1])

#fi = np.linspace( 0, 2*np.pi, 1000)
fig = plt.figure(facecolor='white')
plt.plot(fi, r, linewidth=2)
plt.ylabel("r")
plt.xlabel("fi")
plt.grid(True)
plt.show()

fig, ax = plt.subplots()
x = r*np.cos(fi)
y = r*np.sin(fi)
ax.plot(fi, x, fi, y )
plt.ylabel("x and y")
plt.xlabel("fi")
plt.grid(True)
plt.show()

fig2, ax = plt.subplots()
ax.plot(x, y )
plt.ylabel("y")
plt.xlabel("x")
plt.grid(True)
plt.show()
