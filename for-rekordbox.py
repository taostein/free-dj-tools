
import os

# For some reason the MP3's downloaded with dl-yt won't load into Rekordbox (or Mixed in Key)
# It must be something in the header, or codec.
# If we run them through ffmpeg, MP3 to MP3, then they load just fine.
# I guess it's the codec.
# Fron youtube (via ffprobe):
# Stream #0:0[0x1](und): Audio: aac (LC) (mp4a / 0x6134706D), 44100 Hz, stereo, fltp, 2 kb/s (default)
# After running through ffmpeg:
# Stream #0:0: Audio: mp3 (mp3float), 44100 Hz, stereo, fltp, 128 kb/s
# So this script does that.
# Note: This script generates a shell script. Run that.

target_dir = "Rekordbox"
print("mkdir " + target_dir)
files = os.listdir()
for f in files:
    if f.endswith(".mp3"):
        f1 = f.replace(' ','\\ ')
        f1 = f1.replace('(','\\(')
        f1 = f1.replace(')','\\)')
        print("ffmpeg -i ", f1, (target_dir + "/" + f1))

