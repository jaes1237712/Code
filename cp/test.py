import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm
from sklearn.model_selection import GridSearchCV

for i in range(3):
    seq = [i, (i+1)%3, (i+2)%3] # A,B,C B,C,A C,A,B
    print(seq)