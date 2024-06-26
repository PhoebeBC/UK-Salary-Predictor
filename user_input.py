from math import floor

from data_keys import level_education_data, region_data, industry_data, job_title_data

ages_strings = [
        "Under 25",
        "25-30",
        "30-35",
        "35-40",
        "40-45",
        "45-50",
        "50-55",
        "55-60",
        "60-65",
        "Over 65"
    ]

def get_index_from_age(age):
    if age < 25:
        return 0
    elif age > 65:
        return len(ages_strings)
    return (age - 20) / 5

def get_age_category(age):
    return ages_strings[floor(get_index_from_age(age))]


def get_years_of_experience_category(years_of_experience):
    experience_category = ""
    if years_of_experience < 2:
        experience_category = "Under 2"
    elif years_of_experience < 5:
        experience_category = "2-5"
    elif years_of_experience < 10:
        experience_category = "5-10"
    elif years_of_experience < 20:
        experience_category = "10-20"
    else:
        experience_category = "Over 20"
    return experience_category


def get_job_moves(num_job_moves):
    job_moves_category = ""
    if num_job_moves < 4:
        job_moves_category = str(num_job_moves)
    else:
        job_moves_category = "4 Plus"
    return job_moves_category


def print_options(data_list):
    for data in data_list:
        print(data)


def get_user_input():
    age_input = int(input("Please enter your age\n"))
    age = get_age_category(age_input)

    print_options(region_data)
    region = input("Please type in your region from the list above\n")

    gender = input("Please choose your gender from the following:\nMale\nFemale\nOther\n")

    print_options(industry_data)
    industry = input("Please type in your Industry from the list above\n")

    print_options(job_title_data)
    job_title = input("Please type in the job title closest to your own from the list above\n")

    years_of_experience_input = int(input("Please enter the number of years of experience you have.\n"))
    years_of_experience = get_years_of_experience_category(years_of_experience_input)

    num_job_moves_input = int(input("Please enter the number times you have moved jobs.\n"))
    num_job_moves = get_job_moves(num_job_moves_input)

    print_options(level_education_data)
    level_education = input("Please the highest level of education you have from the list above.\n")

    return [age, region, gender, industry, job_title, years_of_experience, num_job_moves, level_education, age_input,
            years_of_experience_input]
