# Flask server — JSON API routes + HTML UI routes

from flask import Flask, request, jsonify, abort, render_template, redirect, url_for, send_from_directory

from person_dao import (
    get_all,
    get_by_id,
    get_by_surname,
    get_by_email,
    create,
    update,
    delete,
)

# required fields when creating a new member
REQUIRED_CREATE_FIELDS = (
    "name",
    "last_name",
    "phone",
    "email",
    "emergency_contact_name",
    "emergency_contact_phone",
)

# Point Flask to the templates and static files inside the FE folder
app = Flask(__name__, template_folder="FE/templates", static_folder="FE/static")


# Landing page
@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


# Serve images from FE/gallery/ so templates can reference them via url_for('gallery', ...)
@app.route("/gallery/<path:filename>")
def gallery(filename):
    return send_from_directory("FE/gallery", filename)


# ── Members list ───────────────────────────────────────────────────────────

# GET /persons — render the HTML members table
# curl *host*/persons  →  returns the members list page
@app.route("/persons", methods=["GET"])
def get_all_persons():
    return render_template("members.html", members=get_all())


# ── Member detail ──────────────────────────────────────────────────────────

# GET /persons/<id> — render the HTML detail card for one member
# curl *host*/persons/1
@app.route("/persons/<int:id>", methods=["GET"])
def get_person_by_id(id):
    member = get_by_id(id)
    if member is None:
        abort(404, description=f"Person with id {id} not found")
    return render_template("member.html", member=member)


# ── Add member ─────────────────────────────────────────────────────────────

# GET /persons/new — show an empty add-member form
@app.route("/persons/new", methods=["GET"])
def new_member_form():
    return render_template("form.html", member=None, error=None)


# POST /persons — process the add-member form; redirect to the new member's page
@app.route("/persons", methods=["POST"])
def create_persons():
    payload = request.form.to_dict()
    # strip whitespace; treat empty strings as missing so validation catches them
    payload = {k: (v.strip() or None) for k, v in payload.items()}

    missing = [f for f in REQUIRED_CREATE_FIELDS if not payload.get(f)]
    if missing:
        error = f"Please fill in: {', '.join(missing).replace('_', ' ')}"
        return render_template("form.html", member=None, error=error), 400

    new_member = create(payload)
    return redirect(url_for("get_person_by_id", id=new_member["id"]))


# ── Edit member ────────────────────────────────────────────────────────────

# GET /persons/<id>/edit — show the edit form pre-filled with existing data
@app.route("/persons/<int:id>/edit", methods=["GET"])
def edit_member_form(id):
    member = get_by_id(id)
    if member is None:
        abort(404, description=f"Person with id {id} not found")
    return render_template("form.html", member=member, error=None)


# POST /persons/<id>/edit — process the edit form; redirect to the detail page
@app.route("/persons/<int:id>/edit", methods=["POST"])
def edit_member(id):
    if get_by_id(id) is None:
        abort(404, description=f"Person with id {id} not found")

    payload = request.form.to_dict()
    # strip whitespace; leave optional fields as None so the DAO skips them
    payload = {k: (v.strip() or None) for k, v in payload.items()}

    updated = update(id, payload)
    return redirect(url_for("get_person_by_id", id=updated["id"]))


# ── Delete member ──────────────────────────────────────────────────────────

# POST /persons/<id>/delete — delete member then redirect to the members list
# (HTML forms only support GET/POST, so we use POST instead of DELETE)
@app.route("/persons/<int:id>/delete", methods=["POST"])
def delete_member(id):
    if not delete(id):
        abort(404, description=f"Person with id {id} not found")
    return redirect(url_for("get_all_persons"))


# ── Search routes (return JSON) ────────────────────────────────────────────

# GET /persons/surname/<value> — case-insensitive surname search
# curl *host*/persons/surname/Smith
@app.route("/persons/surname/<value>", methods=["GET"])
def get_persons_by_surname(value):
    return jsonify(get_by_surname(value))


# GET /persons/email/<value> — case-insensitive email search
# curl *host*/persons/email/foo@bar.com
@app.route("/persons/email/<value>", methods=["GET"])
def get_persons_by_email(value):
    return jsonify(get_by_email(value))


if __name__ == "__main__":
    app.run(debug=True)
