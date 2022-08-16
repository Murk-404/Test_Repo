import sys
from urllib.parse import urlsplit
from xml.sax import default_parser_list
import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials
import os
import wget
import yt_dlp
from youtubesearchpython import VideosSearch
import music_tag
from ytmusicapi import YTMusic
from PIL import Image
#TODO file format selection 
#TODO album art style, yt thumbnail or spotify
#TODO 

#set environment variables
if (sys.platform == 'linux'):
  exec(open("../Spotify_Auth/set_env.py").read())
  SCOPE = open('../Spotify_Auth/scopes.txt').read()
  windows = False
else:
  exec(open("C:\Spotify_Project\website-files\Spotify_Auth\set_env.py").read())
  SCOPE = open('C:\Spotify_Project\website-files\Spotify_Auth\scopes.txt').read()
  windows = True

#set variables
user = str(sys.argv[1])
playlistid = str(sys.argv[2])
token = spotipy.util.prompt_for_user_token(username=user, scope=SCOPE)
sp = spotipy.Spotify(token)

#read the tracks from the spotify playlist defined
output = sp.user_playlist_tracks(user,playlistid,None,100,0)

playlistcount = output['total']

if (sys.argv[3]):
  countdone = (int)(sys.argv[3])
else:
  countdone = 0

class Track:
  def __init__(s,album,artist,artwork,discnumber,totaltracks,tracknumber,title,year,lengthms,local):
    s.album = album
    s.artist = artist
    s.artwork = artwork
    s.discnumber = discnumber
    s.totaltracks = totaltracks
    s.tracknumber = tracknumber
    s.title = title
    s.year = year
    s.lengthms = lengthms
    s.local = local

  def out(s):
    return s.artist + ' - ' + s.title

  def dump(s):
    return 'album ' + str(s.album) + ' artist ' + str(s.artist) + ' artwork ' + str(s.artwork) + ' discnumber ' + str(s.discnumber) + ' tracknumber ' + str(s.tracknumber) + ' release date ' + str(s.year) + ' length in ms ' + str(s.lengthms)

