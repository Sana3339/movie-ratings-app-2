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
    """View the homepage"""

    return render_template("homepage.html")

@app.route("/movies")
def show_all_movies():
    """View a list of all movies in the db"""

    movies = crud.get_all_movies()

    return render_template("movies.html", movies = movies)


if __name__ == "__main__":
    # DebugToolbarExtension(app)
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)
