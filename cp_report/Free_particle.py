# 3.1.2 Werner Krauth - Statistical Mechanics_ Algorithms and Computations 
import numpy as np
import matplotlib.pyplot as plt

def gen_wavefunctions(N,L,x):
    phi_list = np.zeros(N+1, dtype='complex_')
    for n in range(N+1):
        z = complex(0, 2*n*np.pi*x/L)
        phi_list[n] = pow(1/L,0.5)*np.exp(z)
    return phi_list
    

#Algorithm 3.2 from  Werner Krauth - Statistical Mechanics_ Algorithms and Computations 
def cal_density(phi,phi_prime,T):
    N = len(phi)
    rho = 0     # rho(x,x',beta)
    for n in range(N):
        En = n + 0.5
        rho = rho + phi[n]*phi_prime[n]*np.exp(-1*En/T)
    return rho

def Wavefunc_graph(N,L,x1,x2):
    x = np.arange(x1,x2, (x2-x1)/100)
    y = np.zeros(shape=x.shape)
    for n in range(N):
        for i in range(y.size):
            y[i] = gen_wavefunctions(n+1,L,x[i]).real[n]
        plt.plot(x,y)
    for n in range(N):
        for i in range(y.size):
            y[i] = gen_wavefunctions(n+1,L,x[i]).imag[n]
        plt.plot(x,y)