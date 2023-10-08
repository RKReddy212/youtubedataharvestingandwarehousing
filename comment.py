vid_id ='enter vid id'

def cmntdetls(vid_id):

  request = youtube.commentThreads().list(
    part="snippet,replies",
    videoId =vid_id,
    maxResults=100
    )
  response = request.execute()
  CmntDetls = []


  for Comment in response.get('items',[]):
    Comment_details = { 'comment' : Comment['snippet']['topLevelComment']['snippet']['textOriginal'],
                        'author_name' : Comment['snippet']['topLevelComment']['snippet']['authorDisplayName'],
                        'authorchnlid': Comment['snippet']['topLevelComment']['snippet']['authorChannelId']['value'],
                        'cmntrply'  :   Comment['snippet']['totalReplyCount'],
                        'publishdate':  Comment['snippet']['topLevelComment']['snippet']['publishedAt']}

    CmntDetls.append(Comment_details)


  return CmntDetls



#To get all comment details of all video ids in the channel




def cmntdetls(vid_id):
  CmntDetls = []
  for i in vid_id:

    request = youtube.commentThreads().list(
      part="snippet,replies",
      videoId = i,
      maxResults=2
      )
    response = request.execute()
    try:   ------------------------->#using try and except to get comments without restrictedcomments
    


      for Comment in response['items']:
        Comment_details = { 'comment' : Comment['snippet']['topLevelComment']['snippet'].get('textOriginal','NA'),
                            'author_name' : Comment['snippet']['topLevelComment']['snippet'].get('authorDisplayName','NA'),
                            'authorchnlid': Comment['snippet']['topLevelComment']['snippet']['authorChannelId'].get('value','NA'),
                            'cmntrply'  :   Comment['snippet'].get('totalReplyCount',0),
                            'publishdate':  Comment['snippet']['topLevelComment']['snippet'].get('publishedAt','NA')}

        CmntDetls.append(Comment_details)
    except:
      pass    


  return CmntDetls
