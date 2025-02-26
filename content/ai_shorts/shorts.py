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
#%%
from PIL import Image
from moviepy.editor import ImageSequenceClip

images = [
	"../images/office/office1.jpeg", 
	"../images/office/office2.jpeg", 
	"../images/office/office3.jpeg"
]

# Resize all images to the same size
size = (800, 600)  # Set the target size
resized_images = []

for img_path in images:
	img = Image.open(img_path)
	img = img.resize(size)
	resized_path = img_path.replace('.jpeg', '_resized.jpeg')
	img.save(resized_path)
	resized_images.append(resized_path)

# Create the video
clip = ImageSequenceClip(resized_images, fps=0.5)
clip.write_videofile("../images/office/office_slideshow.mp4", codec='libx264', fps=24)


# %%
from PIL import Image
from moviepy.editor import ImageSequenceClip

images = [
	"../images/office/office1.jpeg", 
	"../images/office/office2.jpeg", 
	"../images/office/office3.jpeg"
]

phone_size = (1080, 1920)
resized_images = []

for img_path in images:
	img = Image.open(img_path)
	img = img.resize(phone_size)
	resized_path = img_path.replace('.jpeg', '_resized.jpeg')
	img.save(resized_path)
	resized_images.append(resized_path)

clip = ImageSequenceClip(resized_images, fps=0.5)
clip.write_videofile("../images/office/office_slideshow.mp4", codec='libx264', fps=24)

# %%
from PIL import Image, ImageOps
from moviepy.editor import ImageSequenceClip, AudioFileClip

images = [
	"office1.jpeg", 
	"office2.jpeg", 
	"office3.jpeg"
]

# Target phone screen dimensions
phone_size = (1080, 1920)
resized_images = []

