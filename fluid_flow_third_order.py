import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Pressure drop along a pipe with nonlinear friction
# P''' = -0.2P'' + 0.1P' - 0.05P
# P(0) = 10, P'(0) = 0, P''(0) = 0

# Reducing to 3 first order equations, since it's a third order 
# P' = u ; Equation 1
# P'' = u' = v ; Equation 2
# P''' = v' = w = -0.2P'' + 0.1P' - 0.05P ; Equation 3

# S is just a container holding both x and v variables together so the solver can handle them as one system

def dSdt (t, S):
    P, u, v = S
    return [u,
            v,
            -0.2*v + 0.1*u - 0.05*P]
S_0 = [10, 0, 0]    # Initial conditions for P(0) = 10, P'(0) = 0, P''(0) = 0

t = np.linspace(0, 5, 100)
sol2 = solve_ivp(dSdt, t_span=(0, max(t)), y0=S_0, t_eval=t)
print('P VALUES:', sol2.y[0])
print()  # empty line
print('u VALUES:', sol2.y[1])
print()  # empty line
print('v VALUES:', sol2.y[2])

# Plot showing the pressure drop along a pipe with nonlinear friction
plt.plot(sol2.t, sol2.y[0], label='P')
plt.plot(sol2.t, sol2.y[1], label='u')
plt.plot(sol2.t, sol2.y[2], label='v')
plt.ylabel('P, u, v')
plt.xlabel('TIme')
plt.title('Pressure Drop Profile')
plt.legend()
plt.show()