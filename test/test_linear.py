from sklearn import linear_model
import numpy as np
import matplotlib.pyplot as plt

# 线性回归
clf = linear_model.LinearRegression()
# 训练
np.array([1, 2, 3])
clf.fit(np.array([2, 4, 6]).reshape(-1,1), np.array([0, 2, 4]).reshape(-1,1))
# 表达式参数
a, b = clf.coef_, clf.intercept_
print(a)
print(b)

# # 画图
# # 1.真实的点
# plt.scatter(df['square_feet'], df['price'], color='blue')
#
# # 2.拟合的直线
# plt.plot(df['square_feet'], regr.predict(df['square_feet'].reshape(-1,1)), color='red', linewidth=4)
#
# plt.show()