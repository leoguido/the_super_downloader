from pytube import YouTube

def download_video(url, output_file):
    
    video = YouTube(url)
    video = video.streams.get_highest_resolution()

    video.download(output_file)

    return True