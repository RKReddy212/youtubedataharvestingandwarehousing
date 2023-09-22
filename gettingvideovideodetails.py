import googleapiclient.discovery
from pprint import pprint



api_service_name ="youtube"
api_version = "v3"
api_key='use api key '
youtube = googleapiclient.discovery.build(api_service_name,api_version,developerKey=api_key)

playlist_id = 'enter playlist id'



#define function to retreive the video ids in the playlist it gives 50 ids only bcoz without nextpage token we get only 50 ids#

def vididdetl(playlist_id):



  request = youtube.playlistItems().list(
        part="snippet,contentDetails",
        playlistId=playlist_id,
        maxResults=50
    )
  response = request.execute()
  Videoids = []

  for VidIds in response.get('items',[]):
      Video_ids = {'Vids_Ids' : VidIds['contentDetails']['videoId']}

      Videoids.append(Video_ids)


  return Videoids

  playlist_id = 'enter playlist id'


#define function using next page token to get all the video ids in all play list#


def vididdetl(playlist_id):
  Videoids = []
  next_page_token = None


  while True:
    request = youtube.playlistItems().list(
          part="snippet,contentDetails",
          playlistId=playlist_id,
          maxResults=50,
          pageToken=next_page_token
      )
    response = request.execute()



    for VidIds in response.get('items',[]):
        Video_ids = {'Vids_Ids' : VidIds['contentDetails']['videoId']}

        Videoids.append(Video_ids)

    next_page_token = response.get('nextPageToken')

    if not next_page_token:
            break

  return Videoids

playlist_id = 'enter playlist id'
