import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

#dx^2/dt^2 + (a + t^2) * x = 0
a = 23

def z_derivatives(x, t):
    return [x[1], (t**(2) - a) * x[0]]

time = np.arange(-np.sqrt(22), + np.sqrt(22), 1e-3)
position, velocity = odeint(z_derivatives, [1, 2], time).T   
position_sq = []
for i in position:
    position_sq += [[i**(2)]]
plt.plot(time, position, time, position_sq,'orange', linewidth = 2)
plt.xlabel('time (s)')
plt.ylabel('position (cm)')
plt.ticklabel_format(style='sci', axis='x', scilimits=(0,0))
plt.grid(True)
plt.show()
