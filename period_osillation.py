import math
import matplotlib.pyplot as plt 
import numpy as np 
import sympy as sy 
from sympy import symbols, Eq, solve


fig, ax = plt.subplots()
ax.set_title('grafik ')
ax.set_xlabel('x')
ax.set_ylabel('eq')
x = np.linspace(-10, 10, 10**2)
E = []
for i in x:
    E += [200]
#eq = 2*x**(2)
#eq = 5*x**(3)
#eq = -5*(np.tan(2*x))**(2)
eq = 3*x**(4)
ax.plot(x, eq, x, E)
plt.show()

x = symbols('x')
#eq = 2*x**(2)
#eq = 5*x**(3)
#eq = -5*(sy.tan(2*x))**(2)
eq = 3*x**(4)
E = 200
m = 2
def f(x):
    return E - eq

solution = solve(f(x), x)
print(solution)

if len(solution) <= 1: 
    T = float('inf')
    print(T) 
elif len(solution) >= 2:        
    a = solution[0]
    b = solution[1]  
    print(a, " ", b) 
    x = sy.Symbol("x") 
    def f(x):
        return 1/sy.sqrt(E - eq)
    sl = sy.integrate(f(x), (x, a, b))
    T = np.sqrt(2*m)*sl
    print(T)


