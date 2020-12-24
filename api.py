import flask
from flask import request, jsonify
from main import getRecipes

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<h1>Recipe Scraper</h1>"


@app.route('/recipes', methods=['POST'])
def search():
    req_data = request.get_json()
    search_name = req_data['name']
    num = req_data['num']
    recipes = getRecipes(search_name, num)
    return jsonify(recipes)


app.run()
