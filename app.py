from flask import Flask, render_template, request, jsonify
from inviteArr import plexMigrationTools
from plexapi import config
import os
import logging

if os.getenv("PLEXAPI_CONFIG_PATH"):
    pass
else:
    PLEXAPI_CONFIG_PATH = os.getcwd() + "/config.ini"

running_config = config.PlexConfig(PLEXAPI_CONFIG_PATH)
dry_run_value = running_config.data["migration_options"]["dry_run"].lower() == "true"


app = Flask(__name__)

migration = plexMigrationTools(
    running_config.data["auth"]["myplex_username"],
    running_config.data["auth"]["myplex_password"],
    running_config.data["auth"]["server_baseurl"],
    running_config.data["auth"]["server_token"],
    running_config.data["auth"]["server_baseurl"],
    dry_run_value,
)

print(migration.DRY_RUN)
if migration.DRY_RUN == True:
    logging.info("I'm in the main app and Dry Run is enabled")

if migration.DRY_RUN == False:
    logging.info("I'm in the main app and Dry Run is disabled")


@app.route("/")
def index():
    current_server = migration.PLEX_SERVER
    return render_template("index.html", current_server=current_server)


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
