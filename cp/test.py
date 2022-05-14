import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
# 0.00340883937	-0.00064
# 0.005079170661	-0.00094
# 0.006851767133	-0.00126
# 0.008522098424	-0.00157
B_list = np.array([[0.00340883937,0.005079170661,0.006851767133,0.008522098424]])
V_H_list = np.array([[-0.00064*(0.9),-0.00094*1.1,-0.00126,-0.00157*1.3]])
# plt.scatter(B_list,V_H_list)
# for i in range(len(B_list)):
#     plt.plot([B_list[i],0], [V_H_list[i],0])
regressor = LinearRegression()

regressor.fit(B_list,V_H_list)
plt.plot(B_list[0],regressor.predict(B_list)[0], color='k')
print(regressor.predict(B_list)[0])