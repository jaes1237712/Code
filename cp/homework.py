import math
import scipy.integrate as integrate
#prob,err = integrate.quad(func,-n,n,epsabs=1E-10,epsrel=1E-10, args=(1))

def func(x,E,M,Gamma,sigma):
    return math.exp((-1*(math.pow(x,2)))/(2*(math.pow(sigma,2))))/(math.pow((math.pow(E-x,2)-math.pow(M,2)),2)+M*M*Gamma*Gamma)

def convoluted_BreitWigner(E, M, Gamma, sigma):
    value = 0.
    ### START YOUR CODE HERE ###
    value = integrate.quad(func,-math.inf,math.inf,epsabs=1E-10,epsrel=1E-10,args=(E,M,Gamma,sigma))[0]
    #### END YOUR CODE HERE ####
    return value

#Test point E=-3.2438, M=+1.2559, Gamma=+1.2073, sigma=+0.4605
#F(E, M, Gamma, sigma) expected=+0.01890289 result=+0.01927053 --- Failed
print(convoluted_BreitWigner(-3.2438, 1.2559, 1.2073, 0.4605))