
import sys
import os
import time
from pytube import YouTube

if "-onlyvideo" in sys.argv:
    onlyvideo = True
else:
    onlyvideo = False

if "-withvideo" in sys.argv:
    withvideo = True
else:
    withvideo = False

# text file at the end of the arg list
filename = sys.argv[-1]

# make sure filename is a .txt file
if (not filename.endswith(".txt")):
    print("link file must be a text file")
    exit(1)

# create a Downloads directory if it doesn't exist
downloads = 'Downloads' 
if not os.path.exists(downloads):
    os.makedirs(downloads)

# open the file with all the links
with open(filename) as file:
    urls = [line.rstrip() for line in file]

# go into the Downloads directory
cd = os.getcwd() 
os.chdir(downloads)

num = 0
for url in urls:
    print(url)
    vid = YouTube(url)
    video_download = vid.streams.get_highest_resolution()
    audio_download = vid.streams.get_audio_only()
    entry = YouTube(url).title
    print(f"Video found: {entry}")
    if (withvideo or onlyvideo):
        print(f"Downloading video...", end='')
        video_download.download(filename=f"{entry}.mp4")
        print(f"done")
    if (not onlyvideo):
        print("Downloading audio...", end='')
        audio_download.download(filename=f"{entry}.mp3")
        print(f"done")
    num = num + 1
    time.sleep(1)

os.chdir(cd)
print(f"Done downloading " + str(num) + " links.")

