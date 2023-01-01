# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 15:34:55 2019

@author: 俊男
"""

# In[] Data Preprocessing
import HappyML.preprocessor as pp

# Load Data
dataset = pp.dataset(file="Social_Network_Ads.csv")

# X, Y decomposition
X, Y = pp.decomposition(dataset, x_columns=[1, 2, 3], y_columns=[4])

# One-Hot Encoder
X = pp.onehot_encoder(ary=X, columns=[0], remove_trap=True)

# Feature Selection
from HappyML.preprocessor import KBestSelector
selector = KBestSelector()
X = selector.fit(x_ary=X, y_ary=Y, verbose=True, sort=True).transform(x_ary=X)

# Split Training / TEsting Set
X_train, X_test, Y_train, Y_test = pp.split_train_test(x_ary=X, y_ary=Y)

# Feature Scaling
X_train, X_test = pp.feature_scaling(fit_ary=X_train, transform_arys=(X_train, X_test))

# In[] Training & Testing
# from sklearn.naive_bayes import GaussianNB

# classifier = GaussianNB()
# classifier.fit(X_train, Y_train.values.ravel())

# Y_pred = classifier.predict(X_test)

# In[] Training & Testing using HappyML's Class
from HappyML.classification import NaiveBayesClassifier

classifier = NaiveBayesClassifier()
Y_pred = classifier.fit(X_train, Y_train).predict(X_test)

# In[] Performance
from HappyML.performance import ClassificationPerformance

pfm = ClassificationPerformance(Y_test, Y_pred)
print("Confusion Matrix:\n", pfm.confusion_matrix())
print("Accuracy: {:.2%}".format(pfm.accuracy()))
print("Recall: {:.2%}".format(pfm.recall()))
print("Precision: {:.2%}".format(pfm.precision()))
print("F1-score: {:.2%}".format(pfm.f_score()))

# In[] K-Fold Validation
#from sklearn.model_selection import cross_val_score
#
#k_fold = 10
#accuracies = cross_val_score(estimator=classifier.classifier, X=X, y=Y.values.ravel(), scoring="accuracy", cv=k_fold, n_jobs=-1)
#print("{} Folds Mean Accuracy: {}".format(k_fold, accuracies.mean()))
#
#recalls = cross_val_score(estimator=classifier.classifier, X=X, y=Y.values.ravel(), scoring="recall", cv=k_fold, n_jobs=-1)
#print("{} Folds Mean Recall: {}".format(k_fold, recalls.mean()))
#
#precisions = cross_val_score(estimator=classifier.classifier, X=X, y=Y.values.ravel(), scoring="precision", cv=k_fold, n_jobs=-1)
#print("{} Folds Mean Precision: {}".format(k_fold, precisions.mean()))
#
#f_scores = cross_val_score(estimator=classifier.classifier, X=X, y=Y.values.ravel(), scoring="f1", cv=k_fold, n_jobs=-1)
#print("{} Folds Mean F1-Score: {}".format(k_fold, f_scores.mean()))

from HappyML.performance import KFoldClassificationPerformance

K = 10
kfp = KFoldClassificationPerformance(x_ary=X, y_ary=Y, classifier=classifier.classifier, k_fold=K, verbose=False)

print("{} Folds Mean Accuracy: {}".format(K, kfp.accuracy()))
print("{} Folds Mean Recall: {}".format(K, kfp.recall()))
print("{} Folds Mean Precision: {}".format(K, kfp.precision()))
print("{} Folds Mean F1-Score: {}".format(K, kfp.f_score()))

# In[] Visualization
import HappyML.model_drawer as md

md.classify_result(x=X_train, y=Y_train, classifier=classifier, title="訓練集 vs. 模型", font='DFKai-sb')
md.classify_result(x=X_test, y=Y_test, classifier=classifier, title="測試集 vs. 模型", font='DFKai-sb')

# In[] Check for Variables Independence
from HappyML.criteria import AssumptionChecker

checker = AssumptionChecker(x_train=X_train, x_test=X_test, y_train=Y_train, y_test=Y_test, y_pred=Y_pred)
checker.features_correlation(heatmap=True)
