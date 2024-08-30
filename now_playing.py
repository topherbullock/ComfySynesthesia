import spotipy
from spotipy.oauth2 import SpotifyOAuth

SCOPE = "user-read-recently-played,user-read-currently-playing"

class SpotifyNowPlaying:
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=SCOPE))

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {},
        }

    RETURN_TYPES = ("STRING", "STRING",)
    RETURN_NAMES = ("Song Title", "Artist",)

    FUNCTION = "run"

    CATEGORY = "Synesthesia"

    @classmethod
    def IS_CHANGED(cls, **kwargs):
        return float("NaN")

    def run(self):
        response = self.sp.currently_playing()

        if response is None:
            recents = self.sp.current_user_recently_played(limit=1)
            item = recents['items'][0]['track']
        else:
            item = response['item']

        return (item["name"], item["artists"][0]["name"],)