import numpy as np
from scipy. integrate import odeint
import matplotlib.pyplot as plt

 # create function
def dydt(y, t):
	return 2*np.cos(t) + np.sin(t)

t = np.arange( 0, 4*np.pi, 10**(-1)) # vector of time
y0 = 0 # start value
y = odeint (dydt, y0, t) # solve eq.
y = np.array(y).flatten()
y2 = []
for i in y:
    y2 += [[i**(2)]]    
plt.plot( t, y, t, y2) # graphic
plt.grid(True)
plt.show() # display

import sympy as sp

# Определяем переменные
t = sp.symbols('t')
y = sp.Function('y')

# Определяем уравнение
equation = sp.Eq(y(t).diff(t), 2*sp.cos(t) + sp.sin(t))

# Решаем уравнение
solution = sp.dsolve(equation)

print(solution)
