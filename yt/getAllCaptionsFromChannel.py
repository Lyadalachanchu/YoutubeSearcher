api_key = "AIzaSyAZjUllFM931vhUM7JdOAl_eysGcTzGZtk"
from apiclient.discovery import build
import pickle
def get_channel_videos(channel_id):
    res = youtube.channels().list(id = channel_id, part = 'contentDetails').execute()
    playlist_id = res['items'][0]['contentDetails']['relatedPlaylists']['uploads']

    videos = []
    next_page_token = None

    while 1:
        res = youtube.playlistItems().list(playlistId = playlist_id, part = 'snippet', maxResults = 50, pageToken = next_page_token).execute()
        videos += res['items']
        next_page_token = res.get('nextPageToken')

        if next_page_token is None:
            break

    return videos

youtube = build('youtube', 'v3', developerKey = api_key)
''''res = youtube.channels().list(id = 'UCsXVk37bltHxD1rDPwtNM8Q', part = 'contentDetails').execute()
res = youtube.playlistItems().list(playlistId = 'UUsXVk37bltHxD1rDPwtNM8Q', part = 'snippet', maxResults = 50).execute()'''
videos = get_channel_videos('UCr3cBLTYmIK9kY0F_OdFWFQ')

videoIds = []
for video in videos:
    print(video['snippet']['resourceId']['videoId'])
    videoIds.append(video['snippet']['resourceId']['videoId'])


MyFile=open('output.txt','w')
for videoId in videoIds:
     MyFile.write(videoId)
     MyFile.write('\n')
MyFile.close()



