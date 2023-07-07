import requests
from client.twitter.script import download_video as download_twitter_video
from client.youtube.script import download_video as download_youtube_video


class Downloader():

    def __init__(self):
        #variables
        pass
    
    def download_twitter(self, url):

        try:
            download_twitter_video(tweet_url=url, output_file='./video.mp4', target_all_videos=False)

            return True

        except Exception as e:
            print(e)

            return False
        
    def download_youtube(self, url):

        try:
            download_youtube_video(url=url, output_file='./client/youtube/video')
            return True

        except Exception as e:
            print('ERROR')
            print(e)

            #import traceback
            #print(traceback.format_exc())

            return False