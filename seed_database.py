"""Seeding database."""

import os
import json
from random import choice, randint
from datetime import datetime

import crud
import model
import server

os.system('dropdb ratings')
os.system('createdb ratings')

#connect to database
model.connect_to_db(server.app)
model.db.create_all()

#Load movie data from JSON file
with open('data/movies.json') as f:
    movie_data = json.loads(f.read())

#Create movies, store them in list to be used to later create fake ratings
movies_in_db = []

for movie in movie_data:

    title, overview, poster_path = (movie["title"],
                                    movie["overview"],
                                    movie["poster_path"])

    release_date = datetime.strptime(movie["release_date"], "%Y-%m-%d")

    db_movie = crud.create_movie(title, overview, release_date, poster_path)
    movies_in_db.append(db_movie)


#Create fake users with unique email addresses.
#For each user, generate 10 fake movie ratings

for n in range(10):
    email = f'user{n}@test.com'
    password = 'test'

    user = crud.create_user(email, password)

    for n in range(10):

        score = randint(1,5)
        movie = choice(movies_in_db)

        db_rating = crud.create_rating(score, movie, user)
