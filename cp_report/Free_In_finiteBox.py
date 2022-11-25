# 3.1.3 Werner Krauth - Statistical Mechanics_ Algorithms and Computations 
import numpy as np
import matplotlib.pyplot as plt

def gen_wavefunctions(N,L,x):
    phi_list = np.zeros(N+1)
    for n in range(1,N+1):
        phi_list[n] = pow(2/L,0.5)*np.sin(n*np.pi*x/L)
    return phi_list
    

#Algorithm 3.2 from  Werner Krauth - Statistical Mechanics_ Algorithms and Computations 
def cal_density(phi,phi_prime,L,beta):
    N = len(phi)
    rho = 0     # rho(x,x',beta)
    for n in range(1,N):
        En = (1/2)*pow((n*np.pi/L),2)
        rho = rho + phi[n]*phi_prime[n]*np.exp(-1*En*beta)
    return rho

def Wavefunc_graph(N,L,x1,x2):
    x = np.arange(x1,x2, (x2-x1)/100)
    y = np.zeros(shape=x.shape)
    for n in range(1,N+1):
        for i in range(y.size):
            y[i] = gen_wavefunctions(n+1,L,x[i])[n]+2*n
        plt.plot(x,y)
