"""CRUD operations."""

#imports code needed from other files and libraries
from model import db, User, Movie, Rating, connect_to_db

def create_user(email, password):
    """Creates and return a new user."""

    user = User(email = email, password = password)

    db.session.add(user)
    db.session.commit()

    return user


def get_all_users():
    """Returns all users in db."""

    return User.query.all()


def get_user_by_id(user_id):
    """Returns user details for a particular user id."""

    return User.query.get(user_id)


def get_ratings_by_user_id(user_id):
    """Returns all ratings for a particular user id."""

    return Rating.query.filter(Rating.user_id == user_id).all()


def get_user_by_email(email):
    """If an email exists in db, return user.  If not, returns None"""

    return User.query.filter(User.email == email).first()


def check_password_for_user(email,password):
    """Given an user's email, check if the password is correct. Returns True or False."""

    user = User.query.filter(User.email == email).first()

    if user.password == password:
        return True

    return False

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


def create_rating(user, movie, score):
    """Create and return a new rating."""

    rating = Rating(user=user, movie=movie, score=score)

    db.session.add(rating)
    db.session.commit()

    return rating


#Code below connects us to the db when we run crud.py interactively
if __name__ == '__main__':
    from server import app
    connect_to_db(app)