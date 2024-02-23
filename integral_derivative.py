import sympy as sym

x, m, E, k = sym.symbols('x m E k')
m = 0.2
k = 0.1
E = 0.03
t = 1/(sym.sqrt(E - (k/2) * x**2))*sym.sqrt(2 * m)
integral1 = sym.integrate(t, (x, -sym.sqrt(2 * E/k), +sym.sqrt(2 * E/k)))
print('indefinite integral of: ', integral1)

t = 1/(sym.sqrt(1 -  x**2))
integral2 = sym.integrate(t, (x))
print('indefinite integral of: ', integral2)

derivative1_x = sym.diff(integral2, x)
print('derivative w.r.t x: ',derivative1_x)