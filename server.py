"""Server for movie ratings app."""

from flask import (Flask, render_template, request, flash, session, redirect)
from model import connect_to_db
import crud
from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined


@app.route("/")
def homepage():
    """View the homepage."""

    return render_template("homepage.html")

@app.route("/movies")
def show_all_movies():
    """View a list of all movies in the db."""

    movies = crud.get_all_movies()

    return render_template("all_movies.html", movies=movies)

@app.route("/movies/<movie_id>")
def show_movie_details(movie_id):
    """Show the details of a specific movie."""

    movie = crud.get_movie_by_id(movie_id)

    return render_template("movie_details.html", movie=movie)

@app.route("/users")
def show_all_users():

    users = crud.get_all_users()

    return render_template("all_users.html", users=users)


@app.route("/users/<user_id>")
def show_user_profile(user_id):

    user = crud.get_user_by_id(user_id)
    ratings = crud.get_ratings_by_user_id(user_id)

    return render_template("user_profile.html", user=user, ratings=ratings)

@app.route("/users", methods=["POST"])
def register_user():
    """Create a new user."""

    email = request.form.get("email")
    password = request.form.get("password")

    user = crud.get_user_by_email(email)

    if user:
        flash('Email is already registered. Register with a different email or log in.')

    else:
        crud.create_user(email, password)
        flash('Your account has been created successfully.  Please log in.')

    return redirect("/")


if __name__ == "__main__":
    # DebugToolbarExtension(app)
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)
