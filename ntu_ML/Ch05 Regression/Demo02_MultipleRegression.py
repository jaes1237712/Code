# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 12:21:45 2019

@author: 俊男
"""

# In[] Pre-processing
import HappyML.preprocessor as pp

# Dataset Loading
dataset = pp.dataset("50_Startups.csv")

# Independent/Dependent Variables Decomposition
X, Y = pp.decomposition(dataset, [0, 1, 2, 3], [4])

# Apply One Hot Encoder to Column[3] & Remove Dummy Variable Trap
X = pp.onehot_encoder(X, columns=[3])
X = pp.remove_columns(X, [3])
#X = pp.onehot_encoder(X, columns=[3], remove_trap=True)

# Split Training vs. Testing Set
X_train, X_test, Y_train, Y_test = pp.split_train_test(X, Y, train_size=0.8)

# Feature Scaling (optional)
#X_train, X_test = pp.feature_scaling(fit_ary=X_train, transform_arys=(X_train, X_test))
#Y_train, Y_test = pp.feature_scaling(fit_ary=Y_train, transform_arys=(Y_train, Y_test))

# In[] Create Linear Regressor
from HappyML.regression import SimpleRegressor

simple_reg = SimpleRegressor()
Y_pred_simple = simple_reg.fit(X_train, Y_train).predict(X_test)

# R-Squared always increase in multiple linear regression --> Use Adjusted R-Squared instead
print("Goodness of Model (R-Squared Score):", simple_reg.r_score(X_test, Y_test))

# In[] Multiple Linear Regression

## Add one column X0 for constant C0
#import statsmodels.tools.tools as smtools
#X_train = smtools.add_constant(X_train)
#
## Try-and-Error of Selecting Features with Backward Elimination
#import statsmodels.api as sm
#
#features = [0, 1, 2, 3, 4, 5]
##features = [0, 1, 2, 3, 5]
##features = [0, 1, 2, 3]
##features = [0, 1, 3]
##features = [0, 1]
#X_opt = X_train.iloc[:, features]
#
#regressor_OLS = sm.OLS(exog=X_opt, endog=Y_train).fit()
#print(regressor_OLS.summary())

# In[] Predict by the model

## Add one column X0 for constant
#X_test = smtools.add_constant(X_test)
#
## Use selected features to predict
#X_opttest = X_test.iloc[:, features]
#Y_predmulti = regressor_OLS.predict(X_opttest)

# In[] Multiple Linear Regression with HappyML's class

# Add one constant column
X_train = pp.add_constant(X_train)
X_test = pp.add_constant(X_test)

# In[] Backward Elimination of Features
from HappyML.regression import MultipleRegressor

regressor = MultipleRegressor()
selected_features = regressor.backward_elimination(x_train=X_train, y_train=Y_train, verbose=True)

Y_predict = regressor.fit(x_train=X_train.iloc[:, selected_features], y_train=Y_train).predict(x_test=X_test.iloc[:, selected_features])

print("Goodness of Model (Adjusted R-Squared Score):", regressor.r_score())

# In[] 使用「均方差」（Mean Squared Error, MSE）比較兩個模型的好壞。MSE 小者勝
# 均方差定義 = SUM(Yi-Yh)^2/n
# 亦有人將「均方差」再開根號，得到「均方差根」（Root of MSE, RMSE）後，才來比較
from HappyML.performance import rmse

rmse_linear = rmse(Y_test, Y_pred_simple)
rmse_multi = rmse(Y_test, Y_predict)

if rmse_linear < rmse_multi:
    print("RMSE Linear:{:.4f} < RMSE Multi-Linear:{:.4f}...Linear smaller, WIN!!".format(rmse_linear, rmse_multi))
else:
    print("RMSE Linear:{:.4f} > RMSE Multi-Linear:{:.4f}...Multi-Linear smaller, WIN!!".format(rmse_linear, rmse_multi))

# In[] Check for Assumption of Regression
from HappyML.criteria import AssumptionChecker

checker = AssumptionChecker(X_train.iloc[:, selected_features], X_test.iloc[:, selected_features], Y_train, Y_test, Y_predict)
checker.y_lim = (-4, 4)
checker.heatmap = True
checker.check_all()