for img_path in images:
	img = Image.open(img_path)
	img = ImageOps.fit(img, phone_size, method=Image.LANCZOS, centering=(0.5, 0.5))

	final_img = Image.new("RGB", phone_size, (0, 0, 0))
	img_w, img_h = img.size
	final_img.paste(img, ((phone_size[0] - img_w) // 2, (phone_size[1] - img_h) // 2))
	
	resized_path = img_path.replace('.jpeg', '_resized.jpeg')
	final_img.save(resized_path)
	resized_images.append(resized_path)

clip = ImageSequenceClip(resized_images, fps=0.5)
clip.write_videofile("short.mp4", codec='libx264', fps=24)

audio = AudioFileClip("happy.mp3")

clip = clip.set_audio(audio)
clip

# %%
from PIL import Image, ImageOps
from moviepy.editor import *

images = [
	"office1.jpeg", 
	"office2.jpeg", 
	"office3.jpeg"
]

phone_size = (1080, 1920)
resized_images = []

for img_path in images:
	img = Image.open(img_path)
	img = ImageOps.fit(img, phone_size, method=Image.LANCZOS, centering=(0.5, 0.5))
	
	final_img = Image.new("RGB", phone_size, (0, 0, 0))
	
	img_w, img_h = img.size
	final_img.paste(img, ((phone_size[0] - img_w) // 2, (phone_size[1] - img_h) // 2))
	
	resized_path = img_path.replace('.jpeg', '_resized.jpeg')
	final_img.save(resized_path)
	resized_images.append(resized_path)

clip = ImageSequenceClip(resized_images, fps=.25)

audioclip = AudioFileClip("happy.mp3").subclip(0, 15)
audio = CompositeAudioClip([audioclip])
clip.audio = audio

clip = clip.set_duration(audio.duration)

clip.write_videofile("short.mp4", codec='libx264', fps=24, audio_codec='aac')


#%%

from PIL import Image, ImageOps, ImageDraw, ImageFont
from moviepy.editor import ImageSequenceClip, AudioFileClip

images = [
	"office1.jpeg", 
	"office2.jpeg", 
	"office3.jpeg"
]

business_texts = [
	"Focus on Customer Experience: Build loyalty through exceptional service.",
	"Data-Driven Decisions: Use analytics to guide your business strategy.",
	"Innovation and Adaptation: Stay ahead by embracing change and creativity."
]


phone_size = (1080, 1920)
resized_images = []

font_path = "arial.ttf"
font_size = 60
font = ImageFont.truetype(font_path, font_size)

for img_path, text in zip(images, business_texts):
	# img = Image.open(img_path)
	# img = ImageOps.fit(img, phone_size, method=Image.LANCZOS, centering=(0.5, 0.5))
	
	# final_img = Image.new("RGB", phone_size, (0, 0, 0))
	
	# img_w, img_h = img.size
	# final_img.paste(img, ((phone_size[0] - img_w) // 2, (phone_size[1] - img_h) // 2))

	# draw = ImageDraw.Draw(final_img)
	# # text_w, text_h = draw.textsize(text, font=font)
	# text_w = draw.textlength(text, font=font)
	# text_h = 10 * 3
	# text_position = ((phone_size[0] - text_w) // 2, phone_size[1] - 200)  # Position near the bottom
	# draw.text(text_position, text, font=font, fill=(255, 255, 255))

	resized_path = img_path.replace('.jpeg', '_resized.jpeg')
	final_img.save(resized_path)
	resized_images.append(resized_path)

clip = ImageSequenceClip(resized_images, fps=0.5)

audio = AudioFileClip("happy.mp3")
clip = clip.set_audio(audio)

clip = clip.set_duration(audio.duration)

clip.write_videofile("short.mp4", codec='libx264', fps=24, audio_codec='aac')

# %%
from PIL import Image, ImageOps, ImageDraw, ImageFont
from moviepy.editor import *

images = [
	"office1.jpeg", 
	"office2.jpeg", 
	"office3.jpeg"
]

business_texts = [
	"Focus on Customer Experience",
	"Data-Driven Decision Making",
	"Innovation and Adaptation"
]

phone_size = (1080, 1920)
resized_images = []

font_path = "arial.ttf"
font_size = 80
font = ImageFont.truetype(font_path, font_size)

for img_path, text in zip(images, business_texts):
	img = Image.open(img_path)
	img = ImageOps.fit(img, phone_size, method=Image.LANCZOS, centering=(0.5, 0.5))
	
	final_img = Image.new("RGB", phone_size, (0, 0, 0))
	
	img_w, img_h = img.size
	final_img.paste(img, ((phone_size[0] - img_w) // 2, (phone_size[1] - img_h) // 2))

	draw = ImageDraw.Draw(final_img)
	text_w = draw.textlength(text, font=font)
	text_h = 10 * 3
	text_position = ((phone_size[0] - text_w) // 2, phone_size[1] - 250)
	draw.text(text_position, text, font=font, fill=(255, 255, 255))

	resized_path = img_path.replace('.jpeg', '_resized.jpeg')
	final_img.save(resized_path)
	resized_images.append(resized_path)

clip = ImageSequenceClip(resized_images, fps=0.25)

audioclip = AudioFileClip("happy.mp3").subclip(0, 15)
audio = CompositeAudioClip([audioclip])
clip.audio = audio

clip = clip.set_duration(audio.duration)

clip.write_videofile("short.mp4", codec='libx264', fps=24, audio_codec='aac')

# %%
from PIL import Image, ImageOps, ImageDraw, ImageFont
from moviepy.editor import *

images = [
	"office1.jpeg", 
	"office2.jpeg", 
	"office3.jpeg"
]

business_texts = [
	"Bloom Marketing is highly Focused on Customer Experience",
	"The Bloom Analysis team executes Data-Driven Decision Making",
	"Bloom Marketing is fueled by Innovation and Adaptation"
]

phone_size = (1080, 1920)
resized_images = []

font_path = "arial.ttf"
font_size = 40
font = ImageFont.truetype(font_path, font_size)

for img_path, text in zip(images, business_texts):
	img = Image.open(img_path)
	img = ImageOps.fit(img, phone_size, method=Image.LANCZOS, centering=(0.5, 0.5))
	
	final_img = Image.new("RGB", phone_size, (0, 0, 0))
	
	img_w, img_h = img.size
	final_img.paste(img, ((phone_size[0] - img_w) // 2, (phone_size[1] - img_h) // 2))

	draw = ImageDraw.Draw(final_img)
	text_w = draw.textlength(text, font=font)
	text_h = 10 * 3
	text_position = ((phone_size[0] - text_w) // 2, 50)
	draw.text(text_position, text, font=font, fill=(0, 0, 0))

	resized_path = img_path.replace('.jpeg', '_resized.jpeg')
	final_img.save(resized_path)
	resized_images.append(resized_path)

clip = ImageSequenceClip(resized_images, fps=0.25)

audioclip = AudioFileClip("happy.mp3").subclip(0, 15)
audio = CompositeAudioClip([audioclip])
clip.audio = audio

clip = clip.set_duration(audio.duration)

clip.write_videofile("short.mp4", codec='libx264', fps=24, audio_codec='aac')

# %%
from PIL import Image, ImageOps, ImageDraw, ImageFont
from moviepy.editor import *

def create_video():
	images = [
		'image7.jpeg',
		'image8.jpeg',
		'image9.jpeg',
	]

	# business_texts = [
		# "Bloom Marketing is highly Focused on Customer Experience",
		# "The Bloom Analysis team executes Data-Driven Decision Making",
		# "Bloom Marketing is fueled by Innovation and Adaptation",
		# "Strategic Partnerships drive long-term growth and expansion",
		# "Consistent Branding builds trust and market recognition",
		# "Personalized Marketing enhances customer engagement",
	# ]

	# images = [

	# ]
	business_texts = [
		"I'm Mr. Poopybutthole, and I'm here to save the day... or at least make you laugh!",
		"Wubba lubba dub dub! Did you know that cats have three eyelids?",
		"Oooh, I've got a great idea! Let's make some DIY slime using glue, water, and borax!",
		"Don't worry, I've got this! After all, I'm a master of playing the harmonica with my feet!",
		"Mr. Poopybutthole's got a secret: I can eat an entire pizza by myself in one sitting! Don't tell anyone, but...",
		"Who needs superpowers when you've got a good sense of humor? Am I right, folks? I mean, who needs to fly when you can just laugh your way through life?",
		"Woo-hoo! It's time for a dance party! Who's with me?",
		"Aww, shucks! I just spilled coffee all over my shirt... again! That's just my morning routine, folks!"
	]

	phone_size = (1080, 1920)
	resized_images = []

	font_path = "arial.ttf"
	font_size = 40
	font = ImageFont.truetype(font_path, font_size)

	def wrap_text(text, font, max_width):
		"""Wrap text into multiple lines to fit within max_width."""
		lines = []
		words = text.split()
		line = ""

		for word in words:
			test_line = f"{line} {word}".strip()
			if draw.textlength(test_line, font=font) <= max_width:
				line = test_line
			else:
				lines.append(line)
				line = word
		if line:
			lines.append(line)

		return lines

	for img_path, text in zip(images, business_texts):
		img = Image.open(img_path)
		img = ImageOps.fit(img, phone_size, method=Image.LANCZOS, centering=(0.5, 0.5))
		
		final_img = Image.new("RGB", phone_size, (0, 0, 0))
		
		img_w, img_h = img.size
		final_img.paste(img, ((phone_size[0] - img_w) // 2, (phone_size[1] - img_h) // 2))

		draw = ImageDraw.Draw(final_img)

		max_text_width = phone_size[0] - 100
		lines = wrap_text(text, font, max_text_width)

		line_spacing = 10
		line_height = max(font.getbbox(line)[3] - font.getbbox(line)[1] for line in lines)
		total_text_height = len(lines) * line_height + (len(lines) - 1) * line_spacing

		start_y = 100

		bg_margin = 20
		bg_width = max(draw.textlength(line, font=font) for line in lines) + bg_margin * 2
		bg_height = total_text_height + bg_margin * 2
		bg_position = (
			(phone_size[0] - bg_width) // 2,
			start_y - bg_margin,
			(phone_size[0] + bg_width) // 2,
			start_y + total_text_height + bg_margin
		)
		draw.rectangle(bg_position, fill=(255, 255, 255))

		y_offset = start_y
		for line in lines:
			text_w = draw.textlength(line, font=font)
			text_position = ((phone_size[0] - text_w) // 2, y_offset)
			draw.text(text_position, line, font=font, fill=(0, 0, 0))
			y_offset += line_height + line_spacing

		resized_path = img_path.replace('.jpeg', '_resized.jpeg')
		final_img.save(resized_path)
		resized_images.append(resized_path)

	clip = ImageSequenceClip(resized_images, fps=0.25)

	audioclip = AudioFileClip("happy.mp3").subclip(0, 15)
	audio = CompositeAudioClip([audioclip])
	clip.audio = audio

	clip = clip.set_duration(audio.duration)
	return clip

clip = create_video()

clip.write_videofile("short.mp4", codec='libx264', fps=24, audio_codec='aac')



# %%
import pyttsx3

engine = pyttsx3.init()
text = "I am a poopy butthole."
filename = "my_audio.mp3"

engine.save_to_file(text, filename)
engine.runAndWait()
print(f"Audio saved to {filename}")
engine.stop()

# %%