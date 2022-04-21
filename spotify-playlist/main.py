import os

import requests
import spotipy
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()

user_input = input("Which year do you want to travel to? type the date in this format YYYY-MM-DD: ")

response = requests.get(url=f"https://www.billboard.com/charts/hot-100/{user_input}")
response.raise_for_status()
soup = BeautifulSoup(response.text, "html.parser")

songs = [item.getText().strip() for item in soup.find_all(name="h3", class_="a-no-trucate")]

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=os.environ.get("SPOTIFY_CLIENT_ID"),
                                               client_secret=os.environ.get("SPOTIFY_CLIENT_SECRET"),
                                               redirect_uri="https://example.com",
                                               scope="playlist-modify-private",
                                               show_dialog=True,
                                               cache_path=".cache"))
song_uris = []
for song in songs:
    results = sp.search(q=f"track:{song} year:{user_input.split('-')[0]}", type="track")
    try:
        uri = results["tracks"]["items"][0]["uri"]
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")
    else:
        print(uri)
        song_uris.append(uri)

playlist = sp.user_playlist_create(user=sp.current_user()["id"], public=False, name=f"{user_input} Billboard 100")
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
print(f"Added {len(song_uris)} songs to '{user_input} Billboard 100' Playlist")
