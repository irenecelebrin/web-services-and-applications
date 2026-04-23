# Flask endpoint

from flask import Flask, request, jsonify, abort

from person_dao import (
    get_all,
    get_by_id,
    get_by_surname,
    get_by_email,
    create,
    update,
    delete,
)

# required fields when creating a new member (per planning/plan.md §2)
REQUIRED_CREATE_FIELDS = (
    "name",
    "last_name",
    "phone",
    "email",
    "emergency_contact_name",
    "emergency_contact_phone",
)

app = Flask(__name__)


# Index
# Test: curl *host*/
@app.route("/", methods=["GET"])
def index():
    return "Welcome to the API"


# Get all persons
# Test: curl *host*/persons
@app.route("/persons", methods=["GET"])
def get_all_persons():
    return jsonify(get_all())


# Get item by id
# Test: curl *host*/persons/1
@app.route("/persons/<int:id>", methods=["GET"])
def get_person_by_id(id):
    person = get_by_id(id)
    if person is None:
        abort(404, description=f"Person with id {id} not found")
    return jsonify(person)


# Get persons by surname (case-insensitive exact match)
# Test: curl *host*/persons/surname/Smith
@app.route("/persons/surname/<value>", methods=["GET"])
def get_persons_by_surname(value):
    return jsonify(get_by_surname(value))


# Get persons by email (case-insensitive exact match)
# Test: curl *host*/persons/email/foo@bar.com
@app.route("/persons/email/<value>", methods=["GET"])
def get_persons_by_email(value):
    return jsonify(get_by_email(value))


# Create new item
# Test: curl -X POST -H "Content-Type: application/json" -d '{...}' *host*/persons
@app.route("/persons", methods=["POST"])
def create_persons():
    payload = request.get_json(silent=True) or {}
    missing = [
        field
        for field in REQUIRED_CREATE_FIELDS
        if payload.get(field) in (None, "")
    ]
    if missing:
        abort(400, description=f"missing fields: {', '.join(missing)}")
    return jsonify(create(payload)), 201


# Update an item
# Test: curl -X PUT -H "Content-Type: application/json" -d '{...}' *host*/persons/1
@app.route("/persons/<int:id>", methods=["PUT"])
def update_item(id):
    payload = request.get_json(silent=True) or {}
    updated = update(id, payload)
    if updated is None:
        abort(404, description=f"Person with id {id} not found")
    return jsonify(updated)


# Delete item
# Test: curl -X DELETE *host*/persons/1
@app.route("/persons/<int:id>", methods=["DELETE"])
def delete_item(id):
    if not delete(id):
        abort(404, description=f"Person with id {id} not found")
    return ("", 204)


if __name__ == "__main__":
    app.run(debug=True)
