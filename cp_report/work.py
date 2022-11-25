import Harmonic
import Free_In_finiteBox
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate

def probability_density_graph(x1,x2,N,L,beta):
    ax = plt.gca()
    print("Alert: the nomalize constant might not correct.")
    beta = 0.5
    step = (x2-x1)/100
    x = np.arange(x1, x2, (x2-x1)/100)
    y = np.zeros(shape=x.shape)
    sum = 0 
    for i in range(y.size):
        phi = Free_In_finiteBox.gen_wavefunctions(N,L,x[i])
        y[i] = Free_In_finiteBox.cal_density(phi,phi,L,beta)
        sum += y[i]*step
    ax.plot(x,y/sum, label = r'$\beta = 0.5$')

    beta = 2
    step = (x2-x1)/100
    x = np.arange(x1, x2, (x2-x1)/100)
    y = np.zeros(shape=x.shape)
    sum = 0 
    for i in range(y.size):
        phi = Free_In_finiteBox.gen_wavefunctions(N,L,x[i])
        y[i] = Free_In_finiteBox.cal_density(phi,phi,L,beta)
        sum += y[i]*step
    ax.plot(x,y/sum, label = r'$\beta = 2$')

    beta = 8
    step = (x2-x1)/100
    x = np.arange(x1, x2, (x2-x1)/100)
    y = np.zeros(shape=x.shape)
    sum = 0 
    for i in range(y.size):
        phi = Free_In_finiteBox.gen_wavefunctions(N,L,x[i])
        y[i] = Free_In_finiteBox.cal_density(phi,phi,L,beta)
        sum += y[i]*step
    ax.plot(x,y/sum, label = r'$\beta = 8$')
    ax.legend()
    ax.set_xlabel("Position")
    ax.set_ylabel("probability Density")

def weight_vector(N,L,beta):
    weight = np.zeros(N)
    Z = 0
    sum = 0 
    for n in range(1,N+1):
        En = 0.5*pow(n*np.pi/L,2)
        weight[n-1] = np.exp(-beta*En)
        Z += weight[n-1]
    weight = weight/Z
    for n in range(N):
        sum += weight[n]*pow((n+1)*np.pi/L,2)
    print(sum)
    weight = np.sqrt(weight)
    return weight

def density_matrix(N,L,beta):
    tmp = np.zeros(shape=(N,N))
    Z = 0 
    for n in range(1,N+1):              
        En = 0.5*pow(n*np.pi/L,2)
        tmp[n-1][n-1] = np.exp(-1*beta*En)
        Z += tmp[n-1][n-1]
    return tmp/Z
    sum = np.zeros(shape=(N,N))
    vec = np.zeros(N)
    vec[0] = 1
    weight = np.zeros(N)
    Z = 0
    for n in range(1,N+1):
        En = 0.5*pow(n*np.pi/L,2)
        weight[n-1] = np.exp(-beta*En)
        Z += weight[n-1]
    weight = weight/Z
    weight = np.sqrt(weight)
    return np.outer(weight,weight)

def twice_momentum_operator(N,L):
    tmp = np.zeros(shape=(N,N))
    for n in range(1,N+1):                  
        tmp[n-1][n-1] = pow(n*np.pi/L,2)
    return tmp

def fourier_trick_cos(n,M,L):       # cos(nx) & sin(mx)
    coefficients = np.zeros(M+1, dtype='complex_')
    for m in range(1,M+1):
        func = lambda x: (2/L)*(n*np.pi/L)*np.cos(n*np.pi*x/L)*np.sin(m*np.pi*x/L)
        result = -1*integrate.quad(func, 0, L)[0]
        if abs(result) < 10E-9:
            result = 0 
        coefficients[m] = complex(0, result)
    return coefficients

def momentum_operator(N,L):
    tmp = np.zeros(shape=(N,N), dtype='complex_')
    for n in range(1,N+1):
        vec = fourier_trick_cos(n,N,L)
        for m in range(1,N+1):
            tmp[m-1][n-1] = vec[m]
    return tmp


# def Graph(coeff,x1,x2):
#     x = np.arange(x1,x2, (x2-x1)/100)
#     y = np.zeros(shape=x.shape)
#     L = x2-x1
#     plt.plot(x,x*pow(2/L,0.5)*np.sin(x*np.pi/5))
#     for n in range(1,len(coeff)):
#         y = np.add(y,coeff[n]*pow(2/L,0.5)*np.multiply(x,np.sin(n*np.pi*x/L)))
#         print(y)
#     plt.plot(x,y)

def fourier_trick_x(n,M,L):       # x & sin(nx)
    coefficients = np.zeros(M+1)
    for m in range(1,M+1):
        func = lambda x: x*(2/L)*np.sin((n*np.pi*x)/L)*np.sin((m*np.pi*x)/L)
        result = integrate.quad(func, 0, L)[0]
        coefficients[m] = result
    return coefficients

def position_operator(N,L):
    tmp = np.zeros(shape=(N,N))
    for n in range(1,N+1):
        vec = fourier_trick_x(n,N,L)
        for m in range(1,N+1):
            tmp[m-1][n-1] = vec[m]
    return tmp

def trace_two_matrix(m1,m2):
    result = np.trace(np.matmul(m1,m2))
    if abs(result) < 10E-9:
        result = 0
    print(result)
    return result