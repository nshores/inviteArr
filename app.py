from flask import Flask, render_template, request, jsonify
from inviteArr import plexMigrationTools

USERNAME = ""
PASSWORD = ""
SERVER = ""
TOKEN = ""
PLEX_SERVER = ""
DRY_RUN = True


app = Flask(__name__)

migration = plexMigrationTools(
    USERNAME,
    PASSWORD,
    SERVER,
    TOKEN,
    PLEX_SERVER,
)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/getUsers", methods=["GET"])
def get_users():
    users = migration.getUsers()
    return render_template("users.html", users=users)


@app.route("/backup", methods=["GET"])
def backup():
    migration.backupPlex()
    return "Backup done!"


@app.route("/invitePage", methods=["GET"])
def invite_page():
    return render_template("invite.html")


@app.route("/invite", methods=["POST"])
def invite_user():
    email = request.form.get("email")
    if not email:
        return "Email is required!", 400
    migration.inviteUser(email)
    return f"Invitation sent to {email}!"


if __name__ == "__main__":
    app.run(debug=True)
