import numpy as np
L = 2.     # fm
x_min = -4.
x_max = +4.
h = 0.01       #step
conv =  0.0483 # 2m/hbar^2

def V(V0,x): 
    if abs(x)<=L:
        return -V0*((L-abs(x))/L)
    else:
        return 0
def f(x,y,V0,E):
    psi   = y[0]
    psip  = y[1]
    psipp = -conv*(E-V(V0,x))*psi
    return np.array([psip,psipp])

def solve_rk4(x0, x1, y, h, V0, E):
    x = x0
    psi = []
    while (x-x0)*(x-x1)<=1E-7:
        psi.append((x,y[0],y[1]))
        k1  = f(x, y, V0, E)
        k2  = f(x+0.5*h, y+0.5*h*k1, V0, E)
        k3  = f(x+0.5*h, y+0.5*h*k2, V0, E)
        k4  = f(x+h, y+h*k3, V0, E)
        y  += h/6.*(k1+2.*k2+2.*k3+k4)
        x  += h
    return np.array(psi)

def calc_delta(Xm,E,V0):
    kappa = (conv*abs(E))**0.5 # wave vector
    x_match = Xm 
    x = x_min
    y = np.array([np.exp(kappa*x),kappa*np.exp(kappa*x)])
    psi_L = solve_rk4(x,x_match,y,+0.01,V0,E)

    x = x_max
    y = np.array([np.exp(-kappa*x),-kappa*np.exp(-kappa*x)])
    psi_R = solve_rk4(x,x_match,y,-0.01,V0,E)

    delta = (psi_L[-1,2]/psi_L[-1,1]-psi_R[-1,2]/psi_R[-1,1]) / \
            (psi_L[-1,2]/psi_L[-1,1]+psi_R[-1,2]/psi_R[-1,1])
    return delta

def groundstate_energy(V0, Xm):
    E0 = 0.
    Xm = 1.1
    ### START YOUR CODE HERE ###
    E0 = -V0
    while abs(calc_delta(Xm,E0,V0))>1E-2:
        E0 += 0.1
    E0 = round(E0,0)
    return float(E0)
groundstate_energy(67.777407,+1.8)
