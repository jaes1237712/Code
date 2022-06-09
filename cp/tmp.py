import numpy as np

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
    result = np.zeros(4)
    ### START YOUR CODE HERE ###
    t = 0 
    y1 = np.array([A1,0.])
    y2 = np.array([A2,0.])
    while t <= T:
        omega1 = y1[1]
        omega2 = y2[1]
        theta1 = y1[0]
        theta2 = y2[0]
        k1_1  = f1(t, y1,omega1,omega2,theta1,theta2)
        k1_2  = f1(t+0.5*h, y1+0.5*h*k1_1,omega1,omega2,theta1,theta2)
        k1_3  = f1(t+0.5*h, y1+0.5*h*k1_2,omega1,omega2,theta1,theta2)
        k1_4  = f1(t+h, y1+h*k1_3,omega1,omega2,theta1,theta2)

        k2_1  = f2(t, y2,omega1,omega2,theta1,theta2)
        k2_2  = f2(t+0.5*h, y2+0.5*h*k2_1,omega1,omega2,theta1,theta2)
        k2_3  = f2(t+0.5*h, y2+0.5*h*k2_2,omega1,omega2,theta1,theta2)
        k2_4  = f2(t+h, y2+h*k2_3,omega1,omega2,theta1,theta2)

        y1  += h/6.*(k1_1+2.*k1_2+2.*k1_3+k1_4)
        y2  += h/6.*(k2_1+2.*k2_2+2.*k2_3+k2_4)
        t  += h
    result = np.array([y1[0],y2[0],y1[1],y2[1]])
    #### END YOUR CODE HERE ####
    return result
solve_double_pendulum(0.226545,0.406019,5.)
