import os
from flask import Flask, flash, render_template, redirect, request, session, url_for
from flask_pymongo import PyMongo
from datetime import datetime
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


@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    if query:
        technologies = list(mongo.db.technologies.find({"$text": {"$search": query}}))
    else:
        technologies = mongo.db.technologies.find()

    return render_template(
        "technologies.html", technologies=technologies)


@app.route("/add_comment", methods={"GET", "POST"})
def add_comment():
    if request.method == "POST":
        comment = {
            "technology_name": request.form.get("technology_name"),
            "technology_comment": request.form.get("technology_comment"),
            "author": session["user"],
            "created_on": datetime.now()
        }
        mongo.db.comments.insert_one(comment)

        flash("Your comment on {{ technology_name }} has been added")
    return redirect(url_for("profile", username=session["user"]))



@app.route("/edit_comment/<comment_id>", methods={"GET", "POST"})
def edit_comment(comment_id):
    # Edit a comment in database
    if request.method == "POST":
        editted_comment = {
            "technology_name": request.form.get("technology_name"),
            "technology_comment": request.form.get("technology_comment"),
            "author": session["user"],
            "created_on": datetime.now()
        }
        mongo.db.comments.update(
            {"_id": ObjectId(comment_id)}, editted_comment)

        flash("Your comment on {{ technology_name }} has been changed")
        return redirect(url_for("profile", username=session["user"]))

    comment = mongo.db.comments.find_one(
        {"_id": ObjectId(comment_id)})
    
    return render_template("edit_comment.html", comment=comment)


@app.route("/delete_comment/<comment_id>")
def delete_comment(comment_id):
    mongo.db.comments.remove({"_id": ObjectId(comment_id)})
    flash("{{ comments.technology_name }} has been deleted")
    return redirect(url_for("profile", username=session["user"]))



@app.route("/individual_technology/<technology_id>", methods=["GET", "POST"])
def individual_technology(technology_id):
    technology = mongo.db.technologies.find_one({"_id": ObjectId(technology_id)})
    comments = list(mongo.db.comments.find())
    return render_template("individual_technology.html", technology=technology, comments=comments)



@app.route("/registration", methods=["GET", "POST"])
def registration():
    if request.method == "POST":

        # Check if the passwords match
        user_password = request.form.get("password")
        confirm_password = request.form.get("confirm_password")
        if user_password != confirm_password:
            flash("Your passwords do not match, please try again")
            return redirect(url_for("registration"))

        # Check if the username is already in the database
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()}
        )

        if existing_user:
            flash("Username already exists, please try a new username")
            return redirect(url_for("registration"))
        
        # Add the new user into the database
        registration = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password")),
            "first_name": request.form.get("first_name").lower(),
            "last_name": request.form.get("last_name").lower(),
            "email": request.form.get("email").lower(),
            "is_admin": "off",
            "join_date": datetime.now(),
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
            {"username": request.form.get("username").lower()}
        )

        if existing_user:

            # Make sure the hashed password matches the user's password
            if check_password_hash(
                existing_user["password"], request.form.get("password")
            ):
                session["user"] = request.form.get("username").lower()
                flash(
                    "Welcome {}, you have successfully logged in".format(
                        request.form.get("username")
                    )
                )
                return redirect(
                    url_for("get_technologies", username=session["user"]))

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
    comments = list(mongo.db.comments.find(
                           {"author": session["user"]}))
    technologies = list(mongo.db.technologies.find({"added_by": session["user"]}))
    if session["user"]:
        return render_template(
            "profile.html", username=username, comments=comments, technologies=technologies, page_title="Profile")

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
            "added_by": session["user"],
            "added_on": datetime.now()
        }
        mongo.db.technologies.insert_one(technology)
        flash(
            "You have successfully added {{ technologies.technology_name }} to {{ categories.category_name }}. Thank you!"
        )
        return redirect(url_for("get_technologies"))

    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template(
        "add_technology.html", page_title="Add a Technology",
        categories=categories
    )


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
            "posted_by": session["user"],
        }
        mongo.db.technologies.update(
            {"_id": ObjectId(technology_id)}, edittedtech)
        flash("You have successfully updated {{ technology.technology_name }}. Thank you!")
        return redirect(url_for("get_technologies"))

    technology = mongo.db.technologies.find_one(
        {"_id": ObjectId(technology_id)})
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template(
        "edit_technology.html", technology=technology, categories=categories
    )


@app.route("/delete_technology/<technology_id>")
def delete_technology(technology_id):
    mongo.db.technologies.remove({"_id": ObjectId(technology_id)})
    flash("{{ technology_name }} has been deleted")
    return redirect(url_for("get_technologies"))


@app.route("/manage_categories")
def manage_categories():
    categories = list(mongo.db.categories.find().sort("category_name", 1))
    return render_template("manage_categories.html", categories=categories)


@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    if request.method == "POST":
        category = {"category_name": request.form.get("category_name")}
        mongo.db.categories.insert_one(category)
        flash("You have added a new category of {{ category_name }}")
        return redirect(url_for("manage_categories"))

    return render_template("add_category.html")


@app.route("/edit_category/<category_id>", methods=["GET", "POST"])
def edit_category(category_id):
    if request.method == "POST":
        edittedcategory = {"category_name": request.form.get("category_name")}
        mongo.db.categories.update({"_id": ObjectId(
            category_id)}, edittedcategory)
        flash("{{ category.category_name }} was successfully editted")
        return redirect(url_for("manage_categories"))

    category = mongo.db.categories.find_one({"_id": ObjectId(category_id)})
    return render_template("edit_category.html", category=category)



if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")), debug=True)
