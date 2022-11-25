import math
import numpy as np 
from scipy.integrate import solve_ivp

Resistor, Capcity, Volt, Peroid = 0,0,0,0

def f(t,vars):
    [q,q_p] = vars  # in order of q,q_p
    q_prime = (Volt*np.exp(-t/Peroid))/Resistor - (q/(Resistor*Capcity))
    return [q_prime,0]


def charge_on_capacitor(R, C, V, T):
    charge = np.zeros(8)
    global Resistor, Capcity, Volt, Peroid
    [Resistor, Capcity, Volt, Peroid] = [R,C,V,T]
    vars = [0,0]
    ### START YOUR CODE HERE ###
    for i in range(8):
        sol = solve_ivp(f,[0,i+1],vars, atol=1E-12, rtol=1E-12)
        charge[i] = sol.y[0,-1]
    #### END YOUR CODE HERE ####
    return charge
print(charge_on_capacitor(176.29, 0.0191662, 3.13445, 1.97246))