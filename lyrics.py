import os
import requests

MUSIXMATCH_API_KEY = os.environ["MUSIXMATCH_API_KEY"]
MUSIXMATCH_API_URL = "https://api.musixmatch.com/ws/1.1/"
MUSIXMATCH_LYRICS_URL = MUSIXMATCH_API_URL + "matcher.lyrics.get?apikey=" + MUSIXMATCH_API_KEY

class SongLyrics:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "title": ("STRING",),
                "artist": ("STRING",),
            },
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("lyrics",)

    FUNCTION = "run"

    CATEGORY = "Synesthesia"

    def run(self, title, artist):
        url = MUSIXMATCH_LYRICS_URL + "&q_track=" + title + "&q_artist=" + artist + "&format=json"
        response = requests.get(url)
        if response.status_code != 200:
            return None

        json = response.json()
        if json['message']['header']['status_code'] != 200:
            return ("",)

        lyrics = json['message']['body']['lyrics']['lyrics_body']
        print (lyrics)
        lyric_lines = lyrics.split("\n")

        lyric_lines = lyric_lines[:-4]
        lyrics = "\n".join(lyric_lines)
        return (lyrics,)