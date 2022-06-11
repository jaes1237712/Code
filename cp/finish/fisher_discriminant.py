import numpy as np
import scipy.linalg as linalg


def invert_horizontally(A):
    N_i = np.size(A, axis=0)
    N_j = np.size(A, axis=1)
    sum = 0
    for j in range(N_j):
        for i in range(N_i):
            sum += ((A[j][i] - A[j][N_i-i-1]))**2
    return sum            

def invert_vertically(A):
    N_i = np.size(A, axis=0)
    N_j = np.size(A, axis=1)
    sum = 0
    for j in range(N_j):
        for i in range(N_i):
            sum += ((A[j][i] - A[N_j-j-1][i]))**2
    return sum            

def rotate_90(A):
    N_i = np.size(A, axis=0)
    N_j = np.size(A, axis=1)
    sum = 0 # A'[-i+N][j] = 
    for j in range(N_j):
        for i in range(N_i):
            sum += ((A[-i+N_j-1][j] - A[j][i]))**2
    return sum


def calc_image_features(A):
    S = np.zeros(3)
    S[0] = invert_horizontally(A)
    S[1] = invert_vertically(A)
    S[2] = rotate_90(A)
    return S

def calc_fisher_weights(A, B):
    W = np.zeros(3)
    ### START YOUR CODE HERE ###
    N_A = np.size(A, axis=0)
    N_B = np.size(B, axis=0)
    var_A = np.zeros((N_A,3))
    var_B = np.zeros((N_B,3))
    for i in range(N_A):
        var_A[i] = calc_image_features(A[i])
    for i in range(N_B):
        var_B[i] = calc_image_features(B[i])
    var_A = np.transpose(var_A)
    var_B = np.transpose(var_B)
    mu_A = var_A.mean(axis = 1)
    mu_B = var_B.mean(axis = 1)
    cov_A = np.cov(var_A)
    cov_B = np.cov(var_B)
    # A_hor, A_ver, A_rotate = var_A[:,0], var_A[:,1], var_A[:,2]
    # B_hor, B_ver, B_rotate = var_B[:,0], var_B[:,1], var_B[:,2]
    W = np.dot(linalg.inv(cov_A+cov_B),mu_A-mu_B)
    norm = np.sqrt((W**2).sum())
    W /= norm
    #### END YOUR CODE HERE ####
    return W

def calc_fisher_dist(A, B):
    FA = np.zeros(len(A))
    FB = np.zeros(len(B))
    Fmin = np.Inf
    Fmax = 0.
    W = calc_fisher_weights(A,B)
    N_A = np.size(A, axis=0)
    N_B = np.size(B, axis=0)
    var_A = np.zeros((N_A,3))
    var_B = np.zeros((N_B,3))

    for i in range(N_A):
        var_A[i] = calc_image_features(A[i])
        for k in range(3): 
            FA[i] += var_A[i][k]*W[k]
    for i in range(N_B):
        var_B[i] = calc_image_features(B[i])
        for k in range(3): 
            FB[i] += var_B[i][k]*W[k]
    
    al = np.concatenate([FA,FB])
    Fmin = np.amin(al)
    Fmax = np.amax(al)            
    return FA, FB, float(Fmin), float(Fmax)


def calc_roc_curve(A, B):
    ROC = np.zeros((2,51))
    ### START YOUR CODE HERE ###
    FA, FB, Fmin, Fmax = calc_fisher_dist(A,B)
    def e(F,T):
        sum = 0
        for i in F:
            if i>T:
                sum += 1
        return sum/len(F)
    Fmin = 0
    Fmax = 1.00
    delta = 0.01
    for i in range(101):
        T = np.linspace(Fmin, Fmax, 101)[i] 
        ROC[0,i], ROC[1,i] = e(FA, T), e(FB, T)
    #### END YOUR CODE HERE ####
    return ROC

