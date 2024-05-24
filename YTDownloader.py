from pytube import YouTube
from sys import argv

link = argv(1)
yt = YouTube(link)

print ("title: ", yt.title)
print ("view: ", yt.views)
yd = yt.streams.get_highest_resolution()

## set folder for YD.download to PATH that you want the videos to save to.
yd.download()

## when running the command use format ( python3 YTDownloader.py " -- video link --")