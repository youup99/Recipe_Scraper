import flask
from flask import request, jsonify
from main import getRecipesByName, getRecipesByNameFiltered, getRecipesByIngredients

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<h1>Recipe Scraper</h1>"


@app.route('/recipesByName', methods=['POST'])
def search_by_name():
    req_data = request.get_json()
    search_name = req_data['name']
    num = req_data['num']
    recipes = getRecipesByName(search_name, num)
    return jsonify(recipes)


@app.route('/recipesByNameFiltered', methods=['POST'])
def search_by_name_with_filter():
    req_data = request.get_json()
    search_name = req_data['name']
    num = req_data['num']
    include = req_data['include']
    exclude = req_data['exclude']
    recipes = getRecipesByNameFiltered(search_name, num, include, exclude)
    return jsonify(recipes)


@app.route('/recipesByIngredients', methods=['POST'])
def search_by_ingredients():
    req_data = request.get_json()
    num = req_data['num']
    include = req_data['include']
    exclude = req_data['exclude']
    recipes = getRecipesByIngredients(num, include, exclude)
    return jsonify(recipes)


app.run()
