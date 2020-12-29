import flask
from flask import request, jsonify
from main import get_recipes_by_name, get_recipes_by_name_filtered, get_recipes_by_ingredients

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
    recipes = get_recipes_by_name(search_name, num)
    return jsonify(recipes)


@app.route('/recipesByNameFiltered', methods=['POST'])
def search_by_name_with_filter():
    req_data = request.get_json()
    search_name = req_data['name']
    num = req_data['num']
    include = req_data['include']
    exclude = req_data['exclude']
    recipes = get_recipes_by_name_filtered(search_name, num, include, exclude)
    return jsonify(recipes)


@app.route('/recipesByIngredients', methods=['POST'])
def search_by_ingredients():
    req_data = request.get_json()
    num = req_data['num']
    include = req_data['include']
    exclude = req_data['exclude']
    recipes = get_recipes_by_ingredients(num, include, exclude)
    return jsonify(recipes)


app.run()
