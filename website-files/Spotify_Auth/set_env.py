import os

PORT_NUMBER = 8080
SPOTIPY_CLIENT_ID = 'b22e90de0df940d7834f50ab5b9b6d6c'
SPOTIPY_CLIENT_SECRET = '861f089eee9e4be79eaa321c74d790b4'
SPOTIPY_REDIRECT_URI = 'http://localhost:8080'
# SCOPE = open('C:\Spotify_Project\Spotipy_Reference\scopes.txt').read()
CACHE = '.spotipyoauthcache'

os.environ['SPOTIPY_CLIENT_ID'] = SPOTIPY_CLIENT_ID
os.environ['SPOTIPY_CLIENT_SECRET'] = SPOTIPY_CLIENT_SECRET
os.environ['SPOTIPY_REDIRECT_URI'] = SPOTIPY_REDIRECT_URI