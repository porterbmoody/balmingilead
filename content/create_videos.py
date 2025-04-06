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
os.makedirs('music', exist_ok=True)

url_ids = [
    'WgibpyTp6dY',
    'iQ9xvTq3Jk0',
    'zE_rK8PX83Q',
    'V90pwWdXC2U',
    'mqnb0kKsNkQ',
    'kg8RgTldhbM',
    'AkzNwAlvq_I',
    'dGN1bjLajxI',
    'PQvHFUOc4F4',
    'q9W76M-I0xI',
    'Rfhksohebv8',
    'rYHNB_lPSNc',
    'Vn-1SX0Prg0',
    'P48r8D6N14c',
    'FyASdjZE0R0',
    'u3VFzuUiTGw',
    # 'mZqRDn-8540',
    # 'dMq9U44693E',
    # 'YdIYBkQBmtA',
    # 'ToMj55B6qI8',
    # 'qM5b0GeuD0o',
    # 'AeCRI306hjo',
    # '1CeuXoX4ndg',
    # 'cqFaNi9IMio',
    'luQSQuCHtcI',
    'J_Jn_5TAMMM'
    'Lj-_mD0w474',
    '18sNT1yLJqE',
    '1612_Y7N9x4',
    '0QuAJDgWIoU',
    'GGhfDatd8kw'
    'hQ0Gsf8gyE8'
    'y0WEgrN0nJc'
    'y_0_pa3pmH0'
    'J7p4bzqLvCw'
    '4D7u5KF7SP8'
    '4D7u5KF7SP8'
    'JhulBGMA7G4'
    '3mwiO5st-us'
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
