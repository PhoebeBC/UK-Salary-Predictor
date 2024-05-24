from data_keys import get_age_category_name, get_years_of_experience_category_name
from running_model import data_entered, new_data, run_model



def get_new_age_years_of_experience_values():
    if new_data[5] < 4 and new_data[0] < 5:
        # age variables
        age_entered = data_entered[-2]
        inc_age_entered = age_entered
        age_category = get_age_category_name(age_entered)
        inc_age_category = get_age_category_name(inc_age_entered)
        # years of experience variables
        years_of_experience_entered = data_entered[-1]
        inc_years_of_experience_entered = years_of_experience_entered
        years_of_experience_category = get_years_of_experience_category_name(years_of_experience_entered)
        inc_years_of_experience_category = get_years_of_experience_category_name(inc_years_of_experience_entered)
        # year counter
        inc_years = 0
        # increasing years until age or years of experiences increases to the next category
        while age_category == inc_age_category and years_of_experience_category == inc_years_of_experience_category:
            inc_years += 1
            inc_age_entered += 1
            inc_years_of_experience_entered += 1
            inc_age_category = get_age_category_name(inc_age_entered)
            inc_years_of_experience_category = get_years_of_experience_category_name(inc_years_of_experience_entered)
        # getting the key for the new category
        inc_age = inc_age_entered
        inc_years_of_experience = inc_years_of_experience_entered
        return inc_age, inc_years_of_experience, inc_years
    return 0, 0, 0


def get_salary_age_years_of_experience_inc():
    inc_age, inc_years_of_experience, inc_years = get_new_age_years_of_experience_values()
    if inc_age == 0 and inc_years_of_experience == 0:
        return inc_age, inc_years_of_experience, inc_years
    inc_data = new_data
    inc_data[0] = inc_age
    inc_data[5] = inc_years_of_experience
    interpolated_prediction, salary_band = run_model(inc_data)
    return interpolated_prediction, salary_band, inc_years


def get_salary_job_moves_education_level_inc(category):
    # Setting data to user entered data
    inc_data = new_data
    max_category_value = 4
    # Choosing index for category
    index = 6 # for level_education
    if category == "job_moves":
        index = 7
    # Changing data given to MODEL based on the category we want to increase
    if new_data[index] < max_category_value:
        inc_data[index] += 1
        return run_model(inc_data)
    return 0, 0

def get_best_suggestion():
    job_moves_prediction, job_moves_salaray = get_salary_job_moves_education_level_inc("job_moves")
    education_level_prediction, education_level_salaray = get_salary_job_moves_education_level_inc("education_level")
    age_years_of_experience_prediction, age_years_of_experience_salary, num_years = get_salary_age_years_of_experience_inc()

    suggestion_inc = ["job_moves", "education_level", "age_years_of_experience"]
    suggestion_inc_prediction = [job_moves_prediction, education_level_prediction, age_years_of_experience_prediction]
    suggestion_inc_salary = [job_moves_salaray, education_level_salaray, age_years_of_experience_salary]

    biggest_prediction = max(suggestion_inc_prediction)
    best_suggestion_salary = suggestion_inc_salary[suggestion_inc_prediction.index(biggest_prediction)]
    category = suggestion_inc[suggestion_inc_prediction.index(biggest_prediction)]
    return biggest_prediction, best_suggestion_salary, category, num_years
