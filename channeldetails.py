import googleapiclient.discovery
from pprint import pprint




api_service_name ="youtube"
api_version = "v3"
api_key='Enter api key'
youtube = googleapiclient.discovery.build(api_service_name,api_version,developerKey=api_key)
chnl_id='Enter channel id'



def channel_details(chnl_id):
    request = youtube.channels().list(
             part="snippet,contentDetails,statistics",
             id=chnl_id
        )
    response = request.execute()

    dic = dict(tit = response['items'][0]['snippet']['title'],
                  des = response['items'][0]['snippet']['description'],
                  pub = response['items'][0]['snippet']['publishedAt'],
                  sbc = response['items'][0]['statistics']['subscriberCount'],
                  vic = response['items'][0]['statistics']['videoCount'],
                  vwc = response['items'][0]['statistics']['viewCount'],
                  ply_id = response['items'][0]['contentDetails']['relatedPlaylists']['uploads'])
    return dic


channeldetails=(channel_details(chnl_id))
pprint(channeldetails)
