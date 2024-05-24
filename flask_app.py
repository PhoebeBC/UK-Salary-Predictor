from flask import Flask, render_template, redirect, url_for, request
from data_keys import get_data_values_from_input
from suggestion_model import get_best_suggestion
from running_model import run_model

app = Flask(__name__)
app.config["DEBUG"] = True


# This function gets the name param from the user and allows us to store and use the value
# In this case when you add /"some_text" onto the url it will show the message bellow using the value
# we gave in the url
@app.route("/<name>")
def login(name):
    return f"<h1>{name}</h1>"


# Get is normally visible, POST is more secure
@app.route("/", methods=["POST", "GET"])
def questions_answers():
    '''
    checking if we reach page with get or post request
    '''
    if request.method == "POST":
        answers = [
            request.form["age"],
            request.form["region"],
            request.form["gender"],
            request.form["industry"],
            request.form["job_title"],
            request.form["years_experience"],
            request.form["job_moves"],
            request.form["education_level"],
            request.form["age"], #age_input
            request.form["years_experience"]] #years_eperience_input
        new_data = get_data_values_from_input(answers)
        run_data = new_data[:-2]
        print(f"answers: {new_data}")
        user_interpolated_prediction, user_salary_band = run_model(run_data, 1)
        return redirect(url_for(
            "get_results",
            user_interpolated_prediction=user_interpolated_prediction,
            user_salary_band=user_salary_band
        ))
    else:
        return render_template("questions.html")


# this redirects a user to the page defined with the function home
# if function has params we need to give them just like when we call a function
# eg url_for("user", name="Admin!") goes to user func and assigning the name variable the
# string Admin!
@app.route("/results/<user_interpolated_prediction>/<user_salary_band>")
def get_results(user_interpolated_prediction, user_salary_band):
    #best_suggestion_prediction, biggest_salary_band, category, num_years = get_best_suggestion(new_data=new_data)
    # print(best_suggestion_prediction, biggest_salary_band, category, num_years)
    # if user_interpolated_prediction < best_suggestion_prediction:
    #     print(
    #         f"If you had an increase in {category} then you could go into the salary band {biggest_salary_band} and be "
    #         f"estimated to earn {best_suggestion_prediction}")
    return render_template("results.html", salary_band=user_salary_band, interpolated_prediction=user_interpolated_prediction )


if __name__ == "__main__":
    app.run()
