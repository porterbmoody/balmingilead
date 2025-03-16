
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

# create_video(images, texts)

# %%



#%%

# from gtts import gTTS
# import os

# text = "I am the king. Strive for greatness."
# tts = gTTS(text=text, lang='en', slow=False)
# tts.save("lebron_style.mp3")

# # Play the audio (works on Mac/Linux)
# os.system("mpg321 lebron_style.mp3")

#%%

# audio = elevenlabs.generate(text = "hi im porter", voice = "bella")

# elevenlabs.play(audio)




# import elevenlabs
# from elevenlabs import play
# from elevenlabs.client import ElevenLabs

# client = ElevenLabs(
#   api_key=api_key,
# )

# audio = client.generate(
#   text="Hello!!",
#   voice="Rachel",
#   model="eleven_multilingual_v2"
# )
# play(audio)

# elevenlabs.play(audio)

#%%

# text = "Hey there! Are you investigating The Church of Jesus Christ of Latter-day Saints? I'm excited to share with you some top reasons why I believe the LDS Church is plausibly true. Reason 1: The Book of Mormon. This book is another testament of Jesus Christ and provides a historical and spiritual record of ancient peoples in the Americas. Its complexity, depth, and consistency make it a remarkable work that has been a source of spiritual guidance for millions. Reason 2: Joseph Smith's First Vision. In 1820, Joseph Smith, the founder of the LDS Church, reported having a vision of God the Father and Jesus Christ. This event is seen as a pivotal moment in the restoration of the gospel and has been a source of inspiration for generations. Reason 3: Fulfilled Prophecies. Many ancient prophecies, including those in the Bible, have been fulfilled in the restoration of the Church. This includes the restoration of the priesthood, the gathering of Israel, and the building of temples. Reason 4: Personal Revelation. Members of the LDS Church believe in the power of personal revelation. Through prayer, scripture study, and obedience to God's commandments, individuals can receive their own witness of the truthfulness of the Church. Thanks for watching! These are just a few reasons why I believe the LDS Church is plausibly true. If you're interested in learning more, I invite you to visit (link unavailable) or talk to a representative from the Church."


#%%

from moviepy.editor import ImageSequenceClip, AudioFileClip
from PIL import Image

images = ["book of mormon.jpeg", "alma.jpeg", 'smith.jpeg', 'river.jpeg']
target_size = (1280, 720)

resized_images = []
for img_path in images:
	img = Image.open(img_path)
	img = img.resize(target_size)
	resized_path = f"resized_{img_path}"
	img.save(resized_path)
	resized_images.append(resized_path)

	print(f"{resized_path} size: {img.size}")

unique_sizes = set(Image.open(img).size for img in resized_images)
print(f"Unique image sizes: {unique_sizes}")
print(resized_images)

if len(unique_sizes) > 1:
	print("Error: Not all images are the same size. Please check the resizing step.")
	exit()

audio = AudioFileClip("daniel.mp3")

image_duration = audio.duration / len(resized_images)

video = ImageSequenceClip(resized_images, durations=[image_duration] * len(resized_images))

video = video.set_audio(audio)

video.write_videofile("output_video.mp4", fps=1)
#%%

import elevenlabs
from elevenlabs.client import ElevenLabs
from elevenlabs import *
from moviepy.editor import *
from gtts import gTTS
import os


