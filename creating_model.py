import pandas as pd
import joblib
from sklearn.metrics import mean_absolute_percentage_error, mean_squared_error, r2_score
from sklearn.ensemble import RandomForestRegressor

CSV_COLUMN_NAMES = ['Age', 'Region', 'Sex', 'Industry', 'Job_Title', 'Years_of_Experience', 'Number_of_Job_Moves',
                    'Level_of_Education', 'Salary_Band']
train = pd.read_csv(r"C:\Users\phoeb\Documents\Software Learning\training_data.csv", names=CSV_COLUMN_NAMES, header=0)
test = pd.read_csv(r"C:\Users\phoeb\Documents\Software Learning\testing_data.csv", names=CSV_COLUMN_NAMES, header=0)

# Separate features and target
features_test = test.drop(columns=['Salary_Band'])  # Features
target_test = test['Salary_Band']  # Target

features_train = train.drop(['Salary_Band'], axis=1) # features
target_train = train['Salary_Band'] # target

# Creating the model
model_RFR = RandomForestRegressor(n_estimators=50, random_state=12, oob_score=True)
# Training the model
model_RFR.fit(features_train, target_train)
# Testing the model
target_predictions = model_RFR.predict(features_test)
print(f"rfr loss = {mean_absolute_percentage_error(target_test, target_predictions)}")

# Access the OOB Score
oob_score = model_RFR.oob_score_
print(f'Out-of-Bag Score: {oob_score}')

# Evaluating the model
mse = mean_squared_error(target_test, target_predictions)
print(f'Mean Squared Error: {mse}')

r2 = r2_score(target_test, target_predictions)
print(f'R-squared: {r2}')

# Saving the model
joblib.dump(model_RFR, 'random_forest_model.joblib')
