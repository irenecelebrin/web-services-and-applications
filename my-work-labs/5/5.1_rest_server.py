# Lab 5.1
# Date: 2026-03-01 
# create an application server that will implement a Restful API 

# import flask 
from flask import Flask, url_for, request, jsonify, redirect, abort

# create an instance of the flask class 
app = Flask(__name__)

# Get all recipes
# Test: curl *host*/recipes 
@app.route("/recipes", methods=["GET"])
def get_recipes():
    return 'All recipes are returned here'

# Get recipe by id 
# Test: curl *host*/recipes/1
@app.route("/recipes/<int:id>", methods=["GET"])
def get_recipe_by_id(id):
    return f'Recipe with id:{id} is returned'

# Create new recipe 
# Test: curl -X POST *host*/recipes  
@app.route("/recipes", methods=["POST"])
def create_recipes():
    jsonstring = request.json 
    return f'{jsonstring}' 

# Update a recipe
# Test: curl -X PUT *host*/recipes/1
@app.route("/recipes/<int:id>", methods=["PUT"])
def update_recipe(id):
    jsonstring = request.json
    return f'Recipe with id: {id} is updated to {jsonstring}'

# delete recipe
# Test: curl -X DELETE *host*/recipes/1
@app.route("/recipes/<int:id>", methods=["DELETE"])
def delete_recipe(id):
    return f'Recipe with id: {id} is deleted'


# run the application server 
app.run(debug=True)


if __name__ == "__main__":

    # run the application server 
    app.run(debug=True)