#main loop, loops through every song in the playlist and does cool stuff with that
for trackid in range(playlistcount):
  #ensure the looping stops when we reach the end of the playlist
  output = sp.user_playlist_tracks(user,playlistid,None,100,countdone)
  countdone += 100
  if (playlistcount-countdone < 0):
    loopfor=playlistcount-countdone+100
  else:
    loopfor=100

  #reset on loop
  i=0
  songarray=[]
  urls=[]

  #grabs info from spotify
  for i in range(loopfor):
    localfile = output['items'][i]['is_local']
    if (localfile != True): #if file isnt a local file
      #grab info
      title = output['items'][i]['track']['name']
      album = output['items'][i]['track']['album']['name']
      artist = output['items'][i]['track']['album']['artists'][0]['name']
      discnumber = output['items'][i]['track']['disc_number']
      year = output['items'][i]['track']['album']['release_date'] #TODO is currently full date
      tracknumber = output['items'][i]['track']['track_number']
      totaltracks = output['items'][i]['track']['album']['total_tracks']
      arturl = output['items'][i]['track']['album']['images'][0]['url']
      lengthms = output['items'][i]['track']['duration_ms']
      #save in a track object
      song = Track(album,artist,arturl,discnumber,totaltracks,tracknumber,title,year,lengthms,False)
    else:
      #grab info
      # title = output['items'][i]['track']['name']
      # artist = output['items'][i]['track']['artists'][0]['name']
      song = Track('none','none','none','none','none','none','none','none','none',True)
      playlistcount-=1
      # print(output['items'][i]['track']['album']['images'][0]['url'])
    #put in array
    songarray.append(song)
    count = i+countdone-100
    print((str)(count) + ' -> ' + song.out())


  # def searchYTVideos(): #fallback
  #   title = songarray[i].out() + ' lyrics'
  #   search = VideosSearch(title, limit = 1)
  #   # thumbnail = search.result()['result'][0]['thumbnails'][1]['url']
  #   if (search.result()):
  #     print(search.result())
  #     url = search.result()['result'][0]['link']
  #     urls.append(url)
  #   else:
  #     print('ERROR: NO SONG FOUND, f')
  #     print('MANUAL TAGGING NECESSARY: ' + songarray[i].dump())


  def searchYT(type):
    ytmusic = YTMusic('auth.json')
    title = songarray[i].out()
    search_results = ytmusic.search(title,type,ignore_spelling=False,limit=1)
    if (search_results):
      url = 'https://www.youtube.com/watch?v=' + search_results[0]['videoId']
      urls.append(url)
      return search_results[0]['duration_seconds']
    else:
      urls.append('skip')
      print('MANUAL NEEDED: ' + songarray[i].dump())
      return -1

  for i in range(loopfor):
    if (songarray[i].local == False):
      print('searching... ' + songarray[i].title)
      seconds = searchYT('songs') #run the default search algo, and save the selected songs seconds count in seconds
      if (seconds == -1):
        print('ytmusic search crashed, trying ytvideos')
        urls.pop(len(urls) - 1)
        searchYT('videos')
      chksec = songarray[i].lengthms / 1000 #load the spotify songs seconds
      if (seconds - 3 < chksec and seconds + 3 > chksec): #check to see if the new found song is within a reasonable amount of deviance
        print('spotify time = ' + (str)(chksec) + ' yt time = ' + (str)(seconds) + ' determined trusted.')
      else:
        print('spotify time = ' + (str)(chksec) + ' yt time = ' + (str)(seconds) + ' determined NOT trusted.')
        urls.pop(len(urls) - 1)
        searchYT('videos')
    else:
      urls.append('skip')




  #now that spotify data is ripped, download files
  for i in range(loopfor):
    if (songarray[i].local == False):
      ydl_opts = {
        'format': 'm4a/bestaudio/best',
        'windowsfilenames': windows,
        'outtmpl': 'output/unnamed.m4a',
        'quiet': 'true',
        # 'paths': '/home/dani/Documents/git/spotify-stuff/Spotify-API-Project/website-files/ytdler/output/', #TODO fix path
        'postprocessors': [{
          'key': 'FFmpegExtractAudio',
          'preferredcodec': 'm4a',
        }]
      }

      if (urls[i] != 'skip'):
        try:
          with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            error_code = ydl.download(urls[i])
        except:
          print('ERROR: ' + str(error_code) + ' failed to download!!!')
          print('ERROR: song metadata for manual fix: ' + songarray[i].dump())
      else:
        continue

      #tag music files
      f = music_tag.load_file('output/unnamed.m4a')
      f['album'] = songarray[i].album
      f['artist'] = songarray[i].artist
      f['discnumber'] = songarray[i].discnumber
      f['totaltracks'] = songarray[i].totaltracks
      f['tracknumber'] = songarray[i].tracknumber
      f['title'] = songarray[i].title
      f['year'] = songarray[i].year
      
      #add artwork
      arturl=songarray[i].artwork
      # print(arturl)
      imgout = wget.download(arturl)

      artlocation = arturl[24:]
      os.rename(artlocation,'output/img')

      img = Image.open('output/img')
      rgb_img = img.convert("RGB")
      rgb_img.save('output/img.jpg')

      with open('output/img.jpg','rb') as img:
        f['artwork'] = img.read()
      f.save()

      clean = songarray[i].out().replace('/','-')
      newname = 'output/' + clean + '.m4a'
      os.rename('output/unnamed.m4a', newname)
      #file is done processing, enjoy the music (with like ~<1% chance its the wrong song)

#cleanup
os.remove('output/img.jpg')
os.remove('output/img')

#TODO move all the songs into folder named after spotify playlist

print('\nScript finished, downloaded and tagged ' + (str)(playlistcount) + ' songs from the playlist.')