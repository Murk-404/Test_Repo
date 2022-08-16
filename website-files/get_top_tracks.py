import sys
import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials
import os
import json

# user1 = str(sys.argv[1])
user1 = ""
if (sys.platform == 'linux'):
  exec(open("Spotify_Auth/set_env.py").read())
else:
  exec(open("C:\Spotify_Project\website-files\Spotify_Auth\set_env.py").read())

# sets auth scopes
if (sys.platform == 'linux'):
  SCOPE = open('Spotify_Auth/scopes.txt').read()
else:
  SCOPE = open('C:\Spotify_Project\website-files\Spotify_Auth\scopes.txt').read()

arr1 = []
arr2 = []
arr3 = []
arr4 = []

token = spotipy.util.prompt_for_user_token(scope=SCOPE)
current = spotipy.Spotify(auth=token).current_user()
results = current['id']
# token = spotipy.util.prompt_for_user_token(username=results, scope=SCOPE)

# time_range = 'short_term' #long_term, medium_term or short_term


def run(num, off):
  if(num == 1):
    top = spotipy.Spotify(auth=token).current_user_top_tracks(limit=50, offset=off, time_range=time_range)
    results = top
    for idx, item in enumerate(results['items']):
      artists = item['artists']
      artist = str(artists[0]['name'])
      track = str(item['name'])
      string = track
      arr1.append(string)
      # print(idx, track, " - ", artist)
    if(off == 0):
      if(len(arr1) == 50):
        del arr1[-1]
  if(num == 2):
    top = spotipy.Spotify(auth=token).current_user_top_tracks(limit=50, offset=off, time_range=time_range)
    results = top
    for idx, item in enumerate(results['items']):
      artists = item['artists']
      artist = str(artists[0]['name'])
      # track = str(item['name'])
      string = artist
      arr2.append(string)
      # print(idx, track, " - ", artist)
    if(off == 0):
      if(len(arr2) == 50):
        del arr2[-1]
  if(num==3):
    top = spotipy.Spotify(auth=token).current_user_top_tracks(limit=50, offset=off, time_range=time_range)
    results = top
    # print(results)
    for idx, item in enumerate(results['items']):
      artists = item['album']
      images = str(artists['images'][2]['url'])
      # track = str(item['name'])
      # print(images)
      # string = artist
      arr3.append(images)
      # print(idx, track, " - ", artist)
    if(off == 0):
      if(len(arr3) == 50):
        del arr3[-1]
  if(num==4):
    top = spotipy.Spotify(auth=token).current_user_top_artists(limit=50, offset=off, time_range=time_range)
    results = top
    for idx, item in enumerate(results['items']):
      artists = item['name']
        # artist = str(artists[0]['name'])
      art = str(item['name'])
      arr4.append(art)
    
    if(off == 0):
      if(len(arr4) == 50):
        del arr4[-1]


# def set_envv(num):
#   if(num==1):
#     TOP_TRACKS_LIST = arr
#     os.environ['TOP_TRACKS_LIST'] = TOP_TRACKS_LIST
#   elif(num==2):
#     TOP_TRACKS_ART_LIST = arr
#     os.environ['TOP_TRACKS_ART_LIST'] = TOP_TRACKS_ART_LIST

if (sys.platform == 'linux'):
  newpath = "App_Users/" + results
else:
  newpath = "C:/Spotify_Project/website-files/public/App_Users/" + results
# print(newpath)
if not os.path.exists(newpath):
    os.makedirs(newpath)


def write_json(num):
  if(num==1):
    link_1 = newpath + '\_top_tracks_' + time_range + '_' + results + '.json'
    with open(link_1, 'w') as jsonfile:
      json.dump(arr1, jsonfile)
  if(num==2):
    link_2 = newpath + '\_top_tracks_art_' + time_range + '_' + results + '.json'
    with open(link_2, 'w') as jsonfile:
      json.dump(arr2, jsonfile)
  if(num==3):
    link_3 = newpath + '\_top_tracks_images_' + time_range + '_' + results + '.json'
    with open(link_3, 'w') as jsonfile:
      json.dump(arr3, jsonfile)
  if(num==4):
    link_4 = newpath + '\_top_artists_' + time_range + '_' + results + '.json'
    with open(link_4, 'w') as jsonfile:
      json.dump(arr4, jsonfile)

def run_all():
  run(1, 0)
  run(1, 49)
  run(2, 0)
  run(2, 49)
  run(3, 0)
  run(3, 49)
  run(4, 0)
  run(4, 49)
  write_json(1)
  write_json(2)
  write_json(3)
  write_json(4)

for z in range(3):
  if((z+1)==1):
    time_range = 'short_term'
    run_all()
    arr1 = []
    arr2 = []
    arr3 = []
    arr4 = []
  if((z+1)==2):
    time_range = 'medium_term'
    run_all()
    arr1 = []
    arr2 = []
    arr3 = []
    arr4 = []
  if((z+1)==3):
    time_range = 'long_term'
    run_all()
    arr1 = []
    arr2 = []
    arr3 = []
    arr4 = []


# print(user1)
print(results)

# print('<body><head><link rel="stylesheet" href="style.css"></head></body>')
# c = -1
# for i in arr1:
#   c = c + 1
  # print("<h3>" + '<img src="' + arr3[c] + '"> Track: ' + i + " - Artist: " + arr2[c] + "</h3>")
# print("<h3>" + results + "</h3>")
# print('</body>')
# print(arr1)
# print(arr2)