def create_audio(text, name, path):
	voice_ids = {'Aria': '9BWtsMINqrJLrRacOk9x',
			 'Roger': 'CwhRBWXzGAHq8TQ4Fs17',
			'Sarah': 'EXAVITQu4vr4xnSDxMaL',
			'Laura': 'FGY2WhTYpPnrIDTdsKH5',
			'Charlie': 'IKne3meq5aSn9XLyUdCD',
			'George': 'JBFqnCBsd6RMkjVDRZzb',
			'Callum': 'N2lVS1w4EtoT3dr4eOWO',
			'River': 'SAz9YHcvj6GT2YYXdXww',
			'Liam': 'TX3LPaxmHKxFdv7VOQHJ',
			'Charlotte': 'XB0fDUnXU5powFXDhCwa',
			'Alice': 'Xb7hH8MSUJpSbSDYk0k2',
			'Matilda': 'XrExE9yKIg1WjnnlVkGX',
			'Will': 'bIHbv24MWmeRgasZH58o',
			'Jessica': 'cgSgspJ2msm6clMCkdW9',
			'Eric': 'cjVigY5qzO86Huf0OWal',
			'Chris': 'iP95p4xoKVk53GoZ742B',
			'Brian': 'nPczCjzI2devNBz1zQrb',
			'Daniel': 'onwK4e9ZLuTAKqWW03F9',
			'Lily': 'pFZP5JQG7iQjIQuC4Bku',
			'Bill': 'pqHfZKP75CvOlQylNhV4'
			}

	api_key = 'sk_634beddb49f45a6b7f6261e349592ed6195d0769379f2b6a'

	client = ElevenLabs(
	api_key=api_key,
	)

	# text = "1. Geography and Place Names: The Book of Mormon describes a specific geography, including the River Sidon, the Hill Cumorah, and the land of Nephi. Archaeological discoveries have confirmed the existence of similar place names and geographic features in Mesoamerica. 2. Ancient Cities and Ruins: The Book of Mormon mentions various cities, including Zarahemla, Bountiful, and Jacobugath. Archaeologists have discovered ancient cities and ruins in Mesoamerica that match the descriptions in the Book of Mormon."
	audio = client.text_to_speech.convert(
		text=text,
		voice_id=voice_ids[name],
		model_id="eleven_multilingual_v2",
		output_format="mp3_44100_128",
	)

	save(audio, path + '.mp3')
# texts = [
	# "Galatians 1:8 states: But though we, or an angel from heaven, preach any other gospel unto you than that which we have preached unto you, let him be accursed.",
	# "Some critics of The Church of Jesus Christ of Latter-day Saints (LDS Church) have used this verse to argue that the LDS Church's gospel is different from the gospel preached by Paul and the apostles, and therefore, the LDS Church is accursed.",
	# "Such a claim is unsustainable for the following reasons:",
	# "1. Context: Understand the context of Galatians 1:8. Paul was addressing a specific issue in the Galatian church, where false teachers were preaching a different gospel that emphasized circumcision and the law.",
	# "2. Definition of Gospel: The LDS Church defines the gospel as the good news of Jesus Christ's atonement, resurrection, and the plan of salvation. This definition is consistent with the Bible and the teachings of the apostles.",
	# "3. Restoration: The LDS Church teaches that the gospel was restored through Joseph Smith, including the priesthood, ordinances, and doctrine. This restoration did not change the fundamental message of the gospel but rather clarified and expanded upon it.",
# 	"4. Additional Scripture: The LDS Church accepts additional scripture, including the Book of Mormon, Doctrine and Covenants, and Pearl of Great Price. These scriptures do not contradict the Bible but rather provide additional witnesses of Jesus Christ and the gospel.",
# 	"5. Authority: The LDS Church emphasizes the importance of authority and the priesthood. The church teaches that the priesthood was restored through Joseph Smith, allowing for the performance of ordinances and the governance of the church.",
# 	"6. Interpretation: The LDS Church interprets Galatians 1:8 as a warning against preaching a different gospel that contradicts the fundamental message of Jesus Christ. The church teaches that its gospel is consistent with the Bible and the teachings of the apostles.",
# 	"In summary, the LDS Church responds to Galatians 1:8 by emphasizing the importance of understanding the context, defining the gospel, and recognizing the restoration of the gospel through Joseph Smith. The church teaches that its gospel is consistent with the Bible and the teachings of the apostles.",
# ]

# texts = [
	# 'Chiasmus is a literary structure in which words or phrases are arranged in a reverse order.',
	# 'In the 1960s, a scholar named John Welch discovered that the Book of Mormon contains numerous examples of Chiasmus. This was a significant discovery, as Chiasmus was not well-known in the 19th century when the Book of Mormon was translated.',
	# 'Welch and other scholars have analyzed the Chiasmus in the Book of Mormon and found that it is a sophisticated and complex literary structure. The Chiasmus in the Book of Mormon is often multi-level, with smaller chiasms nested within larger ones.',
	# 'The presence of Chiasmus in the Book of Mormon has several implications: 1. It suggests that the Book of Mormon is an ancient text, as Chiasmus was a common literary structure in ancient Hebrew and Greek literature. 2. It implies that the Book of Mormon was written by multiple authors, as the Chiasmus is not consistent throughout the book. 3. It provides evidence that the Book of Mormon was translated by Joseph Smith, rather than written by him, as the Chiasmus is a complex literary structure that would have been difficult for Joseph Smith to create on his own.',
	# 'The presence of Chiasmus in the Book of Mormon is a significant evidence of its authenticity and ancient origins. It suggests that the Book of Mormon is a complex and sophisticated text that was written by multiple authors and translated by Joseph Smith.',
