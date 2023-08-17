# inviteArr

A simple web-based tool designed to automate the backup and migration of user invites for Plex servers.

## Features

- **Login to Plex**: Uses the PlexAPI to log into your Plex account.
- **Backup Users**: Save a list of all your Plex users to a JSON file.
- **Invite Users**: Easily invite users to your Plex server, with support for dry-run mode to see the actions without actually inviting.
- ** Mass Migrations between plex servers

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

   Modify the config parameters in `plexInviter.py` with your Plex server details:

   ```python
   USERNAME = "YOUR_PLEX_USERNAME"
   PASSWORD = "YOUR_PLEX_PASSWORD"
   SERVER = "YOUR_PLEX_SERVER"
   TOKEN = "YOUR_PLEX_API_TOKEN"
   PLEX_SERVER = "YOUR_PLEX_SERVER_URL"
   ```

4. **Run the App**:

   ```
   python app.py
   ```

   Now, visit `http://127.0.0.1:5000/` in your web browser.

## Screenshots

(Include a few screenshots of the application to provide a visual. You can host these images on GitHub and link them here.)

## Technologies Used

- **Python**: For the backend logic and server.
- **Flask**: To serve the web interface.
- **PlexAPI**: To communicate with Plex servers and manage users.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)

---

Make sure to modify the placeholders like `https://github.com/your-github-username/plexInviter.git` with your actual GitHub repository link. Also, it's always good to include screenshots as they provide a quick look into what the application does.
