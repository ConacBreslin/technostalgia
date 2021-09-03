import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/home")
def home():
    technologies = mongo.db.technologies.find()
    return render_template("/home.html", technologies=technologies)


@app.route("/get_technologies")
def get_technologies():
    technologies = mongo.db.technologies.find()
    categories = mongo.db.categories.find()
    return render_template(
        "technologies.html", technologies=technologies, categories=categories)


@app.route("/registration", methods=["GET", "POST"])
def registration():
    if request.method == "POST":

        # Check if the passwords match
        user_password = request.form.get("password")
        confirm_password = request.form.get("confirm_password")
        if user_password != confirm_password:
            flash('Your passwords do not match, please try again')
            return redirect(url_for("registration"))

        # Check if the username is already in the database
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists, please try a new username")
            return redirect(url_for("registration"))

        registration = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password")),
            "first_name": request.form.get("first_name").lower(),
            "last_name": request.form.get("last_name").lower(),
            "email": request.form.get("email").lower(),
        }
        mongo.db.users.insert_one(registration)

        # Put the new user into the 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Welcome {}, you have successfully registered and you are now logged in ".format(
                            request.form.get("username")))
        return redirect(url_for("get_technologies", username=session["user"]))
    return render_template("registration.html", page_title="Register")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":

        # Check if the username exists in the database
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:

            # Make sure the hashed password matches the user's password
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                        session["user"] = request.form.get("username").lower()
                        flash(
                            "Welcome {}, you have successfully logged in"
                            .format(request.form.get("username")))
                        return redirect(url_for(
                            "get_technologies", username=session["user"]))

            else:
                # If passwords don't match
                flash("Your Username and/or Password were incorrect. Please try again")
                return redirect(url_for("login"))

        else:

            # If username doesn't exist in database
            flash("Your Username and/or Password were incorrect. Please try again")
            return redirect(url_for("login"))

    return render_template("login.html", page_title="Log In")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):

    # Get the session user's username from the database
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template(
            "profile.html", username=username, page_title="Profile")

    return redirect(url_for("login"))


@app.route("/logout")
def logout():

    # Remove the user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add_technology", methods=["GET", "POST"])
def add_technology():

    # Add a techonolgy to database
    if request.method == "POST":
        technology = {
            "technology_name": request.form.get("technology_name"),
            "category_name": request.form.get("category_name"),
            "technology_image": request.form.get("technology_image"),
            "technology_description": request.form.get(
                "technology_description"),
            "best_bits": request.form.get("best_bits"),
            "worst_bits": request.form.get("worst_bits"),
            "posted_by": session["user"]
        }
        mongo.db.technologies.insert_one(technology)
        flash("You have successfully added {{ technology_name }} to {{ category_name }}. Thank you!")
        return redirect(url_for("get_technologies"))

    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template(
        "add_technology.html", page_title="Add a Technology", categories=categories)


@app.route("/edit_technology/<technology_id>", methods=["GET", "POST"])
def edit_technology(technology_id):

    # Edit a techonolgy in database
    if request.method == "POST":
        edittedtech = {
            "technology_name": request.form.get("technology_name"),
            "category_name": request.form.get("category_name"),
            "technology_image": request.form.get("technology_image"),
            "technology_description": request.form.get(
                "technology_description"),
            "best_bits": request.form.get("best_bits"),
            "worst_bits": request.form.get("worst_bits"),
            "posted_by": session["user"]
        }
        mongo.db.technologies.update({"_id": ObjectId(technology_id)}, edittedtech)
        flash("You have successfully updated {{ technology_name }}. Thank you!")
        return redirect(url_for("get_technologies"))

    technology = mongo.db.technologies.find_one({"_id": ObjectId(technology_id)})
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("edit_technology.html", technology=technology, categories=categories)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
