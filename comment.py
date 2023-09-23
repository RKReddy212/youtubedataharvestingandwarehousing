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
