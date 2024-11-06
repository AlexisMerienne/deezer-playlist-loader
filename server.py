import os
import re

import requests

from flask import Flask, request, redirect, session, g

import urllib.parse
from urllib.parse import parse_qs

import runner


app = Flask(__name__)
# Generate a random secret key for session management
app.secret_key = os.urandom(24)


@app.route('/')
def main():
    app_id = "668863"
    app_secret = "0e6390ee07e72b2b778197e06b374d34"
    my_url = "http://127.0.0.10:5001"

    music_genre = runner.get_music_genre()

    directory = 'data/' + music_genre["label"] + '/'
    print("[DBG] - directory :", directory)
    latest_file_path = get_latest_file_path(directory)
    if latest_file_path:
        track_ids = extract_track_ids_from_file(latest_file_path)

    code = request.args.get('code')

    if not code:
        session['state'] = os.urandom(16).hex()  # CSRF protection
        dialog_url = f"https://connect.deezer.com/oauth/auth.php?app_id={app_id}&redirect_uri={urllib.parse.quote(my_url)}&perms=email,offline_access,manage_library&state={session['state']}"
        return redirect(dialog_url)

    if request.args.get('state') == session.get('state'):
        token_url = f"https://connect.deezer.com/oauth/access_token.php?app_id={app_id}&secret={app_secret}&code={code}"
        response = requests.get(token_url)
        print("[DBG] - response :", response.content)
        print("[DBG] - response :", type(response.content))

        # Parse the URL-encoded string response to get the access token
        access_token_data = parse_qs(response.text)
        access_token = access_token_data.get('access_token', [None])[0]

        api_url = f"https://api.deezer.com/playlist/{music_genre['playlist_id']}/tracks?access_token={access_token}&request_method=POST&songs={track_ids}"
        response = requests.get(api_url)
        print("[DBG] - response :", response.content)
        if (response.status_code == 200 and response.content == b'true'):
            return "Successfully added the songs to the playlist."
        else:
            return "Failed to add the song to the playlist."
    else:
        return "The state does not match. You may be a victim of CSRF."


def get_latest_file_path(directory, prefix=''):
    """
    Get the path of the latest (most recent) file in a directory.
    """
    files = [f for f in os.listdir(directory) if f.startswith(prefix)]
    if not files:
        return None
    latest_file = max(files, key=lambda x: int(x.split('_')[0]))
    return os.path.join(directory, latest_file)


def extract_track_ids_from_file(file_path):
    """
    Extract track IDs from the Deezer URLs in the file.
    """
    track_ids = set()  # Use a set to store unique track IDs
    with open(file_path, 'r') as file:
        for line in file:
            # Extract the track ID from the URL
            match = re.search(r'track/(\d+)', line)
            if match:
                track_id = match.group(1)
                track_ids.add(track_id)  # Add track ID to the set
    # get size of the set
    print("[DBG] - track_ids :", len(track_ids))
    # Convert the set to a comma-separated string
    track_ids = (',').join(track_ids)
    return track_ids


if __name__ == '__main__':

    # runner.main()

    app.run(debug=True, host='127.0.0.10', port=5001)

    # webbrowser.open('http://127.0.0.10:5001')
