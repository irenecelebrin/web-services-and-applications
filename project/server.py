# Flask endpoint 

# import flask 
from flask import Flask, url_for, request, jsonify, redirect, abort
from person_dao import get_all, get_by_id, create, update, delete


# create an instance of the flask class 
app = Flask(__name__)

# Index 
# Test: curl *host*/
@app.route("/", methods=["GET"])
def index():
    return 'Welcome to the API'

# Get all persons
# Test: curl *host*/persons 
@app.route("/persons", methods=["GET"])
def get_all_persons():
    return jsonify(get_all())

# Get item by id
# Test: curl *host*/persons/1
@app.route("/persons/<int:id>", methods=["GET"])
def get_person_by_id(id):
    return jsonify(get_by_id(id))

# Create new item
# Test: curl -X POST *host*/persons  
@app.route("/persons", methods=["POST"])
def create_persons():
    jsonstring = request.json 
    return f'{jsonstring}'

# Update a item
# Test: curl -X PUT *host*/persons/1  
@app.route("/persons/<int:id>", methods=["PUT"])
def update_item(id):
    jsonstring = request.json
    return f'Item with id: {id} is updated to {jsonstring}'


# Delete item
# Test: curl -X DELETE *host*/persons/1
@app.route("/persons/<int:id>", methods=["DELETE"])
def delete_item(id):
    return f'Item with id: {id} is deleted'

if __name__ == "__main__":

    # run the application server 
    app.run(debug=True)
