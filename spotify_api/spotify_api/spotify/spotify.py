import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
# (artist birdy api endpoint)'spotify:artist:2WX2uTcsvV5OnS0inACecP'
birdy_uri = 'spotify:artist:1uNFoZAHBGtllmzznpCI3s'
spotify = spotipy.Spotify(
    client_credentials_manager=SpotifyClientCredentials(client_id='43f67b0e5dc14da6bf585901d3f70bfa',
                                                        client_secret='3f1dde51d34b4c24bb6205a3978ba3c3'))
results = spotify.artist_albums(birdy_uri, album_type='album')
albums = results['items']
while results['next']:
    results = spotify.next(results)
    albums.extend(results['items'])

for album in albums:
    print(album['name'])
