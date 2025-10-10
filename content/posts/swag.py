#%%
from pytubefix import YouTube
from moviepy.editor import *
import os

url_ids = [
    # 'WgibpyTp6dY',
    # 'iQ9xvTq3Jk0',
    # 'zE_rK8PX83Q',
    # 'V90pwWdXC2U',
    # 'mqnb0kKsNkQ',
    # 'kg8RgTldhbM',
    # 'AkzNwAlvq_I',
    # 'dGN1bjLajxI',
    # 'PQvHFUOc4F4',
    # 'q9W76M-I0xI',
    # 'Rfhksohebv8',
    # 'rYHNB_lPSNc',
    # 'Vn-1SX0Prg0',
    # 'P48r8D6N14c',
    # 'FyASdjZE0R0',
    # 'u3VFzuUiTGw',
    # 'mZqRDn-8540',
    # 'dMq9U44693E',
    # 'YdIYBkQBmtA',
    # 'ToMj55B6qI8',
    # 'qM5b0GeuD0o',
    # 'AeCRI306hjo',
    # '1CeuXoX4ndg',
    # 'cqFaNi9IMio',
    # 'J_Jn_5TAMMM',
    # '-uoa1FmHbwA',
    # '3qHFceF6th0',
    # 's8XIgR5OGJc',
    # 'qNBcAmujXEU',
    # 'mqnb0kKsNkQ',
    # 'luQSQuCHtcI',
    # 'd020hcWA_Wg',
    # 'WBSpCdepWqw',
    # 'sRLAwvq4qhA',
    # 's4t0_9-Gm0Y',
    # '9296lqPbnF8',
    # 'y_0_pa3pmH0',
    # 'BDrN62e_g8Q',
    # 'WLchIBIAWnI',
    # 'id3KPRJieCk',
    # 'wZhjlAXWuWA',
    # 'u3VFzuUiTGw',
    # '4fQeaM62mOY',
    # 'rSZy6XrN3SU',
    # 'mURl-vgg9xI',
    '1trifshoIw0',
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
