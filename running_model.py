import math
from typing import List

import joblib
import pandas as pd

from data_keys import get_data_values, get_salary_band
from user_input import get_user_input

FEATURE_NAMES: List[str] = ['Age', 'Region', 'Sex', 'Industry', 'Job_Title', 'Years_of_Experience',
                            'Number_of_Job_Moves', 'Level_of_Education']
# Load the MODEL from the file
MODEL = joblib.load('random_forest_MODEL.joblib')

def get_interpolated_prediction(MODEL_prediction, user=0):
    if MODEL_prediction < 4:
        integer = math.floor(MODEL_prediction)
        lower_bound = (20 * integer) + 10
        interpolation = (MODEL_prediction - integer) * 20
        interpolation_prediction = lower_bound + interpolation
        if user == 1:
            print(f"Interpolation prediction: £{interpolation_prediction}K")
        return interpolation_prediction
    else:
        if user == 1:
            print("You are in the highest band.")
        return 90


def make_predictions(df, user=0):
    prediction = MODEL.predict(df)
    if user == 1:
        print(f"This is the prediction:\n{prediction}")
    salary_band = get_salary_band(int(prediction[0]))
    if user == 1:
        print(f"Prediction for the single sample: £{salary_band}\n")
    return prediction, salary_band


def run_model(data, print_result=0):
    df = pd.DataFrame([data], columns=FEATURE_NAMES)
    prediction, salary_band = make_predictions(df, print_result)
    interpolated_prediction = get_interpolated_prediction(prediction[0], print_result)
    return interpolated_prediction, salary_band

# Gets user to input data
data_entered = get_user_input()
#data_entered = ["25-30", "London", "Female", "Technology", "Software Developer", "2-5", "1", "Master's", 25, 1]
# Taking first 8 values for data to go into model
new_data = get_data_values(data_entered[:-2])
