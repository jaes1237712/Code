# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 10:10:12 2019

@author: 俊男
"""

# In[] Pre-processing
from HappyML import preprocessor as pp

# Dataset Loading
dataset = pp.dataset("Salary_Data.csv")

# Independent/Dependent Variables Decomposition
X, Y = pp.decomposition(dataset, [0], [1])

# Split Training vs. Testing Set
X_train, X_test, Y_train, Y_test = pp.split_train_test(X, Y, train_size=2/3)

# Feature Scaling (optional)
X_train, X_test = pp.feature_scaling(fit_ary=X_train, transform_arys=(X_train, X_test))
Y_train, Y_test = pp.feature_scaling(fit_ary=Y_train, transform_arys=(Y_train, Y_test))

# In[] Fitting Simple Regressor
# from sklearn.linear_model import LinearRegression

# regressor = LinearRegression()
# regressor.fit(X_train, Y_train)
# Y_pred = regressor.predict(X_test)

# R_Score = regressor.score(X_test, Y_test)

from HappyML.regression import SimpleRegressor

regressor = SimpleRegressor()
Y_pred = regressor.fit(X_train, Y_train).predict(X_test)
print("R-Squared Score:", regressor.r_score(X_test, Y_test))

# In[] Visualize the Training Set
#import matplotlib.pyplot as plt
#
#plt.scatter(X_train, Y_train, color="red")
#plt.plot(X_train, regressor.predict(X_train), color="blue")
#plt.title("Salary vs. Experience")
#plt.xlabel("Experience")
#plt.ylabel("Salary")
#plt.show()

from HappyML import model_drawer as md

sample_data=(X_train, Y_train)
model_data=(X_train, regressor.predict(X_train))
md.sample_model(sample_data=sample_data, model_data=model_data,
                title="訓練集樣本點 vs. 預測模型", font="DFKai-sb")
md.sample_model(sample_data=(X_test, Y_test), model_data=(X_test, Y_pred),
                title="測試集樣本點 vs. 預測模型", font="DFKai-sb")

# In[] Test for Linearity of Features
#from HappyML import model_drawer as md
#
#for i in range(X_train.shape[1]):
#    md.sample_model(sample_data=(X_train[:, i], Y_train), model_data=None, title="Linearity of Column {}".format(i))

from HappyML.criteria import AssumptionChecker

checker = AssumptionChecker(X_train, X_test, Y_train, Y_test, Y_pred)
checker.sample_linearity()

# In[] Test for Normal Distribution of Residuals
#import scipy.stats as stats
#import matplotlib.pyplot as plt
#
#residuals = (Y_test - Y_pred).ravel()
#stats.probplot(residuals, plot=plt)
#plt.show()

checker.residuals_normality()

# In[] Check for Errpr Uncorrelated
#from statsmodels.stats.stattools import durbin_watson
#
#dw = durbin_watson(residuals)
#print("殘差獨立性（完全正相關0～無相關2～完全負相關4）：", dw)

#from pandas.plotting import autocorrelation_plot
#import pandas as pd
#
#df_res = pd.DataFrame(residuals)
#autocorrelation_plot(df_res)
#plt.show()

checker.residuals_independence()

# In[] 殘差變異數等分散性

# Yellowbrick Install: conda install -c districtdatalabs yellowbrick

#from yellowbrick.regressor import ResidualsPlot
#
#visualizer = ResidualsPlot(regressor.regressor)
#visualizer.fit(X_train, Y_train)
#visualizer.score(X_test, Y_test)
#visualizer.poof()

checker.residuals_homoscedasticity(y_lim=(-4, 4))

# In[] 自變數各自獨立，無共線性

checker.features_correlation(heatmap=True)
