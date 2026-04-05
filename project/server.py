# Flask endpoint 

# import flask 
from flask import Flask, url_for, request, jsonify, redirect, abort
from recipe_dao import get_all, get_by_id, create, update, delete


# create an instance of the flask class 
app = Flask(__name__)

# Index 
# Test: curl *host*/
@app.route("/", methods=["GET"])
def index():
    return 'Welcome to the API'

# Get all items
# Test: curl *host*/items 
@app.route("/recipes", methods=["GET"])
def get_all_recipes():
    return jsonify(get_all())

# Get item by id
# Test: curl *host*/items/1
@app.route("/recipes/<int:id>", methods=["GET"])
def get_recipe_by_id(id):
    return jsonify(get_by_id(id))

# Create new item
# Test: curl -X POST *host*/items  
@app.route("/items", methods=["POST"])
def create_items():
    jsonstring = request.json 
    return f'{jsonstring}'

# Update a item
# Test: curl -X PUT *host*/items/1  
@app.route("/items/<int:id>", methods=["PUT"])
def update_item(id):
    jsonstring = request.json
    return f'Item with id: {id} is updated to {jsonstring}'


# Delete item
# Test: curl -X DELETE *host*/items/1
@app.route("/items/<int:id>", methods=["DELETE"])
def delete_item(id):
    return f'Item with id: {id} is deleted'

if __name__ == "__main__":

    # run the application server 
    app.run(debug=True)