# ]

texts = [
    "Chiasmus is a literary structure where words/phrases are arranged in reverse order, adding complexity and meaning.",
    "In the 1960s, scholar John Welch discovered Chiasmus in the Book of Mormon, a significant find since it was unknown in the 19th century.",
    "Analysis reveals the Book of Mormon's Chiasmus is sophisticated, multi-level, and nested, indicating a complex literary structure.",
    "Chiasmus in the Book of Mormon implies: ancient origins, multiple authors, and Joseph Smith's translation, not authorship.",
    "Chiasmus is significant evidence of the Book of Mormon's authenticity and ancient origins, showcasing its complexity and sophistication."
]
folder = 'chiasmus/'
for i, text in enumerate(texts):
	# create_audio(text, 'Roger', 'chiasmus/' + str(i))
	# text = "Hello, this is another test."
	tts = gTTS(text=text, lang='en', tld='ie')
	tts.save(folder + str(i) + ".mp3")
image_files = [f'images/chiasmus{i}.jpeg' for i in range(len(os.listdir(folder)))]
audio_files = [folder + f'{i}.mp3' for i in range(len(os.listdir(folder)))]

narration_clips = [AudioFileClip(audio) for audio in audio_files]
iphone_resolution = (1080*2, 1080)

image_clips = []
for image, audio in zip(image_files, narration_clips):
	image = ImageClip(f'{image}').set_duration(audio.duration).resize(iphone_resolution)
	image_clips.append(image)

# image_files = ['image0.jpeg', 'image1.jpeg', 'image2.jpeg', 'image3.jpeg']#, , 'image3.jpeg', 'image4.jpeg', 'image5.jpeg', 'image6.jpeg', 'image7.jpeg', 'image8.jpeg', 'image9.jpeg']
# audio_files = ['galations/Daniel0.mp3', 'galations/Daniel1.mp3', 'galations/Daniel2.mp3', 'galations/Daniel3.mp3']# for i in range(len(image_files))]

# narration_clips = [AudioFileClip(audio) for audio in audio_files]
# image_clips = [ImageClip('images/' + img).set_duration(narration_clips.duration) for img, narration_clips in zip(image_files, narration_clips)]
video = concatenate_videoclips(image_clips)

combined_audio = concatenate_audioclips(narration_clips)
video = video.set_audio(combined_audio)
video.write_videofile("chiasmus_vid.mp4", codec='libx264', fps=24, audio_codec='aac')

#%%

image_files = ['verse.jpeg', 'image1.jpeg', 'image2.jpeg', 'image3.jpeg', 'image4.jpeg']
audio_files = [f'galations/Daniel{i}.mp3' for i in range(len(image_files))]

narration_clips = [AudioFileClip(audio) for audio in audio_files]

image_clips = [ImageClip(f'images/{image}').set_duration(audio.duration) for image, audio in zip(image_files, narration_clips)]

video_clips = [CompositeVideoClip([image.set_audio(audio)]) for image, audio in zip(image_clips, narration_clips)]

final_video = concatenate_videoclips(video_clips)

final_video.write_videofile('galations_video.mp4', fps=24)

# %%

import pyttsx3

text = "Hello, this is another test."
engine = pyttsx3.init()

# List available voices and pick a male voice
voices = engine.getProperty('voices')
for voice in voices:
	print(voice.id, voice.name, voice.gender)  # Useful for identifying voices

# Set a male voice (you may need to adjust the index based on your system)
engine.setProperty('voice', voices[0].id)  # Change index if needed

engine.save_to_file(text, "output.mp3")
engine.runAndWait()
#%%

from pytubefix import YouTube
from moviepy.editor import *
import os

def download_audio(url):
	video = YouTube('https://www.youtube.com/watch?v='+url)
	original_title = video.title.replace('?', '').replace('|','').replace('&', 'and').replace('#', '').replace('/','_')
	filename = f'{original_title}.wav'
	audio_stream = video.streams.get_audio_only().download()
	# audio_stream = video.streams.get_highest_resolution().download()
	audio = AudioFileClip(audio_stream)
	audio.write_audiofile(filename)
	os.remove(audio_stream)


urls = [
	'9ZS6v9fQv5M',
	'bTACekXFmWk',
]

for url in urls:
	download_audio(url)


#%%