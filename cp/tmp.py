import scipy.integrate as integrate
import math as m
    
def nsigma_at_prob(prob):
    nsig = 0.
    ### START YOUR CODE HERE ###
    

    #### END YOUR CODE HERE ####
    return nsig

def func(x,mu,sigma):
    b = m.sqrt(2*m.pi)*sigma
    c = m.exp(-1*pow(x-mu,2)/(2*pow(sigma,2)))
    value = c/b
    
    return value

def prob_at_nsigma(n):
    prob = 0.
    ### START YOUR CODE HERE ###

    prob = integrate.quad(func, -n,n,args=(0,1))[0]
    #### END YOUR CODE HERE ####
    return prob
