import requests


def find_track(title, artist):

    title = title.split("(feat")[0]

    query = "https://api.deezer.com/search?q={title}-{artist}".format(
        title=title, artist=artist)

    try:
        response = requests.get(query)
        response_json = response.json()
    except ValueError:
        return None

    if 'error' in response_json:
        return None

    if len(response_json['data']) > 0 and response_json['data'][0]['title'].lower() == title.lower():
        return response_json['data'][0]['link']

    return None


def get_all_tracks_in_playlist(playlist_id):
    '''
    API response is 25 tracks per page, need to loop through all pages to get all tracks
    '''

    tracks = []
    url = f"https://api.deezer.com/playlist/{playlist_id}/tracks"

    def get_tracks(url):
        response = requests.get(url)
        data = response.json()
        for track in data['data']:
            tracks.append(int(track['id']))
        if 'next' in data:
            get_tracks(data['next'])

    get_tracks(url)

    return tracks
