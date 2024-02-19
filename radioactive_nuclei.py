import numpy as np

def number_radioactive_nuclei(N0, a1, a2, a3, t):
    N1 = N0 * np.exp(-a1 * t)
    N2 = N0 * (np.exp(-a1 * t) - np.exp(-a2 * t)) * a1/(a2 - a1)
    N3 = N0 * a1 * a2 * (np.exp(-a1 * t)/(a2 - a1)*(a3 - a1) + np.exp(-a2 * t)/(a1 - a2)*(a3 - a2) + np.exp(-a3 * t)/(a1 - a3)*(a2 - a3))
    print(N1, " ", N2, " ", N3)
   
t = [10, 10**2, 10**3, 10**4, 10**5, 10**6, 10**7, 10**8, 10**9, 10**10, 10**11, 10**12, 10**13, 10**14]
for i in t:
    number_radioactive_nuclei(10**23, 2*10**(-6), 10**(-8), 10**(-11), i)

