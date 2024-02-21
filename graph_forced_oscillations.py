import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

#dx^2/dt^2 + 2*v*dx/dt + w^2*x = (f/m)*cos(c*t)
w = 20
v = 0.3
f = 0.4
m = 1 
c = 5


def z_derivatives(x, t):
    return [x[1], (-2*v*x[1] - x[0]*w**2  + (f/m)*np.cos(c*t))]

time = np.arange(0, 10, 1e-3)
position, velocity = odeint(z_derivatives, [2e-3, 0], time).T   
plt.plot(time, position*100, 'orange', linewidth = 2)
plt.xlabel('time (s)')
plt.ylabel('position (cm)')
plt.ticklabel_format(style='sci', axis='x', scilimits=(0,0))
plt.grid(True)
plt.show()