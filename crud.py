"""CRUD operations."""

#imports code needed from other files and libraries
from model import db, User, Movie, Rating, connect_to_db

def create_user(email, password):
    """Creates and return a new user."""

    user = User(email = email, password = password)

    db.session.add(user)
    db.session.commit()

    return user


def create_movie(title, overview, release_date, poster_path):
    """Create and return a new movie."""

    movie = Movie(title = title,
                overview = overview,
                release_date = release_date,
                poster_path = poster_path)

    db.session.add(movie)
    db.session.commit()

    return movie


def get_all_movies():
    """Returns all movies in the db."""

    return Movie.query.all()


def get_movie_by_id(movie_id):

    return Movie.query.get(movie_id)


def create_rating(score, movie, user):
    """Create and return a new rating."""

    rating = Rating(score = score,
                    movie = movie,
                    user = user)

    db.session.add(rating)
    db.session.commit()

    return rating


#Code below connects us to the db when we run crud.py interactively
if __name__ == '__main__':
    from server import app
    connect_to_db(app)