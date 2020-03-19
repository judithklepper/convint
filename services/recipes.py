# import root_dir, nice_json
from flask import Flask
from werkzeug.exceptions import NotFound, ServiceUnavailable
import json
import requests

import os
import json
from flask import make_response
from flask import request


def root_dir():
    """ Returns root director for this project """
    return os.path.dirname(os.path.realpath(__file__ + '/..'))


def nice_json(arg):
    response = make_response(json.dumps(arg, sort_keys=True, indent=4))
    response.headers['Content-type'] = "application/json"
    return response


app = Flask(__name__)

with open("{}/database/recipes.json".format(root_dir()), "r") as f:
    recipes = json.load(f)


@app.route("/", methods=['GET'])
def hello_recipes():
    return nice_json({
        "uri": "/",
        "subresource_uris": {
            "recipes": "/recipes",
            "recipe": "/recipe/<recipename>"
        }
    })


@app.route("/recipes", methods=['GET'])
def recipe_list():
    return nice_json(recipes)


@app.route("/recipes/<recipename>", methods=['GET'])
def recipe_record(recipename):
    if recipename not in recipes:
        raise NotFound

    return nice_json(recipes[recipename])


@app.route("/query/<naam>", methods=['GET'])
def query(naam):
    zoek1 = {k1: v1 for k1, v1 in recipes.items()}
    zoek2 = {k2: v2 for k2, v2 in zoek1.items() if naam in v2['ingredients']}
    return nice_json(zoek2)


if __name__ == "__main__":
    app.run(port=5000, debug=True)
