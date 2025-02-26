
#%%
import pyttsx3
from PIL import Image, ImageOps, ImageDraw, ImageFont
from moviepy.editor import *

engine = pyttsx3.init()


def generate_audio(text, filename):
	engine.save_to_file(text, filename)
	engine.runAndWait()


def create_video():
	images = [
		'jesus.jpeg',
		'jesus2.jpeg',
		'jesus3.jpeg',
		'jesus4.jpeg',
		'jesus2.jpeg',
		'jesus5.jpeg',
		'jesus6.jpeg',
		'jesus7.jpeg',
		'nelson.jpeg',
	]

	texts = [
		"Matthew 7:7 Ask of God, and it shall be given you",
		"Moses 1:6 Moses, thou art in the similitude of mine Only Begotten",
		"Moses 1:3 Behold, I am the Lord God Almighty, and Endless is my name",
		"Jeremiah 17:7 Blessed is the man that trusteth in the Lord, and whose hope the Lord is.",
		"Matthew 11:28 Come unto me, all ye that labour and are heavy laden, and I will give you rest.",
		"Philippians 4:13 I can do all things through Christ which strengtheneth me.",
		"2 Nephi 25:23 for it is by grace that we are saved, after all we can do.",
		"Jacob 4:8 For with God nothing shall be impossible.",
		"The Answer is Always Jesus Christ",
	]

	phone_size = (1080, 1920)
	resized_images = []
	narration_clips = []

	font_path = "arial.ttf"
	font_size = 40
	font = ImageFont.truetype(font_path, font_size)

	def wrap_text(text, font, max_width):
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

	for i, (img_path, text) in enumerate(zip(images, texts)):
		img = Image.open(img_path)
		img = ImageOps.fit(img, phone_size, method=Image.LANCZOS, centering=(0.5, 0.5))

		final_img = Image.new("RGB", phone_size, (0, 0, 0))

		img_w, img_h = img.size
		final_img.paste(img, ((phone_size[0] - img_w) // 2, (phone_size[1] - img_h) // 2))

		draw = ImageDraw.Draw(final_img)

		max_text_width = phone_size[0] - 500
		lines = wrap_text(text, font, max_text_width)

		line_spacing = 10
		line_height = max(font.getbbox(line)[3] - font.getbbox(line)[1] for line in lines)
		total_text_height = len(lines) * line_height + (len(lines) - 1) * line_spacing

		start_y = phone_size[1] - total_text_height - 250

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

		audio_path = f"audio_{i}.mp3"
		generate_audio(text, audio_path)
		narration_clip = AudioFileClip(audio_path)
		narration_clips.append(narration_clip)
	image_clips = []
	for img in resized_images:
		image_clips.append(ImageClip(img).set_duration(5))
	# image_clips = [ImageClip(img).set_duration(duration) for img, duration in zip(resized_images, lengths)]
	video = concatenate_videoclips(image_clips)

	# combined_audio = concatenate_audioclips(narration_clips)
	# video = video.set_audio(combined_audio)

	audioclip = AudioFileClip("kolob.wav").subclip(0, video.duration)
	audio = CompositeAudioClip([audioclip])
	video.audio = audio

	video.write_videofile("short.mp4", codec='libx264', fps=24, audio_codec='aac')

create_video()

# %%
