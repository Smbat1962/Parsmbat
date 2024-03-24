import numpy as np
from scipy. integrate import odeint
import matplotlib.pyplot as plt



g = 9.8
l = 9
px0 = 2
tmax = px0/g
print(tmax)
def f(y, t):
	x, px, y, py = y
	return [px, 0, py, g]

t = np.linspace( 0, tmax, 100) 
y0 = [0, px0, -l, 0] 
w = odeint(f, y0, t)
x = w[:,0]
px = w[:,1]
y = w[:,2]
py = w[:,3]
y01 = [0, -px0, -l, 0] 
w1 = odeint(f, y01, t)
x1 = w1[:,0]
px1 = w1[:,1]
y1 = w1[:,2]
py1 = w1[:,3]
fig = plt.figure(facecolor='white')
plt.plot(t, x, t, y, t, x1, t, y1, linewidth=2)
plt.ylabel("y--x--y1--x1")
plt.xlabel("t")
plt.grid(True)
plt.show()

fig2 = plt.figure(facecolor='white')
plt.plot(x, y, x1, y1, linewidth=2)
plt.ylabel(" y--y1")
plt.xlabel("x--x1")
plt.grid(True)
plt.show()

fig3 = plt.figure(facecolor='white')
plt.plot(t, px, t, py, t, px1, t, py1, linewidth=2)
plt.ylabel("px--py--px1--py1")
plt.xlabel("t")
plt.grid(True)
plt.show()



def f(y, t):
	fi, pf = y
	return [pf, -g*np.sin(fi)/l]

print(np.sin(np.pi/6))
t = np.linspace( 0, np.pi*np.sqrt(l/g), 100) 
y0 = [np.pi/12, 0] 
w = odeint(f, y0, t)
fi = w[:,0]
pf = w[:,1]
fig = plt.figure(facecolor='white')
plt.plot(t, fi, t, pf, linewidth=2)
plt.ylabel("fi pf")
plt.xlabel("t")
plt.grid(True)
plt.show()

x = l*np.sin(fi)
y = -l*np.cos(fi)
fig1 = plt.figure(facecolor='white')
plt.plot(x, y, linewidth=2)
plt.ylabel("y")
plt.xlabel("x")
plt.grid(True)
plt.show()