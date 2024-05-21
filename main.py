import pandas as pd
import sklearn
import numpy as np
import joblib
from user_input import get_user_input
from data_keys import get_data_values, get_salary_band

# Load the model from the file
model = joblib.load('random_forest_model.joblib')

#data_entered = get_user_input()
# Example of new input data (ensure it has the same features as the training data)
#new_data = get_data_values(data_entered)
new_data = [1, 0, 0, 0, 0, 0, 1, 2]

feature_names = ['Age', 'Region', 'Sex', 'Industry', 'Job_Title', 'Years_of_Experience', 'Number_of_Job_Moves',
                    'Level_of_Education']
single_sample_df = pd.DataFrame([new_data], columns=feature_names)
# Make predictions
prediction = model.predict(single_sample_df)
print(f"This is the prediction:\n{prediction}")


# Print predictions
# for i, prediction in enumerate(predictions):
#
salary_band = get_salary_band(int(prediction[0]))
print(f"Prediction for the single sample: {salary_band}")
