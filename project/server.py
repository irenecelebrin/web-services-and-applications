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


# ── REST API routes ─────────────────────────────────────────────────────────

# GET /persons — members page; also returns JSON when Accept: application/json
@app.route("/persons", methods=["GET"])
def api_get_all():
    if "application/json" in request.headers.get("Accept", ""):
        return jsonify(get_all())
    return send_from_directory("FE/templates", "members.html")


# GET    /person/<id> — member detail page; also returns JSON when Accept: application/json
# PUT    /person/<id> — partial update (JSON body); returns updated member
# DELETE /person/<id> — delete a member
@app.route("/person/<int:id>", methods=["GET", "PUT", "DELETE"])
def api_get_one(id):
    if request.method == "PUT":
        if get_by_id(id) is None:
            return _json_error(f"Person with id {id} not found", 404)
        payload = request.get_json(silent=True) or {}
        payload = {k: (v.strip() if isinstance(v, str) else v) or None for k, v in payload.items()}
        return jsonify(update(id, payload))

    if request.method == "DELETE":
        if not delete(id):
            return _json_error(f"Person with id {id} not found", 404)
        return jsonify({"deleted": id})

    if "application/json" in request.headers.get("Accept", ""):
        member = get_by_id(id)
        if member is None:
            return _json_error(f"Person with id {id} not found", 404)
        return jsonify(member)
    return send_from_directory("FE/templates", "member.html")

# GET /persons/surname/<value> — filtered members page; also returns JSON when Accept: application/json
@app.route("/persons/surname/<value>", methods=["GET"])
def api_search_surname(value):
    if "application/json" in request.headers.get("Accept", ""):
        return jsonify(get_by_surname(value))
    return send_from_directory("FE/templates", "members.html")


# GET /persons/email/<value> — filtered members page; also returns JSON when Accept: application/json
@app.route("/persons/email/<value>", methods=["GET"])
def api_search_email(value):
    if "application/json" in request.headers.get("Accept", ""):
        return jsonify(get_by_email(value))
    return send_from_directory("FE/templates", "members.html")


# GET /form  — add/edit member page
# POST /form — create a new member (JSON body); returns 201 on success
@app.route("/form", methods=["GET", "POST"])
def form_page():
    if request.method == "POST":
        payload = request.get_json(silent=True) or {}
        payload = {k: (v.strip() if isinstance(v, str) else v) or None for k, v in payload.items()}

        missing = [f for f in REQUIRED_CREATE_FIELDS if not payload.get(f)]
        if missing:
            return _json_error(f"Missing required fields: {', '.join(missing)}", 400)

        new_member = create(payload)
        return jsonify(new_member), 201
    return send_from_directory("FE/templates", "form.html")



# ── HTML page routes (serve static files) ──────────────────────────────────

@app.route("/")
def index():
    return send_from_directory("FE/templates", "index.html")



@app.route("/gallery/<path:filename>")
def gallery(filename):
    return send_from_directory("FE/gallery", filename)


# ── Main ──────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    app.run(debug=True)
