from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)
app.config["DEBUG"] = True

#tells flask where to go
@app.route("/")
def home():
    return render_template("basic.html", salary_band="All", interpolated_prediction="25K")


# This function gets the name param from the user and allows us to store and use the value
# In this case when you add /"some_text" onto the url it will show the message bellow using the value
# we gave in the url
@app.route("/<name>")
def user(name):
    return f"Hello {name}"

# this redirects a user to the page defined with the function home
# if function has params we need to give them just like when we call a function
# eg url_for("user", name="Admin!") goes to user func and assigning the name variable the
# string Admin!
@app.route("/admin")
def admin():
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run()