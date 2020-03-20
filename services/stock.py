#from services import root_dir, nice_json
from flask import Flask
from werkzeug.exceptions import NotFound
import json
import os
from flask import make_response

app = Flask(__name__)

def root_dir():
    """ Returns root director for this project """
    return os.path.dirname(os.path.realpath(__file__ + '/..'))


def nice_json(arg):
    response = make_response(json.dumps(arg, sort_keys = True, indent=4))
    response.headers['Content-type'] = "application/json"
    return response

with open("{}/database/stock.json".format(root_dir()), "r") as f:
    stocks = json.load(f)


@app.route("/", methods=['GET'])
def hello_ingredients():
    return nice_json({
        "uri": "/",
        "subresource_uris": {
            "stocks": "/stocks",
            "stock": "/stock/<id>"
        }
    })

@app.route("/stocks", methods=['GET'])
def stock_all():
    return nice_json(stocks)


@app.route("/stocks/<stockid>", methods=['GET'])
def stock(stockid):
    if stockid not in stocks:
        raise NotFound

    result = stocks[stockid]
    result["uri"] = "/stocks/{}".format(stockid)

    return nice_json(result)


if __name__ == "__main__":
    app.run(port=5001, debug=True)

