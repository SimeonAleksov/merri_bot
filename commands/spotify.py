from commands.base_command import BaseCommand
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


class spotify(BaseCommand):
    def __init__(self):
        description = "spotify stuff"
        params = None
        super().__init__(description, params)
        self.sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials())

    async def handle(self, params, message, client):
        msg = ""
        
        results = self.sp.search(q=params[0], limit=20)
        msg = self.sp.current_playback()
        # for idx, track in enumerate(results['tracks']['items']):
        #     msg += f"{idx} -  {track['name']} \n"
        await message.channel.send(msg)
