import numpy as np


def Lyapunov_coeff(mu):
    Lambda = 0.
    ### START YOUR CODE HERE ###
    x = 0.5
    for i in range(500):
        Lambda += np.log(np.abs((1-mu*x)*np.e**(mu*(1-x))))
        x = x*np.e**(mu*(1-x))
    Lambda /=500
    #### END YOUR CODE HERE ####
    return float(Lambda)

Lyapunov_coeff(2.116449)