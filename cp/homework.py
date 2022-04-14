import math as mp
import scipy.integrate as integrate
#prob,err = integrate.quad(func,-n,n,epsabs=1E-10,epsrel=1E-10, args=(1))

def func(x,E,M,Gamma,sigma):
    temp = E-x
    return mp.exp((-1*(mp.pow(x,2)))/(2*(mp.pow(sigma,2))))/(mp.pow((mp.pow(temp,2)-mp.pow(M,2)),2)+mp.pow(M*Gamma,2))

def convoluted_BreitWigner(E, M, Gamma, sigma):
    value = 0.
    ### START YOUR CODE HERE ###
    value = integrate.quad(func, -3*sigma, 3*sigma, epsabs=1E-10,epsrel=1E-10,args=(E,M,Gamma,sigma))[0]
    #### END YOUR CODE HERE ####
    return value

# Test point E=+2.8562, M=+2.3097, Gamma=+0.3054, sigma=+0.4376
print(convoluted_BreitWigner(+2.8562,+2.3097,+0.3054,+0.4376))

