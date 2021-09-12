import os
from flask import Flask, flash, render_template, redirect, request, session, url_for
from flask_pymongo import PyMongo
from datetime import datetime
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash

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

    # Find and display all technologies in database
    technologies = list(mongo.db.technologies.find())
    categories = mongo.db.categories.find()
    return render_template(
        "technologies.html", technologies=technologies, categories=categories
    )


@app.route("/search", methods=["GET", "POST"])
def search():

    # Search by keyword or by category
    query = request.form.get("query")
    category_search = request.form.get("category_search")
    if query:
        technologies = list(mongo.db.technologies.find({"$text": {"$search": query}}))

    elif category_search:
        technologies = list(
            mongo.db.technologies.find({"$text": {"$search": category_search}})
        )

    return render_template("technologies.html", technologies=technologies)


@app.route("/add_comment", methods={"GET", "POST"})
def add_comment():

    # Add a comment to the database
    if request.method == "POST":
        comment = {
            "technology_name": request.form.get("technology_name"),
            "technology_comment": request.form.get("technology_comment"),
            "author": session["user"],
            "created_on": datetime.now().strftime("%d %B, %Y at %H:%M"),
        }
        mongo.db.comments.insert_one(comment)

        flash("Your comment has been added")
    return redirect(url_for("profile", username=session["user"]))


@app.route("/edit_comment/<comment_id>", methods={"GET", "POST"})
def edit_comment(comment_id):

    # Edit a comment in database
    if request.method == "POST":
        editted_comment = {
            "technology_name": request.form.get("technology_name"),
            "technology_comment": request.form.get("technology_comment"),
            "author": session["user"],
            "editted_on": datetime.now().strftime("%d %B, %Y at %H:%M"),
        }
        mongo.db.comments.update({"_id": ObjectId(comment_id)}, editted_comment)

        flash("Your comment on  has been changed")
        return redirect(url_for("profile", username=session["user"]))

    comment = mongo.db.comments.find_one({"_id": ObjectId(comment_id)})
    return render_template("edit_comment.html", comment=comment)


@app.route("/delete_comment/<comment_id>")
def delete_comment(comment_id):
    # Delete a camment from the database
    flash("Your comment has been deleted")
    mongo.db.comments.remove({"_id": ObjectId(comment_id)})
    return redirect(url_for("profile", username=session["user"]))


@app.route("/comments/<technology_id>", methods=["GET", "POST"])
def comments(technology_id):
    technology = mongo.db.technologies.find_one({"_id": ObjectId(technology_id)})
    comments = list(mongo.db.comments.find())
    return render_template(
        "comments.html",
        technology=technology,
        comments=comments,
        page_title="Comment Page",
    )


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
            "is_admin": False,
            "join_date": datetime.now().strftime("%B %Y"),
        }
        mongo.db.users.insert_one(registration)

        # Put the new user into the 'session' cookie
        session["user"] = request.form.get("username").lower()

        flash(
            "Welcome {}, you have registered and are logged in ".format(
                request.form.get("username")
            )
        )
        return redirect(url_for("get_technologies", username=session["user"]))
    return render_template("registration.html", page_title="Register")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":

        # Check if the username exists in the database
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()}
        )

        # Set the users session variable of is_admin to False in the 'session' cookie
        session["is_admin"] = False

        # Check if is_admin is true in database and if so set is_admin to true in session cookie
        if "is_admin" in existing_user and existing_user["is_admin"]:
            session["is_admin"] = True

        if existing_user:

            # Check if the hashed password matches the user's password
            if check_password_hash(
                existing_user["password"], request.form.get("password")
            ):
                session["user"] = request.form.get("username").lower()
                flash(
                    "Welcome {}, you have successfully logged in".format(
                        request.form.get("username")
                    )
                )
                return redirect(url_for("get_technologies", username=session["user"]))

            else:
                # If passwords don't match
                flash("Your Username and/or Password were incorrect. Please try again")
                return redirect(url_for("login"))

        else:
            # If username doesn't exist in database
            flash("""Your Username and/or
            Password were incorrect. Please try again""")
        return redirect(url_for("login"))

    return render_template("login.html", page_title="Log In")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):

    # Get the session user's username, comments and technologies from the database
    user = mongo.db.users.find_one({"username": session["user"]})
    username = user["username"]
    join_date = user["join_date"]

    comments = list(mongo.db.comments.find({"author": session["user"]}))
    technologies = list(mongo.db.technologies.find({"added_by": session["user"]}))

    if session["user"]:
        return render_template(
            "profile.html",
            username=username,
            comments=comments,
            technologies=technologies,
            page_title="Profile",
            join_date=join_date
        )

    return redirect(url_for("login"))


