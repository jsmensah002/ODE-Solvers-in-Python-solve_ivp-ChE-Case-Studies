import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# A CSTR reactor has a first order reaction. Find how concentration changes over time:
# dC/dt = -kC + F
# k = 0.5, F = 2, C(0) = 0

def dCdt(t, C):
    return [-0.5*C + 2]    # return as list for solve_ivp
C0 = [0]         # initial condition as list
t = np.linspace(0, 15, 1000)
sol1 = solve_ivp(dCdt, t_span=(0, max(t)), y0=C0, t_eval=t)
print('Concentration VALUES:', sol1.y[0])

# Plotting how concentration changes over time
plt.plot(t, sol1.y[0])    # .y[0] gets first variable
plt.ylabel('Concentration')
plt.xlabel('Time')
plt.title('Concentration Change Over Time')
plt.show()
