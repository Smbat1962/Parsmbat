import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

#dx^2/dt^2 + k0**(2) * x = 0
k0 = 2
k1 = 0.2
def z_derivatives(x, t):
    return [x[1], (k1**(2) * x[0])]

def z_derivatives1(x, t):
    return [x[1], (-k0**(2) * x[0])]

def z_derivatives2(x, t):
    return [x[1], (k1**(2) * x[0])]
    

time = np.arange(-4*np.pi, 0, 1e-2)
time1= np.arange(0, 4*np.pi, 1e-2)
time2= np.arange(4*np.pi, 8*np.pi, 1e-2)
position, velocity = odeint(z_derivatives, [0.1, k1*0.1], time).T   
position1, velocity = odeint(z_derivatives1, [position[-1], 4], time).T  
position2, velocity = odeint(z_derivatives2, [position1[-1], -k1*position1[-1]], time).T 
position_sq = []
for i in position:
    position_sq += [[i**(2)]]
position1_sq = []
for i in position1:
    position1_sq += [[i**(2)]]
position2_sq = []
for i in position2:
    position2_sq += [[i**(2)]]
plt.plot(time, position, time1, position1, time2, position2, 'orange', linewidth = 2)
plt.xlabel('time')
plt.ylabel('position')
plt.ticklabel_format(style='sci', axis='x', scilimits=(2,2))
plt.grid(True)
plt.show()
plt.plot(time, position_sq, time1, position1_sq, time2, position2_sq, 'orange', linewidth = 2)
plt.grid(True)
plt.show()
plt.plot(time, position, time1, position1, time2, position2, 'orange', linewidth = 2)
plt.plot(time, position_sq, time1, position1_sq, time2, position2_sq, 'orange', linewidth = 2)
plt.grid(True)
plt.show()