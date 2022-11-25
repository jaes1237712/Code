import numpy as np
from scipy.fftpack import fft
from scipy.integrate import solve_ivp

m = 1       #kg
L = 1       #m
h = 0.005   #s
g = 9.8     #m/s^2

def f(t,y):
    theta1, omega1, theta2, omega2 = y
    delta_theta = theta2 - theta1
    sin = np.sin(delta_theta)
    cos = np.cos(delta_theta)
    omega1_p = L*(omega1**2)*sin*cos + g*(np.sin(theta2))*cos + L*(omega2**2)*sin - 2*g*np.sin(theta1)
    omega1_p /= (2*L-L*cos**2)
    omega2_p = -L*(omega2**2)*sin*cos + 2*g*(np.sin(theta1))*cos - 2*L*(omega1**2)*sin - 2*g*np.sin(theta2)
    omega2_p /= (2*L-L*cos**2)
    return np.array([omega1, omega1_p, omega2, omega2_p]) 

def solve_double_pendulum(A1, A2, T):
    ### START YOUR CODE HERE ###
    t = 0 
    y = np.array([A1,0,A2,0])
    record = []
    while t <= T:
        if t!=T:
            record.append(y[2])
        sol = solve_ivp(f, [t, t+h], y, atol = 1E-6, rtol = 1E-6)
        y = sol.y[:,-1]
        t = sol.t[-1]   
    #### END YOUR CODE HERE ####
    return record



def calc_phasespace_orbits(A1,A2):
    result = np.zeros((4000))
    ### START YOUR CODE HERE ###
    result = solve_double_pendulum(A1,A2,20)
    #### END YOUR CODE HERE ####
    return result

def double_pendulum_fft(A1, A2):
    result = np.zeros(2)
    ### START YOUR CODE HERE ###
    
    h, N = 0.005, 4000
    rec = calc_phasespace_orbits(A1,A2)
    rec = fft(rec)
    max_mag = 0.
    max_freq = 0.
    for i in range(N//2):
        mag = abs(rec[i])
        freq = i/N/h
        if mag>max_mag:
            max_mag = mag
            max_freq = freq
    
    result[0] = max_freq
    result[1] = max_mag
    
    #### END YOUR CODE HERE ####
    return result
double_pendulum_fft(0.152492,0.672169)
