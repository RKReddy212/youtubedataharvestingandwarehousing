def youtube_chnl_details(chnl_id):

      chnldetls=channel_details(chnl_id)
      playlistdetails=pl (chnl_id)
      videoids=vididdetl(playlist_id)
      commentdtls=cmntdetls(vid_id)

      youtubechnldata =  {'channel details':chnldetls,
                          'play list' : playlistdetails,
                          'video ids' : videoids,
                          'comment details':commentdtls}

      return youtubechnldata
