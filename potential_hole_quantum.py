import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

E = 9
u0 = 15
l = 4.7
def u(x):
    if x < 0:
        return u0 
    elif x > l:
        return u0 
    else:
        return 0

def z_derivatives(y, x):
    return [y[1], (-E + u(x)) * y[0]]

time = np.arange(-0.5, 0, 1e-3)
position, velocity = odeint(z_derivatives, [0, 1], time).T   
time1 = np.arange(0, 4.7, 1e-3)
position1, velocity1 = odeint(z_derivatives, [position[-1], velocity[-1]], time1).T 
time2 = np.arange(4.7, 5.2, 1e-3)
position2, velocity2 = odeint(z_derivatives, [position1[-1], velocity1[-1]], time2).T 
position_sq = []
for i in position:
    position_sq += [[i**(2)]]
position_sq1 = []
for i in position1:
    position_sq1 += [[i**(2)]]
position_sq2 = []
for i in position2:
    position_sq2 += [[i**(2)]]
plt.plot(time, position, time1, position1, time2, position2, linewidth = 2)
plt.xlabel('x (cm)')
plt.ylabel('wave function')
plt.ticklabel_format(style='sci', axis='x', scilimits=(0,0))
plt.grid(True)
plt.show()

plt.plot(time, position_sq, time1, position_sq1, time2, position_sq2, linewidth = 2)
plt.xlabel('x (cm)')
plt.ylabel('probability')
plt.ticklabel_format(style='sci', axis='x', scilimits=(0,0))
plt.grid(True)
plt.show()
