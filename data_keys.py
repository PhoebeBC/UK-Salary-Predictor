from math import floor, sqrt
from typing import List

age_data = ["Under 25", "25-30", "30-35", "35-40", "40-50", "50-65", "Over 65"]
region_data = ["London", "East Midlands", "South West", "West Midlands", "Scotland", "Wales", "North West",
               "Yorkshire", "Northern Ireland", "South East"]
gender_data = ["Female", "Male", "Other"]
industry_data = ["Technology", "Healthcare", "Finance", "Education", "Retail", "Hospitality", "Manufacturing",
                 "Construction", "Media", "Consulting"]
job_title_data = ["Software Developer", "Data Scientist", "Financial Analyst", "Business Consultant", "Project Manager",
                  "Nurse", "Teacher", "Sales Manager", "Restaurant Manager", "Journalist", "Engineer", "Architect",
                  "IT Support Specialist", "Psychologist", "HR Manager", "Marketing Specialist", "Event Planner",
                  "Quality Assurance Analyst", "Operations Manager", "Social Media Manager"]
years_of_experience_data = ["Under 2", "2-5", "5-10", "10-20", "Over 20"]
num_job_moves_data = ["0", "1", "2", "3", "4 Plus"]
level_education_data = ["High School", "College", "Bachelor's", "Master's", "PhD"]
salary_band_data = ["Under £30k", "£30k - £50k", "£50k - £70k", "£70k - £90k", "Over £90k"]


def get_data_values(data_list):
    # print(f"this is data_list {data_list}")
    # print(f"this is index {data_list[0]}")
    age = age_data.index(data_list[0])
    region = region_data.index(data_list[1])
    gender = gender_data.index(data_list[2])
    industry = industry_data.index(data_list[3])
    job_title = job_title_data.index(data_list[4])
    years_of_experience = years_of_experience_data.index(data_list[5])
    num_job_moves = num_job_moves_data.index(data_list[6])
    level_education = level_education_data.index(data_list[7])
    return [age, region, gender, industry, job_title, years_of_experience, num_job_moves, level_education]


def get_data_names(data_list):
    age = age_data[data_list[0]]
    region = region_data[data_list[1]]
    gender = gender_data[data_list[2]]
    industry = industry_data[data_list[3]]
    job_title = job_title_data[data_list[4]]
    years_of_experience = years_of_experience_data[data_list[5]]
    num_job_moves = num_job_moves_data[data_list[6]]
    level_education = level_education_data[data_list[7]]
    return [age, region, gender, industry, job_title, years_of_experience, num_job_moves, level_education]


def get_salary_band(value):
    return salary_band_data[value]


def get_age_category_value(age):
    if age < 25:
        return 0
    elif age > 65:
        return len(age_data)
    return floor((age - 20) / 5)


def get_age_category_name(age):
    return age_data[get_age_category_value(age)]


def get_job_moves_value(num_job_moves):
    if num_job_moves > 4:
        num_job_moves: int = 4
    return num_job_moves


def get_years_of_experience_category_value(years_of_experience):
    if years_of_experience > 20:
        experience_category_value = 4
    elif years_of_experience > 16:
        experience_category_value = 3
    else:
        experience_category_value = floor(sqrt(years_of_experience - 0.1))
    return experience_category_value


def get_years_of_experience_category_name(years_of_experience):
    return years_of_experience_data[get_years_of_experience_category_value(years_of_experience)]


# ["25", "1",......]
# first changing all to ints
# converting age into category value
# converting experience
def get_data_values_from_input(data_list):
    int_data_list: List[int] = []
    for data in data_list:
        int_data_list.append(int(data))
    int_data_list[0] = get_age_category_value(int_data_list[0])
    int_data_list[5] = get_years_of_experience_category_value(int_data_list[5])
    int_data_list[6] = get_job_moves_value(int_data_list[6])
    return int_data_list
