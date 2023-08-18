# inviteArr

A simple web-based tool designed to automate the backup and migration of user invites for Plex servers.

## Features

- **Backup Users**: Save a list of all your Plex users to a JSON file.
- **Invite Users**: Easily invite users to your Plex server, with support for dry-run mode to see the actions without actually inviting.
- **Mass Migrations**: Easily migrate between plex servers by importing a saved json configuration file between your servers.

## Setup & Installation

1. **Clone the Repository**:

   ```
   git clone https://github.com/your-github-username/plexInviter.git
   cd plexInviter
   ```

2. **Install Dependencies**:

   Assuming you have Python and pip installed:

   ```
   pip install -r requirements.txt
   ```

3. **Configuration**:

   Settings are stored in an INI file within the user’s home directory and can be overridden after importing plexapi by simply setting the value. See the documentation section ‘Configuration’ for more details on available options.

   ```
   [migration_options]
   dry_run = True

   [plexapi]
   container_size = 50
   timeout = 30

   [auth]
   myplex_username = xxx
   myplex_password = xxx
   server_baseurl = https://192.168.1.100:32400
   server_token = xxx

   ```

4. **Run the App**:

   ```
   python app.py
   ```

   Now, visit `http://127.0.0.1:5000/` in your web browser.

## Technologies Used

- **Flask**: To serve the web interface.
- **PlexAPI**: To communicate with Plex servers and manage users.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)
