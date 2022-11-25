import numpy as np


def invert_horizontally(A):
    N = int(np.size(A)**(0.5))
    sum = 0
    for j in range(N):
        for i in range(N):
            sum += ((A[j][i] - A[j][N-i-1]))**2
    return sum            

def invert_vertically(A):
    N = int(np.size(A)**(0.5))
    sum = 0
    for j in range(N):
        for i in range(N):
            sum += ((A[j][i] - A[N-j-1][i]))**2
    return sum            

def rotate_90(A):
    N = int(np.size(A)**(0.5))
    sum = 0 # A'[-i+N][j] = 
    for j in range(N):
        for i in range(N):
            sum += ((A[-i+N-1][j] - A[j][i]))**2
    return sum


def calc_image_features(A):
    S = np.zeros(3)
    S[0] = invert_horizontally(A)
    S[1] = invert_vertically(A)
    S[2] = rotate_90(A)
    return S
