from .prompt import OpenAIPromptGenerator
from .now_playing import SpotifyNowPlaying 
from .lyrics import SongLyrics 

NODE_CLASS_MAPPINGS = {
    "Synesthesia: Spotify Now Playing": SpotifyNowPlaying,
    "Synesthesia: Song Lyrics": SongLyrics,
    "Synesthesia: OpenAI Generate Prompt": OpenAIPromptGenerator,
}

__all__ = ['NODE_CLASS_MAPPINGS']