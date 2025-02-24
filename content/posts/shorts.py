#%%

# I would like it to be able to 
# - give it a prompt like “make a video about 3 important business techniques” 
# - an LLM would create a script -> 
# - create a set of images to go with that script (or maybe a video but that’s probably more advanced) 
# - add the script on top of the video at the correct time stamps 
# - add text to speech on top of the video

#%%

import openai
from gtts import gTTS
from moviepy.editor import ImageSequenceClip, TextClip, CompositeVideoClip
import os

def generate_script(prompt):
	response = openai.ChatCompletion.create(
		model="gpt-4",
		messages=[{"role": "system", "content": "You are a helpful script writer."},
		           {"role": "user", "content": prompt}]
	)
	return response['choices'][0]['message']['content']

def create_images(script, num_images=5):
	images = []
	for i in range(num_images):
		image_path = f"image_{i}.png"
		# For now, assume images are pre-generated and named image_0.png, image_1.png, etc.
		images.append(image_path)
	return images

def text_to_speech(script, output_audio="narration.mp3"):
	tts = gTTS(script)
	tts.save(output_audio)
	return output_audio

def create_video(images, script, audio_file, output_video="output_video.mp4"):
	clip = ImageSequenceClip(images, fps=1)

	text_clip = TextClip(script, fontsize=24, color='white', size=clip.size, method='caption')
	text_clip = text_clip.set_position(('center', 'bottom')).set_duration(clip.duration)

	video = CompositeVideoClip([clip, text_clip])
	video = video.set_audio(audio_file)

	video.write_videofile(output_video, codec='libx264', fps=24)

if __name__ == "__main__":
	prompt = "Make a video about 3 important business techniques"
	script = generate_script(prompt)
	images = create_images(script)
	audio_file = text_to_speech(script)
	create_video(images, script, audio_file)
