from pytube import YouTube
youtube_video_url = 'https://www.youtube.com/watch?v=5g-MHZ0MzZY'
yt_obj = YouTube(youtube_video_url)
filter= yt_obj.streams.filter(progressive=True, file_extension='mp4')
filter.get_highest_resolution().download()