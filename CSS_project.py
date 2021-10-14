import csv
import spotipy
import lyricsgenius
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth


class GetLyrics:
    
    def __init__(self):
        self.user_id = 'luciahrovatin'
        self.genius_key = 'xxxxxx'
        self.track_names = []
        self.track_id = []
        self.track_artists = []

    def get_playlist_tracks(self, client: SpotifyClientCredentials, search_playlist: str):
        """
        Gets all the tracks contained in a playlist defined by the user.

        :param client: credentials to authorise the access
        :param search_playlist: playlist that will be considered
        """
        scope = 'playlist-read-private'
        sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client.client_id,
                                                       client_secret=client.client_secret,
                                                       redirect_uri='http://localhost:1410/', # set in user settings
                                                       scope=scope))

        playlists = sp.current_user_playlists()
        user_id = sp.me()['id']

        for playlist in playlists['items']:
            if playlist['name'] == search_playlist:
                if playlist['owner']['id'] == user_id:
                    print('  total tracks', playlist['tracks']['total'])
                    results = sp.playlist(playlist['id'], fields="tracks,next")
                    tracks = results['tracks']
                    for i, item in enumerate(tracks['items']):
                        track = item['track']
                        self.track_artists.append(track['artists'][0]['name'])
                        self.track_names.append(track['name'])
                        self.track_id.append(track['id'])

                    while tracks['next']:
                        tracks = sp.next(tracks)
                        for i, item in enumerate(tracks['items']):
                            track = item['track']
                            self.track_artists.append(track['artists'][0]['name'])
                            self.track_names.append(track['name'])
                            self.track_id.append(track['id'])

    def request_lyrics(self, track_name, track_artist):
        """
        Using Genius API the lyrics of a song is searched and returned.
        :param str track_name: name of the song
        :param str track_artist: name of the artist
        :return: string containing the song's lyrics
        """
        genius = lyricsgenius.Genius(self.genius_key, timeout=20)

        # Added to avoid problems with songs having "-Remastered" in the title
        if "-" in track_name:
            track_name = track_name[:track_name.index("-")]
        song = genius.search_song(track_name, track_artist)
        missed_song = []
        # Check whether Genius.com recognizes the song
        if song is None:
            missed_song.append((track_name, track_artist))
            print("SKIPPED {} because not found in the collection").format({track_name})
            return 0
        return song.lyrics


    def get_lyrics(self) -> list:
        """
        Parses the whole playlist and returns a list of dictionaries.
        Each dictionary represents a single song and contains the Spotify id assigned to the song
        and the corresponding lyrics.
        :return: a list of dictionaries containing all the songs with lyrics
        """
        song_lyrics = []
        for i in range(len(self.track_names)):
            print("\n")
            print(f"Working on track {i}.")
            response = self.request_lyrics(self.track_names[i], self.track_artists[i])
            new_song = dict()
            new_song['id'] = self.track_id[i]
            new_song["lyrics"] = response
            song_lyrics.append(new_song)
        return song_lyrics

    def save_lyrics(self, filename: str):
        """
        Saves the list of songs in a csv file with two columns: id, lyrics
        :return: csv file
        """
        songs = self.get_lyrics()
        fieldnames = ['id', 'lyrics']
        with open(filename, "w", encoding='UTF8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(songs)


