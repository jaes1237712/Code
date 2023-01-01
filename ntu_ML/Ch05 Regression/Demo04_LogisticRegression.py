# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 21:53:25 2019

@author: 俊男
"""

# In[] Preprocessing
import HappyML.preprocessor as pp

# Load Dataset
dataset = pp.dataset(file="Social_Network_Ads.csv")

# X, Y Decomposition
X, Y = pp.decomposition(dataset, x_columns=[1, 2, 3], y_columns=[4])

# Categorical Data Encoding & Remove Dummy Variable Trap
X = pp.onehot_encoder(X, columns=[0], remove_trap=True)

# Feature Selection
from HappyML.preprocessor import KBestSelector
selector = KBestSelector()
X = selector.fit(x_ary=X, y_ary=Y, verbose=True, sort=True).transform(x_ary=X)

# Split Training & Testing set
X_train, X_test, Y_train, Y_test = pp.split_train_test(X, Y)

# Feature Scaling
X_train, X_test = pp.feature_scaling(fit_ary=X_train, transform_arys=(X_train, X_test))

# In[] Logistic Regression
#from sklearn.linear_model import LogisticRegression
#import time
#
## Model Creation
#classifier = LogisticRegression(solver="lbfgs", random_state=int(time.time()))
#
## Features Selection
#from sklearn.feature_selection import SelectKBest
#from sklearn.feature_selection import chi2
#
#kbest = SelectKBest(score_func=chi2, k=2)
#kbest = kbest.fit(X, Y)
#print("The p-values of Feature Importance: {}".format(kbest.pvalues_))
#
#X_train = kbest.transform(X_train)
#X_test = kbest.transform(X_test)
#
## Training
#classifier.fit(X_train, Y_train.values.ravel())
#
## Testing
#Y_pred_logistic = classifier.predict(X_test)
#
## Evaluation
#from sklearn.metrics import confusion_matrix
#from sklearn.metrics import accuracy_score
#from sklearn.metrics import precision_score
#from sklearn.metrics import recall_score
#from sklearn.metrics import fbeta_score
#
#print("Confusion Matrix:\n", confusion_matrix(y_true=Y_test, y_pred=Y_pred_logistic))
#print("Accuracy: {:.2%}".format(accuracy_score(Y_test, Y_pred_logistic)))
#print("Recall: {:.2%}".format(recall_score(Y_test, Y_pred_logistic)))
#print("Precision: {:.2%}".format(precision_score(Y_test, Y_pred_logistic)))
#print("F1-score: {:.2%}".format(fbeta_score(Y_test, Y_pred_logistic, beta=1)))

# In[] Logistic Regression with HappyML's Class
from HappyML.regression import LogisticRegressor
from HappyML.performance import ClassificationPerformance

# Training & Predict
regressor = LogisticRegressor()
Y_predict = regressor.fit(X_train, Y_train).predict(X_test)

# Performance
pfm = ClassificationPerformance(Y_test, Y_predict)

print("Confusion Matrix:\n", pfm.confusion_matrix())
print("Accuracy: {:.2%}".format(pfm.accuracy()))
print("Recall: {:.2%}".format(pfm.recall()))
print("Precision: {:.2%}".format(pfm.precision()))
print("F1-score: {:.2%}".format(pfm.f_score()))

# In[] Visualize the Result
import HappyML.model_drawer as md

md.classify_result(x=X_train, y=Y_train, classifier=regressor.regressor, 
                   title="訓練集樣本點 vs. 模型", font="DFKai-sb")
md.classify_result(x=X_test, y=Y_test, classifier=regressor.regressor, 
                   title="測試集樣本點 vs. 模型", font="DFKai-sb")
