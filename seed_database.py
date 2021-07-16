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
    movies_in_db.append(movie)


#Create fake users with unique email addresses.
#For each fake user, generate 10 fake ratings for the user

for n in range(10):
    email = f'user{n}@test.com'
    password = 'test'

    for n in range(10):


#Choose a random movie and generate a random score for the movie
