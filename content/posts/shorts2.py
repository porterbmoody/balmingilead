
#%%
import pyttsx3
from PIL import Image, ImageOps, ImageDraw, ImageFont
from moviepy.editor import *

engine = pyttsx3.init()

def generate_audio(text, filename):
	engine.save_to_file(text, filename)
	engine.runAndWait()

def create_video(images, texts):

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
	image_paths = ["images/" + image_path for image_path in images]
	for i, (image_path, text) in enumerate(zip(image_paths, texts)):
		img = Image.open(image_path)
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

		resized_path = image_path.replace('.jpeg', '_resized.jpeg')
		final_img.save(resized_path)
		resized_images.append(resized_path)

		audio_path = f"audio/audio_{i}.mp3"
		generate_audio(text, audio_path)
		narration_clip = AudioFileClip(audio_path)
		narration_clips.append(narration_clip)
	# image_clips = []
	# for img in resized_images:
		# image_clips.append(ImageClip(img).set_duration(5))
	image_clips = [ImageClip(img).set_duration(narration_clips.duration) for img, narration_clips in zip(resized_images, narration_clips)]
	video = concatenate_videoclips(image_clips)

	combined_audio = concatenate_audioclips(narration_clips)
	video = video.set_audio(combined_audio)

	# audioclip = AudioFileClip("thought.wav").subclip(0+11, video.duration+11)
	# audio = CompositeAudioClip([audioclip])
	# video.audio = audio

	video.write_videofile("short.mp4", codec='libx264', fps=24, audio_codec='aac')

images = [
	"musk1.jpeg",
	"musk2.jpeg",
	"musk3.jpeg",
	"musk4.jpeg",
	# "trump1.jpeg",
	# "trump2.jpeg",
	# "trump3.jpeg",
	# "trump4.jpeg",
	# 'office1.jpeg',
	# 'office2.jpeg',
	# 'office3.jpeg',
	# 'office4.jpeg',
	# 'office6.jpeg',
	# 'poop1.jpeg',
	# 'poop2.jpeg',
	# 'poop3.jpeg',
	# 'poop4.jpeg',
	# 'poop5.jpeg',
	# 'poop6.jpeg',
	# 'jesus1.jpeg',
	# 'jesus2.jpeg',
	# 'jesus3.jpeg',
	# 'jesus4.jpeg',
	# 'jesus5.jpeg',
	# 'jesus6.jpeg',
	# 'jesus7.jpeg',
	# 'jesus8.jpeg',
	# '1st vision.jpeg',
	# 'jesus9.jpeg',
	# 'jesus10.jpeg',
	# 'nelson.jpeg',
]

texts = [
	"When something is important enough, you do it even if the odds are not in your favor. Or you might just build rockets and cars instead",
	"Failure is an option here. If things are not failing, you are not innovating enough",
	"I would like to allocate more time to space travel, though. I need to find a planet. That's why I need to carve out just a little more time",
	"The universe is the answer, what was the question",
	# "I'm intelligent. Some people would say I'm very, very, very intelligent",
	# "Why would Kim Jong-un insult me by calling me 'old,' when I would NEVER call him 'short and fat?",
	# "I won't do anything to take care of them. I'll supply funds and she'll take care of the kids",
	# 'Let\'s touch base',
	# 'I\'ll loop you in',
	# 'Can we discuss offline?',
	# 'I\'m on the same page',
	# "Matthew 7:7 Ask of God, and it shall be given you",
	# "Moses 1:6 Moses, thou art in the similitude of mine Only Begotten",
	# "Moses 1:3 Behold, I am the Lord God Almighty, and Endless is my name",
	# "Jeremiah 17:7 Blessed is the man that trusteth in the Lord, and whose hope the Lord is.",
	# "Matthew 11:28 Come unto me, all ye that labour and are heavy laden, and I will give you rest.",
	# "Philippians 4:13 I can do all things through Christ which strengtheneth me.",
	# "2 Nephi 25:23 for it is by grace that we are saved, after all we can do.",
	# "Jacob 4:8 For with God nothing shall be impossible.",
	# "When the light rested upon me I saw two Personages, whose brightness and glory defy all description",
	# "D&C 84:45 For the word of the Lord is truth, and whatsoever is truth is light, and whatsoever is light is Spirit, even the Spirit of Jesus Christ.",
	# "Abraham 3:26 and they who keep their second estate shall have glory added upon their heads for ever and ever.",
	# "The answer is always Jesus Christ",
	# "I'm Mr. Poopybutthole, and I'm here to save the day... or at least make you laugh!",
	# "They say laughter’s the best medicine… but have you tried tacos? Just sayin'!",
	# "Woo-hoo! It's time for a dance party! Who's with me?",
	# "Ever tried juggling spaghetti? Neither have I… but I feel like today’s the day!",
	# "Ooo-wee! Let’s turn up the music and dance like no one’s watching… except my dog. He’s definitely judging me.",
	# "I may not be a superhero, but I once parallel parked on the first try — so, you know, pretty close!",
	# "Ooo-wee! I just signed up for yoga class… turns out I’m *way* better at the napping part!",
	# "Who’s ready for an adventure? Or at least a snack break? I vote snack break!",
	# "Don't worry, I've got this! After all, I'm a master of playing the harmonica with my feet!",
	# "Oooh, I've got a great idea! Let's make some DIY slime using glue, water, and borax!",
	# "Who needs superpowers when you've got a good sense of humor? Am I right, folks? I mean, who needs to fly when you can just laugh your way through life?",
	# "Wubba lubba dub dub! Did you know that cats have three eyelids?",
	# "I once tried to build a treehouse… now I just have a very confused tree with a lot of nails in it!",
	# "I put my pants on one leg at a time… except sometimes I fall over. It’s part of my charm!",
	# "Mr. Poopybutthole's got a secret: I can eat an entire pizza by myself in one sitting! Don't tell anyone, but...",
	# "Aww, shucks! I just spilled coffee all over my shirt... again! That's just my morning routine, folks!",
]

create_video(images, texts)

# %%



#%%

