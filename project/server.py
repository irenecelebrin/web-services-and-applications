# Flask server — REST API (JSON) + static HTML page routes

from flask import Flask, request, jsonify, send_from_directory

from person_dao import (
    get_all,
    get_by_id,
    get_by_surname,
    get_by_email,
    create,
    update,
    delete,
)

REQUIRED_CREATE_FIELDS = (
    "name",
    "last_name",
    "phone",
    "email",
    "emergency_contact_name",
    "emergency_contact_phone",
)

app = Flask(__name__, static_folder="FE/static")


def _json_error(message, status):
    return jsonify({"error": message}), status


# ── HTML page routes (serve static files) ──────────────────────────────────

@app.route("/")
def index():
    return send_from_directory("FE/templates", "index.html")


@app.route("/members")
def members_page():
    return send_from_directory("FE/templates", "members.html")


@app.route("/member")
def member_page():
    return send_from_directory("FE/templates", "member.html")


@app.route("/form")
def form_page():
    return send_from_directory("FE/templates", "form.html")


@app.route("/gallery/<path:filename>")
def gallery(filename):
    return send_from_directory("FE/gallery", filename)


# ── REST API routes ─────────────────────────────────────────────────────────

# GET /api/persons — list all members
@app.route("/api/persons", methods=["GET"])
def api_get_all():
    return jsonify(get_all())


# GET /api/persons/<id> — get one member
@app.route("/api/persons/<int:id>", methods=["GET"])
def api_get_one(id):
    member = get_by_id(id)
    if member is None:
        return _json_error(f"Person with id {id} not found", 404)
    return jsonify(member)


# POST /api/persons — create a new member (JSON body); returns 201 on success
@app.route("/api/persons", methods=["POST"])
def api_create():
    payload = request.get_json(silent=True) or {}
    payload = {k: (v.strip() if isinstance(v, str) else v) or None for k, v in payload.items()}

    missing = [f for f in REQUIRED_CREATE_FIELDS if not payload.get(f)]
    if missing:
        return _json_error(f"Missing required fields: {', '.join(missing)}", 400)

    new_member = create(payload)
    return jsonify(new_member), 201


# PUT /api/persons/<id> — partial update (JSON body); returns updated member
@app.route("/api/persons/<int:id>", methods=["PUT"])
def api_update(id):
    if get_by_id(id) is None:
        return _json_error(f"Person with id {id} not found", 404)

    payload = request.get_json(silent=True) or {}
    payload = {k: (v.strip() if isinstance(v, str) else v) or None for k, v in payload.items()}

    updated = update(id, payload)
    return jsonify(updated)


# DELETE /api/persons/<id> — delete a member
@app.route("/api/persons/<int:id>", methods=["DELETE"])
def api_delete(id):
    if not delete(id):
        return _json_error(f"Person with id {id} not found", 404)
    return jsonify({"deleted": id})


# GET /api/persons/surname/<value> — search by surname (case-insensitive)
@app.route("/api/persons/surname/<value>", methods=["GET"])
def api_search_surname(value):
    return jsonify(get_by_surname(value))


# GET /api/persons/email/<value> — search by email (case-insensitive)
@app.route("/api/persons/email/<value>", methods=["GET"])
def api_search_email(value):
    return jsonify(get_by_email(value))


if __name__ == "__main__":
    app.run(debug=True)
