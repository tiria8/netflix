import json
import sqlite3
from collections import Counter

def get_by_title(title):
    with sqlite3.connect('netflix.db') as connection:
        cursor = connection.cursor()
        query = f"SELECT title, country, release_year, listed_in, description FROM netflix WHERE title LIKE '%{title}%' ORDER BY release_year DESC"
        cursor.execute(query)
        data = cursor.fetchone()

        film = {
            "title": data[0],
            "country": data[1],
            "release_year": data[2],
            "listed_in": data[3],
            "description": data[4]
        }

        return film

def get_by_year(year_1, year_2):
    with sqlite3.connect('netflix.db') as connection:
        cursor = connection.cursor()
        query = f"SELECT title, release_year FROM netflix WHERE release_year BETWEEN {year_1} AND {year_2} LIMIT 10"
        cursor.execute(query)
        data = cursor.fetchall()

        films = []
        for film in data:
            film = {
                "title": film[0],
                "release_year": film[1]
            }
            films.append(film)

        return films

def rating_children():
    with sqlite3.connect('netflix.db') as connection:
        cursor = connection.cursor()
        query = f"SELECT title, rating, description FROM netflix WHERE rating='G'"
        cursor.execute(query)
        data = cursor.fetchall()

        films = []
        for film in data:
            film = {
                "title": film[0],
                "rating": film[1],
                "description": film[2]
            }
            films.append(film)

        return films

def rating_family():
    with sqlite3.connect('netflix.db') as connection:
        cursor = connection.cursor()
        query = f"SELECT title, rating, description FROM netflix WHERE rating='G' OR  rating='PG' OR rating='PG-13'"
        cursor.execute(query)
        data = cursor.fetchall()

        films = []
        for film in data:
            film = {
                "title": film[0],
                "rating": film[1],
                "description": film[2]
            }
            films.append(film)

        return films

def rating_adult():
    with sqlite3.connect('netflix.db') as connection:
        cursor = connection.cursor()
        query = f"SELECT title, rating, description FROM netflix WHERE rating='R' OR  rating='NC-17'"
        cursor.execute(query)
        data = cursor.fetchall()

        films = []
        for film in data:
            film = {
                "title": film[0],
                "rating": film[1],
                "description": film[2]
            }
            films.append(film)

        return films

def get_by_genre(genre):
    with sqlite3.connect('netflix.db') as connection:
        cursor = connection.cursor()
        query = f"SELECT title, description FROM netflix WHERE listed_in LIKE '%{genre}%' ORDER BY release_year DESC LIMIT 10"
        cursor.execute(query)
        data = cursor.fetchall()

        films = []
        for film in data:
            film = {
                "title": film[0],
                "description": film[1]
            }
            films.append(film)

        return films

def get_by_actor(actor_1, actor_2):
    with sqlite3.connect('netflix.db') as connection:
        cursor = connection.cursor()
        query = f"SELECT COUNT(netflix.cast), `cast` FROM netflix WHERE `cast` LIKE '%{actor_1}%' AND `cast` LIKE '%{actor_2}%' GROUP BY `cast`"
        cursor.execute(query)

        data = cursor.fetchall()
        all_actors = []
        for i in data:
            all_actors.extend(i[1].split(', '))

        repeated_actors = []

        for i in all_actors:
            if i == actor_1 or i == actor_2 and all_actors.count(i) <= 2:
                continue
            repeated_actors.append(i)
        return repeated_actors

def get_film(type, release_year, genre):
    with sqlite3.connect('netflix.db') as connection:
        cursor = connection.cursor()
        query = f"SELECT title, description FROM netflix WHERE type='{type}' AND release_year='{release_year}' AND listed_in LIKE '%{genre}%' "
        cursor.execute(query)

        return cursor.fetchall()
