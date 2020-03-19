

APIs and Documentation
======================

## Recipes Service (port 5000)

This service is used to get the recipe for dishes in the database. 

To lookup all movies in the database, hit: `http://127.0.0.1:5000/recipes`


    GET /recipes
    Returns a list of all recipes.


To lookup a movie by its `id`:

    GET / recipes / pancakes
    http://127.0.0.1:5000/recipes
    Returns the specified movie.
    
        {
            "course": "main course",
            "ingredients": [
                {
                    "id": "wheat flour",
                    "quantity": 300,
                    "unit": "grams"
                },
                {
                    "id": "salt",
                    "quantity": 1,
                    "unit": "teaspoon"
                },
                {
                    "id": "egg",
                    "quantity": 2,
                    "unit": "pieces"
                },
                {
                    "id": "milk",
                    "quantity": 500,
                    "unit": "milliliters"
                },
                {
                    "id": "butter",
                    "quantity": 30,
                    "unit": "grams"
                }
            ],
            "name": "pancakes",
            "portions": 8
        }
## Stock Service (port 5001)

This service is used get a list of all stocks.

To lookup all stocks, go to: `http://127.0.0.1:5001/stocks`


    GET /stocks
    Returns a list of all current stocks


To get the stock for a specific product:

    GET /stocks/egg
    Returns the amount of items in stocks for a product

    {
        "id": "egg",
        "quantity in stock": 6,
        "title": "eggs",
        "unit": "pieces",
        "uri": "/stocks/egg"
    }

## Model to chat

services / train_chatbot

Trains neural network to make a simple chatbot

Needs more categories, work and training data etc to properly work


Concept would work if APIs are connected
