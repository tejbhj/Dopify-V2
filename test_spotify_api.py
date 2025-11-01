import spotipy
import sys
from spotipy.oauth2 import SpotifyClientCredentials
spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id='9d44f1c7ffb1418a96863ef81d69e531',client_secret='27e35573b01d42dc8139113879f25bed'))
if len(sys.argv) > 1:
    name = ' '.join(sys.argv[1:])
else:
    name = 'Varun Dubey'
results = spotify.search(q='artist:' + name, type='artist')
items = results['artists']['items']
# if len(items) > 0:
    # artist = items[0]
    # print(artist['uri'])
    # print(artist['name'], artist['images'][0]['url'])
# artist_uri = "spotify:artist:2WX2uTcsvV5OnS0inACecP"
print(items[0])
results = spotify.artist_top_tracks(items[0]['uri'])
# final_result=results['tracks'][:10]
# for track in results['tracks'][:1]:
#     print(track)
#api crash only when exceeding free tier, change tiemout by custom function chatgpt gave, ava on github 