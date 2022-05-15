import numpy as np
from sklearn import svm

def train_and_deploy_svm_classifier(x_data, y_data):
    y_predict = np.zeros(1500)
    ### START YOUR CODE HERE ###
    param_C = [0.5, 1.0, 2.0]
    A_x, B_x, C_x, type = np.split(x_data, [500, 1000, 1500])
    A_y, B_y, C_y, type = np.split(y_data, [500, 1000, 1500])
    A_y_predict, B_y_predict, C_y_predict, type = np.split(y_predict, [500,1000,1500])
    spilt_X = np.array([A_x, B_x, C_x])
    spilt_Y = np.array([A_y, B_y, C_y])
    spilt_Y_predict = np.array([A_y_predict, B_y_predict, C_y_predict])
    for i in range(3):
        score_list = [0, 0, 0]
        best_score = 0
        seq = [i, (i+1)%3, (i+2)%3] # A,B,C B,C,A C,A,B
        for j in range(3):
            clf = svm.SVC(kernel='rbf', C=param_C[j])
            clf.fit(spilt_X[seq[0]], spilt_Y[seq[0]])
            score_list[j] = clf.score(spilt_X[seq[1]], spilt_Y[seq[1]])
            if score_list[j] > best_score:
                best_score = score_list[j]
                print(param_C[j],'\n')
                spilt_Y_predict[seq[2]] = clf.predict(spilt_X[seq[2]])
        print("-------------",'\n')

    y_predict = spilt_Y_predict.reshape(1,1500)[0]
    #### END YOUR CODE HERE ####
    return y_predict
