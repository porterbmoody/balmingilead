pip install -q kokoro>=0.9.2 soundfile

#%%
# !pip install -q moviepy
!apt-get -qq -y install espeak-ng > /dev/null 2>&1
!pip install moviepy==2.0.0.dev2
!apt install imagemagick
!cat /etc/ImageMagick-6/policy.xml | sed 's/none/read,write/g'> /etc/ImageMagick-6/policy.xml

#%%
from kokoro import KPipeline
from IPython.display import display, Audio
import soundfile as sf
import torch
import os
import pandas as pd
from moviepy.editor import *
from google.colab import drive

drive.mount('/content/drive')

os.makedirs('audio', exist_ok=True)
os.makedirs('images', exist_ok=True)

#%%
from kokoro import KPipeline

pipeline = KPipeline(lang_code='a')
pipeline

#%%

from pytubefix import YouTube
from moviepy.editor import *
import os

url_ids = [
]

for url_id in url_ids:
    print(url_id)
    video = YouTube('https://www.youtube.com/watch?v='+url_id)
    original_title = video.title.replace('?', '').replace('|','').replace('&', 'and').replace('#', '').replace('/','_')
    print(original_title)
    filename = f'music/{original_title}.wav'
    audio_stream = video.streams.get_audio_only().download()
    audio = AudioFileClip(audio_stream)
    audio.write_audiofile(filename)
    os.remove(audio_stream)



# %%


