import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# A rod loses heat along its length. Show the temperature profile
# T'' = -0.3T' + 0.1T
# T(0) = 100, T'(0) = 0

# Reducing to 2 first order equations since it's a second order 
# T' = u ;  Equation 1
# T'' = u' = = -0.3T' - 0.1T;  Equation 2

# S is just a container holding both x and v variables together so the solver can handle them as one system.

def dSdt (t, S):
    T, u = S
    return [u,
            -0.3*u - 0.1*T]
S_0 = [100, 0]      # initial conditions for T and u(u = T')

t = np.linspace(0, 5, 100)
sol2 = solve_ivp(dSdt, t_span=(0, max(t)), y0=S_0, t_eval=t)
print('T VALUES:', sol2.y[0])
print()  # empty line
print('u VALUES:', sol2.y[1])

# Plot showing the temperature profile
plt.plot(sol2.t, sol2.y[0], label='T')
plt.plot(sol2.t, sol2.y[1], label='u')
plt.ylabel('T, u')
plt.xlabel('TIme')
plt.title('Temperature Profile')
plt.legend()
plt.show()