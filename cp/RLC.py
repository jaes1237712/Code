from scipy.integrate import solve_ivp
import numpy as np
# I_ppp + (R/L)I_pp + (1/LC)I_p = 0
# I_pp + (R/L)I_p + (1/LC)I = 0
def f(t,vars,R,L,C):
    [I,I_p,I_pp] = vars
    return [I_p,I_pp, -(R/L)*I_pp - (1/(L*C))*I_p]

def current_on_circuit(R, L, C, I0):
    current = np.zeros(8)
    vars = [I0,0,-(1/(L*C))*I0] # I0,I0_p=0,I_pp
    ### START YOUR CODE HERE ###
    for i in range(8):
        sol = solve_ivp(f, [0,i+1],vars, atol=1E-12, rtol=1E-12, args={R,L,C})
        current[i] = sol.y[0,-1]
    #### END YOUR CODE HERE ####
    return current
