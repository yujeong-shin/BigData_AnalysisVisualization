import pymongo
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn import linear_model

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["BigDataAV"]
mycol = mydb["usedcars"]

# 2. Perform linear regression for two attributes: YEAR and MILEAGE
# x_train = []
# y_train = []
# regr = linear_model.LinearRegression()
#
# for item in mycol.find():
#     x_train.append(item["year"])
#     y_train.append(item["mileage"])
#
# X = np.asarray(x_train)
# Y = np.asarray(y_train)
# regr.fit(X.reshape(-1, 1), Y)
#
# plt.xlabel('year')
# plt.ylabel('mileage')
# plt.plot(X, Y, 'o')
# plt.plot(X, regr.predict(X.reshape(-1, 1)), color='r')
# plt.show()

# 3. Predict car price when car year is 2010 and price is 10000
x_train = []
y_train = []
regr = linear_model.LinearRegression()
for item in mycol.find():
    x_train.append([item["year"], item["mileage"]])
    y_train.append(item["price"])

regr.fit(x_train, y_train)

unknown_points = [[2010, 15000]]
guesses = regr.predict(unknown_points)
print(guesses)


# 4. Draw boxplot for YEAR and MILEAGE
# x_train = []
# y_train = []
#
# for item in mycol.find():
#     x_train.append(item["year"])
#     y_train.append(item["mileage"])


# plt.boxplot(x_train)
# plt.show()
# plt.boxplot(y_train)
# plt.show()

# remove outlier
# def find_upper_lower_bound(data_list):
#     temp = sorted(data_list)
#     q1, q3 = np.percentile(temp, [25, 75])
#     iqr = q3 - q1
#     lower_bound = q1 - (1.5 * iqr)
#     upper_bound = q3 + (1.5 * iqr)
#     return lower_bound, upper_bound


# YEAR
# lower, upper = find_upper_lower_bound(x_train)
# print('YEAR lower bound, upper bound : ', lower, upper)
#
# for val in x_train:
#     if val < lower or val > upper:
#         x_train.remove(val)
#
# plt.boxplot(x_train)
# plt.show()
#
# # MILEAGE
# lower, upper = find_upper_lower_bound(y_train)
# print('MILEAGE lower bound, upper bound : ', lower, upper)
#
# for val in y_train:
#     if val < lower or val > upper:
#         y_train.remove(val)
#
# plt.boxplot(y_train)
# plt.show()
