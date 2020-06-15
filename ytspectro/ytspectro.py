from pytube import YouTube
import os

VIDEOS_PATH = '.'
VIDEOS_EXTENSION = '.mp4' 
AUDIO_EXT = 'wav'

videos_dict = {}

# Video download function using pytube
def dowload_video(video_list):
  for video_name in video_list:
    video = YouTube('https://www.youtube.com/watch?v={}'.format(video_name))
    video.streams.filter(type = "audio", file_extension = "mp4").all()[0].download(filename=video_name)


# Download process
for key in list(videos_dict.keys()):
  dowload_video(videos_dict[key])

# Check
assert len([f for f in os.listdir(VIDEOS_PATH) if f.endswith(VIDEOS_EXTENSION)]) == num_videos
print('Videos downloaded')