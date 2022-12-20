from flask import Flask, jsonify
from utils import get_film, get_by_year, get_by_actor, get_by_genre, get_by_title, rating_adult, rating_family, rating_children


app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route("/movie/<title>")
def get_film_by_title(title):
    film = jsonify(get_by_title(title))
    return film

@app.route("/movie/<int:year_1>/to/<int:year_2>")
def get_films_by_year(year_1, year_2):
    films = get_by_year(year_1, year_2)
    return jsonify(films)

@app.route("/rating/children")
def films_children():
    films = rating_children()
    return jsonify(films)

@app.route("/rating/family")
def films_family():
    films = rating_family()
    return jsonify(films)

@app.route("/rating/adult")
def films_adult():
    films = rating_adult()
    return jsonify(films)

@app.route("/genre/<genre>")
def get_films_by_genre(genre):
    films = get_by_genre(genre)
    return jsonify(films)




if __name__=="__main__":
    app.run(debug=True)