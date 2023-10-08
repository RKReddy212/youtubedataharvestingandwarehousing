import googleapiclient.discovery
from pprint import pprint

api_service_name ="youtube"
api_version = "v3"
api_key='use apikey'
youtube = googleapiclient.discovery.build(api_service_name,api_version,developerKey=api_key)
chnl_id='use channel id'
playlist_id = 'playlist id'

def pl (chnl_id):

 request = youtube.playlists().list(
        part="snippet,contentDetails",
        channelId=chnl_id,
        maxResults=50
    )
 plylst = request.execute()

 playlists = []

 for playlist_item in plylst.get('items', []):
        playlist_info = {
            'plylst_id': playlist_item['id'],
            'Itcnt': playlist_item['contentDetails']['itemCount'],
            #'kind': playlist_item['kind'],
            #'chtit': playlist_item['snippet']['channelTitle'],
            'vidtit': playlist_item['snippet']['title'],
            'publidate': playlist_item['snippet']['publishedAt'],
            'videsc': playlist_item['snippet']['localized']['description']
        }
        playlists.append(playlist_info)

 return playlists
