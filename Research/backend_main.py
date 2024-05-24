from suggestion_model import get_best_suggestion
from running_model import new_data, run_model

#if __name__ == "__main__":
    # Running the model and printing results
user_interpolated_prediction, user_salary_band = run_model(new_data, 1)
best_suggestion_prediction, biggest_salary_band, category, num_years = get_best_suggestion()
#print(best_suggestion_prediction, biggest_salary_band, category, num_years)
if user_interpolated_prediction < best_suggestion_prediction:
    print(f"If you had an increase in {category} then you could go into the salary band {biggest_salary_band} and be "
          f"estimated to earn {best_suggestion_prediction}")
