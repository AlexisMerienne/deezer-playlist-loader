from ytmusicapi import YTMusic
from yt_dlp import YoutubeDL


def download_from_ytb(title, artist):
    yt = YTMusic()
    search_results = yt.search("{title} - {artist}".format(
        title=title, artist=artist), filter="songs")
    id = search_results[0]['videoId']

    URLS = ['https://www.youtube.com/watch?v={id}'.format(id=id)]

    ydl_opts = {
        'format': 'wav/bestaudio/best',
        'outtmpl': 'downloads/%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'wav',
            'preferredquality': '192',
        }],
    }

    with YoutubeDL(ydl_opts) as ydl:
        ydl.download(URLS)


if __name__ == "__main__":
    download_from_ytb("Blinding Lights", "The Weeknd")
