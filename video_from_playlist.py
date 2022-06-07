from pytube import Playlist

try:
    playlist = Playlist("https://www.youtube.com/playlist?list=PLL0MRDsQu9LXjvm3WfPUVwj14B7GJSOuB")
    k=0
    for video in playlist.videos:
        filter = video.streams.filter(progressive=True, file_extension='mp4')
        filter.get_highest_resolution().resolution.download(output_path='./')
except Exception as e:
    print(e)