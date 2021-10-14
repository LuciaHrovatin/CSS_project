from spotipy.oauth2 import SpotifyClientCredentials
from CSS_project import GetLyrics

# Initialize with user access keys
SPOTIPY_CLIENT_ID='xxx'
SPOTIPY_CLIENT_SECRET='xxx'
user = SpotifyClientCredentials(SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET)

# Download the lyrics banned after 9/11
css_lyrics = GetLyrics()
css_lyrics.get_playlist_tracks(user, search_playlist="CSS_project")
css_lyrics.save_lyrics(filename="songs_lyrics.csv")

# Download 100 further not banned songs
css_lyrics = GetLyrics()
css_lyrics.get_playlist_tracks(user, search_playlist="CSS_2000")
css_lyrics.save_lyrics(filename="songs_2000.csv")



