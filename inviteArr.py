from plexapi.server import PlexServer
from plexapi.settings import Settings
import json
import logging
import os
import requests
import sys

logging.basicConfig(level=logging.INFO)


class plexMigrationTools:
    def __init__(self, username, password, server, token, plex_server, dry_run=True):
        self.USERNAME = username
        self.PASSWORD = password
        self.SERVER = server
        self.TOKEN = token
        self.PLEX_SERVER = plex_server
        self.DRY_RUN = dry_run

        self.plex = self.plexLogin()

    def plexLogin(self):
        # logging.info("Logging into Plex Account")
        # try:
        #     account = MyPlexAccount(self.USERNAME, self.PASSWORD)
        # except Exception as error:
        #     logging.error("Error Logging into Plex Account %s", error)
        #     sys.exit(1)

        logging.info("Connecting to Plex Server...")
        session = requests.Session()
        session.verify = False
        try:
            plex = PlexServer(self.PLEX_SERVER, self.TOKEN, session)
        except Exception as error:
            logging.error("Error connecting to Plex Server: %s", error)
            sys.exit(1)

        return plex

    def getUsers(self):
        users = self.plex.myPlexAccount().users()
        user_list = []
        for user in users:
            user_detail = {
                "id": user.id,
                "title": user.title,
                "email": user.email,
                "username": user.username,
            }
            user_list.append(user_detail)
        return user_list

    def backupPlex(self):
        logging.info("Backing up user list to %s", os.getcwd())
        with open("plex_users_backup.json", "w") as outfile:
            users = self.getUsers()
            json.dump(users, outfile, indent=4)

    def inviteUser(self, UserToInvite):
        sections = self.plex.library.sections()
        # get all sections by default
        sec_list = []
        for sec in sections:
            sec_list.append(sec.title)
        try:
            invite = self.plex.myPlexAccount().inviteFriend(
                UserToInvite, self.plex, sections=sec_list
            )
        except Exception as error:
            logging.error("General error inviting user: %s", error)


# if __name__ == "__main__":
#     migration = plexMigrationTools(
#         USERNAME,
#         PASSWORD,
#         SERVER,
#         TOKEN,
#         PLEX_SERVER,
#     )
#     migration.backupPlex()

# # TODO - Create function for actual migration process
# users = migration.getUsers()
# for user in users:
#     if migration.DRY_RUN:
#         logging.info("--Dry run mode --")
#         logging.info(f"Inviting {user['email']}")
#     else:
#         logging.info(f"Inviting {user['email']}")
#         migration.inviteUser(user["email"])
