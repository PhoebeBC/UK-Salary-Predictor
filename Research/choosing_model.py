import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import mean_absolute_percentage_error
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression

CSV_COLUMN_NAMES = ['Age', 'Region', 'Sex', 'Industry', 'Job_Title', 'Years_of_Experience', 'Number_of_Job_Moves',
                    'Level_of_Education', 'Salary_Band']
train = pd.read_csv(r"C:\Users\phoeb\Documents\Software Learning\training_data.csv", names=CSV_COLUMN_NAMES, header=0)
test = pd.read_csv(r"C:\Users\phoeb\Documents\Software Learning\testing_data.csv", names=CSV_COLUMN_NAMES, header=0)

features_test = test.drop(columns=['Salary_Band'])  # Features
target_test = test['Salary_Band']  # Target

# Separate features and target
X = train.drop(['Salary_Band'], axis=1)
Y = train['Salary_Band']

# Split the training set into
# training and validation set
X_train, X_valid, Y_train, Y_valid = train_test_split(
    X, Y, train_size=0.8, test_size=0.2, random_state=0)

# Support vector Machine Model
model_SVR = svm.SVR()
model_SVR.fit(X_train, Y_train)
Y_pred = model_SVR.predict(X_valid)

print(f"svm loss = {mean_absolute_percentage_error(Y_valid, Y_pred)}")

# Random Forest Regressor Model
model_RFR = RandomForestRegressor(n_estimators=10)
model_RFR.fit(X_train, Y_train)
Y_pred = model_RFR.predict(X_valid)

print(f"rfr loss = {mean_absolute_percentage_error(Y_valid, Y_pred)}")

# Linear Regression Model
model_LR = LinearRegression()
model_LR.fit(X_train, Y_train)
Y_pred = model_LR.predict(X_valid)

print(f"lin reg loss = {mean_absolute_percentage_error(Y_valid, Y_pred)}")

# svm loss = 104407048687042.08
# rfr loss = 0.028009259259259258
# lin reg loss = 37990160049394.46
# So we will use rfr as it has the least loss