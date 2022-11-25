import numpy as np
from sklearn import svm

def scan_over_svm_classifier(x_train, y_train, R, S):
    y_test = np.zeros(101)
    ### START YOUR CODE HERE ###
    clf  = svm.SVC(kernel='linear', C=1.0)
    clf.fit(x_train, y_train)
    for i in range(101):
        y_test[i] = clf.predict([[R,S,i*0.01]])
    #### END YOUR CODE HERE ####
    return y_test