@app.route("/logout")
def logout():

    # Remove the user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add_technology", methods=["GET", "POST"])
def add_technology():

    if request.method == "POST":

        # Check if the technology is already in the database
        existing_technology = mongo.db.technologies.find_one(
            {"technology_name": request.form.get("technology_name")}
        )

        if existing_technology:
            flash("This technology already exists")
            return redirect(url_for("add_technology"))

        # Add the new technolgy to the database
        newtechnology = {
            "technology_name": request.form.get("technology_name"),
            "category_name": request.form.get("category_name"),
            "technology_image": request.form.get("technology_image"),
            "technology_description": request.form.get("technology_description"),
            "best_bits": request.form.get("best_bits"),
            "worst_bits": request.form.get("worst_bits"),
            "added_by": session["user"],
            "added_on": datetime.now().strftime("%d %B, %Y at %H:%M"),
        }
        mongo.db.technologies.insert_one(newtechnology)
        flash("You have successfully added a new technology. Thank you!")
        return redirect(url_for("profile", username=session["user"]))

    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template(
        "add_technology.html",
        page_title="Add a Technology",
        categories=categories,
    )


@app.route("/edit_technology/<technology_id>", methods=["GET", "POST"])
def edit_technology(technology_id):

    # Edit a techonolgy in database
    if request.method == "POST":
        edittedtech = {
            "technology_name": request.form.get("technology_name"),
            "category_name": request.form.get("category_name"),
            "technology_image": request.form.get("technology_image"),
            "technology_description": request.form.get("technology_description"),
            "best_bits": request.form.get("best_bits"),
            "worst_bits": request.form.get("worst_bits"),
            "added_by": session["user"],
            "added_on": "",
        }

        mongo.db.technologies.update({"_id": ObjectId(technology_id)}, edittedtech)
        flash("Your technology has been updated. Thank you!")
        return redirect(url_for("get_technologies"))

    technology = mongo.db.technologies.find_one({"_id": ObjectId(technology_id)})
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template(
        "edit_technology.html", technology=technology, categories=categories
    )


@app.route("/delete_technology/<technology_id>")
def delete_technology(technology_id):

    # Find and then delete comments on a technology from database
    technology_name = mongo.db.technologies.find_one(
        {"_id": ObjectId(technology_id)}
    )["technology_name"]
    mongo.db.comments.remove({"technology_name": technology_name})

    # Delete a technology from database
    mongo.db.technologies.remove({"_id": ObjectId(technology_id)})
    flash("Your technology has been deleted")
    return redirect(url_for("profile", username=session["user"]))


@app.route("/manage_categories")
def manage_categories():
    categories = list(mongo.db.categories.find())
    return render_template(
        "manage_categories.html", categories=categories, page_title="Manage Categories"
    )


@app.route("/add_category", methods=["GET", "POST"])
def add_category():

    # Add a new category to the database
    if request.method == "POST":

        # Check if the category is already in the database
        existing_category = mongo.db.categories.find_one(
            {"category_name": request.form.get("category_name")}
        )

        if existing_category:
            flash("This category already exists")
            return redirect(url_for("add_category"))

        newcategory = {"category_name": request.form.get("category_name")}
        mongo.db.categories.insert_one(newcategory)
        flash("You have successfully added a new category.")
        return redirect(url_for("manage_categories"))

    return render_template("add_category.html", page_title="Add a new Category")


@app.route("/edit_category/<category_id>", methods=["GET", "POST"])
def edit_category(category_id):

    # Edit a technology in database
    if request.method == "POST":
        edittedcategory = {"category_name": request.form.get("category_name")}
        mongo.db.categories.update({"_id": ObjectId(category_id)}, edittedcategory)
        flash("The category was successfully editted")
        return redirect(url_for("manage_categories"))

    category = mongo.db.categories.find_one({"_id": ObjectId(category_id)})
    return render_template(
        "edit_category.html", category=category, page_title="Edit this Category"
    )


@app.route("/delete_category/<category_id>")
def delete_category(category_id):

    # Find and then delete technologies in a the category being deleted
    category_name = mongo.db.categories.find_one({"_id": ObjectId(category_id)}).get(
        "category_name"
    )

    technologies = mongo.db.technologies.find({"category_name": category_name})

    print(technologies)

    for technology in technologies:
        delete_technology(technology.get("_id"))

    # Delete the category from database
    mongo.db.categories.remove({"_id": ObjectId(category_id)})
    flash("You have deleted this category")
    return redirect(url_for("manage_categories"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"), port=int(os.environ.get("PORT")), debug=True)
