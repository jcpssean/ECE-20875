import pandas
import matplotlib.pyplot as plt 
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn import metrics
import numpy as np


''' 
The following is the starting code for path1 for data reading to make your first step easier.
'dataset_1' is the clean data for path1.
'''
dataset_1 = pandas.read_csv('NYC_Bicycle_Counts_2016_Corrected.csv')
dataset_1['Brooklyn Bridge']      = pandas.to_numeric(dataset_1['Brooklyn Bridge'].replace(',','', regex=True))
dataset_1['Manhattan Bridge']     = pandas.to_numeric(dataset_1['Manhattan Bridge'].replace(',','', regex=True))
dataset_1['Queensboro Bridge']    = pandas.to_numeric(dataset_1['Queensboro Bridge'].replace(',','', regex=True))
dataset_1['Williamsburg Bridge']  = pandas.to_numeric(dataset_1['Williamsburg Bridge'].replace(',','', regex=True))

"""The use of the code provided is optional, feel free to add your own code to read the dataset. The use (or lack of use) of this code is optional and will not affect your grade."""

"""Problem 1"""

#plot the data
fig,axs = plt.subplots(2, 2)
fig.suptitle("Number of bike traffic for different bridges")
axs[0, 0].plot(dataset_1[['Brooklyn Bridge']])
axs[0, 0].set_title('Brooklyn Bridge')
axs[0, 1].plot(dataset_1[['Manhattan Bridge'] ])
axs[0, 1].set_title('Manhattan Bridge')
axs[1, 0].plot(dataset_1[['Queensboro Bridge']])
axs[1, 0].set_title('Queensboro Bridge')
axs[1, 1].plot(dataset_1[['Williamsburg Bridge']])
axs[1, 1].set_title('Williamsburg Bridge')
fig.tight_layout(pad = 2.0)
#create histogram
fig, axs = plt.subplots(2, 2)
fig.suptitle("Histogram of bike traffic for different bridges")
axs[0, 0].hist(dataset_1[['Brooklyn Bridge']])
axs[0, 0].set_title('Brooklyn Bridge')
axs[0, 1].hist(dataset_1[['Manhattan Bridge'] ])
axs[0, 1].set_title('Manhattan Bridge')
axs[1, 0].hist(dataset_1[['Queensboro Bridge']])
axs[1, 0].set_title('Queensboro Bridge')
axs[1, 1].hist(dataset_1[['Williamsburg Bridge']])
axs[1, 1].set_title('Williamsburg Bridge')
fig.tight_layout(pad = 2.0)
plt.show()

Brooklyn = dataset_1['Brooklyn Bridge'].values.tolist()
Manhattan = dataset_1['Manhattan Bridge'].values.tolist()
Queensboro = dataset_1['Queensboro Bridge'].values.tolist()
Williamsburg = dataset_1['Williamsburg Bridge'].values.tolist()
NormB = [(x - np.mean(Brooklyn))/np.std(Brooklyn) for x in Brooklyn]
NormM = [(x - np.mean(Manhattan))/np.std(Manhattan)for x in Manhattan]
Normq = [(x - np.mean(Queensboro))/np.std(Queensboro) for x in Queensboro]
NormW = [(x - np.mean(Williamsburg))/np.std(Williamsburg)for x in Williamsburg]
OnestdB = len([x for x in Brooklyn if (x > np.mean(Brooklyn) - np.std(Brooklyn) and x < np.mean(Brooklyn) + np.std(Brooklyn))])/len(Brooklyn)
print("Percentage of one std of Brooklyn", OnestdB)
OnestdM = len([x for x in Manhattan if (x > np.mean(Manhattan) - np.std(Manhattan) and x < np.mean(Manhattan) + np.std(Manhattan))])/len(Manhattan)
print("Percentage of one std of Manhattan", OnestdM)
OnestdQ = len([x for x in Queensboro if (x > np.mean(Queensboro) - np.std(Queensboro) and x < np.mean(Queensboro) + np.std(Queensboro))])/len(Queensboro)
print("Percentage of one std of Queensboro", OnestdQ)
OnestdW = len([x for x in Williamsburg if (x > np.mean(Williamsburg) - np.std(Williamsburg) and x < np.mean(Williamsburg) + np.std(Williamsburg))])/len(Williamsburg)
print("Percentage of one std of Williamsburg", OnestdW)


"""Problem 2"""

dataset_1['Total'] = pandas.to_numeric(dataset_1['Total'].replace(',', '', regex=True))

X = dataset_1[['High Temp', 'Low Temp','Precipitation']]
Y = dataset_1['Total']
X_train, X_test, Y_train, Y_test = train_test_split(
        X, Y, test_size=0.2, shuffle=False
    )

regr = linear_model.LinearRegression()
regr.fit(X_train, Y_train)

print('Intercept: \n', regr.intercept_)
print('Coefficients: \n', regr.coef_)

# total_hat = regr.intercept_ + regr.coef_[0]*X_test['Low Temp'] + regr.coef_[1]*X_test['Precipitation']
total_hat = regr.intercept_ + regr.coef_[0]*X_test['High Temp'] + regr.coef_[1]*X_test['Low Temp'] + regr.coef_[2]*X_test['Precipitation']
error = np.mean(abs((total_hat - Y_test)/Y_test))
print('Error = ' + str(error))
print('Accuracy = ' + str(1 - error))


"""problem3"""

###logistic regression
Total = [dataset_1['Total']]
To = np.array(Total).reshape(-1, 1)
Pre = np.array(dataset_1['Precipitation'])

plt.scatter(Total, Pre)
plt.xscale('symlog')
plt.xlabel('Total precipitation')
plt.ylabel('Raining or not')
for x in range(len(Pre)):
    if (Pre[x] > 0):
        Pre[x] = 1
    else:
        Pre[x]= 0
plt.scatter(Total, Pre)
x_train, x_test, y_train, y_test = train_test_split(To, Pre, test_size=0.2, random_state=0)
logistic_regr = linear_model.LogisticRegression()
logistic_regr.fit(x_train, y_train)
y_pred = logistic_regr.predict(x_test)
print("Accuracy :", metrics.accuracy_score(y_test, y_pred))






