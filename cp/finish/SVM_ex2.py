import numpy as np
from sklearn import svm
from sklearn.model_selection import GridSearchCV

def best_trained_svm_classifier(x_train, y_train, x_test):
    y_test = np.zeros(100)
    ### START YOUR CODE HERE ###
    param = {'C':[0.5,1.0], 'gamma':[0.5, 1.0, 2.0]}
    clf = svm.SVC(kernel='rbf')
    grid = GridSearchCV(clf, param, verbose=3)
    grid.fit(x_train, y_train)
    y_test = grid.predict(x_test)
    #### END YOUR CODE HERE ####
    return y_test
