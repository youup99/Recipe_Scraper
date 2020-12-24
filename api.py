import flask
from flask import request, jsonify
from main import getRecipes

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<h1>Test</h1>"


@app.route('/recipes', methods=['GET'])
def api():
    search_name = request.args.get('searchName')
    num = request.args.get('num')
    recipes = getRecipes(search_name, int(num))
    return jsonify(recipes)


app.run()
