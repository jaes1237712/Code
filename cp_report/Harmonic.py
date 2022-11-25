#Algorithm 3.1 from  Werner Krauth - Statistical Mechanics_ Algorithms and Computations 
import numpy as np
import matplotlib.pyplot as plt


def gen_wavefunctions(n,x):
    phi_zero = pow(np.pi,0.25)*np.exp(-x**2/2) 
    phi_one = pow(2,0.5)*x*phi_zero
    phi_list = np.zeros(n+1)
    phi_list[0] = phi_zero
    phi_list[1] = phi_one
    for i in range(2,n+1):
        phi_list[i] = pow(2/i, 0.5)*x*phi_list[i-1] - pow((i-1)/i, 0.5)*phi_list[i-2]
    return phi_list
    
#Algorithm 3.2 from  Werner Krauth - Statistical Mechanics_ Algorithms and Computations 
def cal_density(phi,phi_prime,beta):
    N = len(phi)
    rho = 0     # rho(x,x',beta)
    for n in range(N):
        En = n + 0.5
        rho = rho + phi[n]*phi_prime[n]*np.exp(-1*beta*En)
    return rho

def Wavefunc_graph(N,x1,x2):
    x = np.arange(x1,x2, (x2-x1)/100)
    y = np.zeros(shape=x.shape)
    for n in range(N):
        for i in range(y.size):
            y[i] = gen_wavefunctions(n+1,x[i])[n] + 3*n

        plt.plot(x,y)


