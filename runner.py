import sys
import re

import requests
from utils import datetime_manager, constants, deezer_manager
from ytb_converter import download_from_ytb


def get_all_yesterday_songs(init_timestamp, base_url, all_playlists_tracks, download=False):
    # Get the timestamp for the previous day
    it_timestamp = init_timestamp

    # Initialize an empty list to store the song info
    songs_info = []

    print("[DBG] init_timestamp: ", init_timestamp)
    debug_new_tracks = []

    while datetime_manager.is_less_than_24h(init_timestamp, it_timestamp):
        # Append the song info to the list
        print("[DBG] it_timestamp: ", it_timestamp)
        it_timestamp = append_song_info(
            songs_info, it_timestamp, base_url, all_playlists_tracks, debug_new_tracks, download)
    print("[DBG] - debug_new_tracks : ", debug_new_tracks)

    return songs_info


def append_song_info(songs_info, timestamp, base_url, all_playlists_tracks, debug_new_tracks, download=False):

    # Define the URL for the GET request
    url = base_url + str(timestamp)

    # Send the GET request and store the response
    response = requests.get(url)

    # Parse the JSON content from the response
    data = response.json()

    # Iterate through each song in the response
    for song in data['songs']:
        # Initialize a variable to store the deezer link if found
        deezer_link = None
        # Check each link in the song's links
        for link in song['links']:
            # If a deezer link is found, store it and break the loop
            if link['label'] == 'deezer':
                deezer_link = link['url']
                break

        if not deezer_link:
            deezer_link = deezer_manager.find_track(
                song['secondLine'], song['firstLine'])
        # If a deezer link was found, create a tuple and add it to the list
        if deezer_link:
            match = re.search(r'track/(\d+)', deezer_link)
            debug_new_tracks.append(match.group(1))
            if match and (int(match.group(1)) not in all_playlists_tracks):
                title_artist = f"{song['secondLine']} - {song['firstLine']}"
                songs_info.append((title_artist, deezer_link))
            elif match:
                print("[DBG] - track already in playlist : ", match.group(1))
        else:
            print("[DBG] - no deezer link found for : ", song['secondLine'])
        if download:
            print("[DBG] - Downloading : ", song['secondLine'])
            download_from_ytb(song['secondLine'], song['firstLine'])

    return data['songs'][-1]['end']


def write_songs_info_to_file(songs_info, init_timestamp, label):
    # Create the file name using the init_timestamp
    file_name = f"data/{label}/{init_timestamp}_songs_info.txt"

    # Open the file in write mode
    with open(file_name, 'w') as file:
        # Iterate through each song info and write it to the file
        for song_info in songs_info:
            file.write(f"{song_info[0]} - {song_info[1]}\n")

    print(f"Successfully wrote songs info to {file_name}")


def get_music_genre():
    # Check if the argument is valid
    if len(sys.argv) < 2:
        print("Please provide a valid argument.")
        return

    argument = sys.argv[1]

    # Check if the argument is valid
    if argument not in constants.radio_map:
        print("Invalid argument.")
        return

    return constants.radio_map[argument]


def get_previous_days():
    if len(sys.argv) < 3:
        return 1
    return int(sys.argv[2].split("--")[1])


def main():
    # Read the command line argument
    music_genre = get_music_genre()
    previous_days = get_previous_days()
    all_playlists_tracks = deezer_manager.get_all_tracks_in_playlist(
        music_genre['playlist_id'])
    if (len(sys.argv) < 4):
        download = False
    else:
        download = (sys.argv[3] == "--download")
    init_timestamp = datetime_manager.get_previous_day_timestamp(previous_days)
    all_yesterday_songs = get_all_yesterday_songs(
        init_timestamp, music_genre['base_url'], all_playlists_tracks, download)

    # Call the function to write songs info to file
    write_songs_info_to_file(
        all_yesterday_songs, init_timestamp, music_genre['label'])


if __name__ == '__main__':
    main()
