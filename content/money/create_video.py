
#%%
import pyttsx3
from PIL import Image, ImageOps, ImageDraw, ImageFont
from moviepy.editor import *
from gtts import gTTS

engine = pyttsx3.init()

def generate_audio(text, filename):
	# engine.save_to_file(text, filename)
	# engine.runAndWait()

	tts = gTTS(text=text, lang='en', tld='ie')
	tts.save(filename)

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

		max_text_width = phone_size[0] - 200
		lines = wrap_text(text, font, max_text_width)

		line_spacing = 10
		line_height = max(font.getbbox(line)[3] - font.getbbox(line)[1] for line in lines)
		total_text_height = len(lines) * line_height + (len(lines) - 1) * line_spacing

		start_y = phone_size[1] - total_text_height - 1400

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

	audio_background = AudioFileClip('swag.wav')
	final_audio = CompositeAudioClip([video.audio, audio_background])
	final_clip = video.set_audio(final_audio)

	final_clip.write_videofile("short.mp4", codec='libx264', fps=24, audio_codec='aac')

texts = [
	'3 Irrefutable Evidences for the Book of Mormon',
	"""1. Chiasmus in the Text\nChiasmus is a literary structure commonly found in ancient Hebrew and other Near Eastern texts. It involves a mirrored or inverted parallelism, where ideas are introduced in a certain order and then repeated in reverse. This structure was used to aid oral transmission and reinforce key messages.\nOne of the strongest examples of chiasmus in the Book of Mormon is Alma 36, where Alma recounts his dramatic conversion. The structure follows this pattern:\nA. Alma’s afflictions and suffering\nB. Recalling his father’s prophecies about Christ\nC. Being racked with torment for sins\nD. Calling upon Jesus for mercy\nC'. Joy replaces torment\nB'. Recognizing the truth of Christ’s role\nA'. Rejoicing in salvation and desiring to share it\nThis complex pattern suggests a deliberate literary construction rather than random storytelling. Since Joseph Smith had limited formal education and chiasmus wasn’t widely recognized in 19th-century America, some scholars argue that this is evidence of an ancient Hebrew influence in the Book of Mormon.""",
	"""2. Arabian Geography & Nahom\nThe Book of Mormon states that Lehi’s family traveled through the Arabian Peninsula and buried Ishmael in a place called Nahom (1 Nephi 16:34). This location is significant for a few reasons:\nNHM Inscription Discovery\nIn the 1990s, archaeologists found ancient inscriptions in Yemen dating back to around 700-600 BCE (the time Lehi’s family would have traveled) that reference a tribal region called NHM (which corresponds phonetically with Nahom in Semitic languages, which often omit vowels in written form).\nTrade Routes & Burial Customs\nThe NHM region in ancient Arabia was known for being near major incense trade routes and had burial sites, which aligns with the Book of Mormon’s mention of Ishmael being buried there. Lehi’s family also reportedly turned "nearly eastward" from Nahom (1 Nephi 17:1), which corresponds with the geography leading to the coast where Nephi’s group could have built a ship.\nUnlikely to Be Known by Joseph Smith\nThe Arabian Peninsula was largely unexplored by Western scholars in the early 19th century, and the specific name NHM would not have been available in sources accessible to Joseph Smith. The discovery of this location after the Book of Mormon was published is seen by some as evidence that the book describes real-world places.""",
	"""3. Mesoamerican Cultural Parallels\nAlthough the Book of Mormon does not explicitly name its setting, many LDS researchers believe that the Nephites and Lamanites lived in ancient Mesoamerica (southern Mexico, Guatemala, and nearby regions). There are several cultural and historical parallels between Book of Mormon societies and pre-Columbian civilizations:\nCity-Building & Complex Societies\nThe Nephites and Lamanites built cities with walls, temples, roads, and public buildings (Mosiah 7:10, Alma 48:8). This aligns with evidence of advanced city-building cultures in Mesoamerica, such as the Maya and Olmec, who had complex urban centers.\nTemple Worship\nThe Nephites constructed temples "after the manner of Solomon" (2 Nephi 5:16). While the Maya and other Mesoamerican cultures did not follow Jewish temple practices, they did build step-pyramids used for religious ceremonies, which some LDS scholars see as a parallel.\nWarfare & Weapons\nThe Book of Mormon describes wars involving large armies, armor, and fortifications (Alma 49:4-8). Mesoamerican civilizations also had frequent warfare, used obsidian-bladed weapons similar to those described in the Book of Mormon (e.g., the macuahuitl, which resembles a sword), and built defensive structures.\nHebrew-Like Traditions\nSome Mesoamerican legends and myths contain themes that seem to echo biblical or Book of Mormon teachings, such as a bearded white god (Quetzalcoatl) who resembles descriptions of Christ’s visit to the Nephites in 3 Nephi 11.""",
]

	# '1. The Bibles oldest surviving manuscript: The oldest surviving manuscript of the Bible is the Dead Sea Scrolls, which date back to around 150 BCE. These scrolls were discovered in 1947 in Qumran, near the Dead Sea, and contain fragments of every book of the Hebrew Bible, as well as other ancient texts.',
	# '2. The Bibles most translated verse: The most translated verse in the Bible is John 3:16, which has been translated into over 1,000 languages.',
	# '3. The Bibles mysterious "lost" books: The Bible mentions several books that are no longer extant, including the "Book of Jasher" (Joshua 10:13, 2 Samuel 1:18), the "Book of the Wars of the Lord" (Numbers 21:14), and the "Book of the Acts of Solomon" (1 Kings 11:41). These lost books are the subject of much speculation and debate among scholars and biblical enthusiasts.',
	# '3 strong evidences for The Book of Mormon',
	# '1. Metalworking: The Book of Mormon describes the Nephites as skilled metalworkers (1 Nephi 17:16, 2 Nephi 5:15), which is consistent with archaeological findings in Mesoamerica.',
	# '2. Swords and cimeters: The Book of Mormon mentions swords and cimeters (Enos 1:20, Alma 2:12), which were unknown in pre-Columbian America until the discovery of metal artifacts in Mesoamerica.',
	# '3. Horses and other animals: The Book of Mormon describes horses, cattle, and other animals (Enos 1:21, 3 Nephi 3:22), which were present in the Americas during the time period described.',
	# 'uni0.jpeg',
	# 'uni1.jpeg',
	# 'uni2.jpeg',
	# 'uni3.jpeg',
	# 'uni4.jpeg',
	# 'uni5.jpeg',
	# 'uni6.jpeg',
	# "save0.jpeg",
	# "save1.jpeg",
	# "save2.jpeg",
	# "save3.jpeg",
	# "save4.jpeg",
	# "save5.jpeg",
	# "save6.jpeg",
	# "save7.jpeg",
	# "save8.jpeg",
	# "save9.jpeg",
	# "save10.jpeg",

images = [
	'book of mormon.jpeg',
	'chiasmus.jpg',
	'nahom.jpeg',
	'mesoamerican culture.jpeg',
	# 'metal.jpeg',
	# 'sword.jpeg',
	# 'horse.jpg',
]
# '5 Mind-Blowing Facts About the Universe',
# 'Fact #1: The Universe is Still Expanding\n1. The Big Bang theory suggests that the universe began as a single point.\n2. This point expanded rapidly around 13.8 billion years ago.\n3. The universe is still growing, with galaxies moving away from each other.',
# 'Fact #2: There are More Stars than Grains of Sand\n1. The observable universe contains over 200 billion galaxies.\n2. Each galaxy contains billions of stars.\n3. The number of stars in the universe is estimated to be around 100 billion trillion.',
# 'Fact #3: Space is Filled with Mysterious Sounds\n1. NASA has recorded strange sounds in space, such as whistles and chirps.\n2. These sounds are thought to be caused by solar winds and magnetic fields.\n3. The sounds are still not fully understood and are the subject of ongoing research.',
# 'Fact #4: The International Space Station is Huge\n1. The ISS orbits the Earth at an altitude of around 250 miles.\n2. It is the largest human-made object in space.\n3. The ISS is so big that it can be seen from Earth with the naked eye.',
# 'Fact #5: There are Planets Made Entirely of Diamond\n1. Scientists have discovered planets that are thought to be composed primarily of diamond.\n2. These planets are formed when carbon-rich stars explode.\n3. The diamond planets are still purely theoretical and have yet to be directly observed.',

# texts = [
# 	'3 Proven Ways to Boost Your Income',
# 	'Tip 1: Start a Side Hustle\n1. Identify your passions: Reflect on your interests and skills.\n2. Research opportunities: Explore platforms like Etsy, eBay, or Upwork.\n3. Take action: Start small and scale your side hustle.',
# 	'Tip 2: Invest in Personal Development\n1. Learn in-demand skills: Focus on emerging technologies like AI, data science, or cybersecurity.\n2. Attend workshops and conferences: Network with professionals and stay updated on industry trends.\n3. Read books and articles: Continuously educate yourself on personal finance, entrepreneurship, and career development.',
# 	'Tip 3: Participate in the Gig Economy\n1. Sign up with gig platforms: Join companies like Uber, Lyft, DoorDash, or Postmates.\n2. Offer services on freelance platforms: Use platforms like Fiverr, Freelancer, or TaskRabbit.\n3. Monetize your skills: Offer high-demand services like pet-sitting, house-sitting, or tutoring.',
# ]

# "#1: Track Your Spending. You can’t save money if you don’t know where it’s going. Use budgeting apps like Mint or YNAB, or even a simple spreadsheet to track every dollar. You’d be surprised how much those ‘little’ purchases add up.",
# "#2: Cancel Unused Subscriptions. Look through your bank statements and cancel those subscriptions you don’t really use. Do you really need five different streaming services?",
# "#3: Use Cashback & Rewards. Apps like Rakuten, Honey, and credit card reward programs can give you cash back on things you already buy. It’s free money—why not take it?",
# "#4: Meal Plan & Cook at Home. Eating out is one of the biggest money drains. Try meal prepping for the week—you’ll save money and eat healthier. Plus, homemade coffee? Way cheaper than Starbucks!",
# "#5: Buy Generic Brands. Most store-brand products are just as good as name brands but cost way less. Give them a try and see if you really notice a difference.",
# "#6: Negotiate Your Bills. Call your internet, phone, or insurance provider and ask for a lower rate. You’d be surprised how often they’ll cut your bill just to keep you as a customer.",
# "#7: Use Public Transport or Carpool. Gas and maintenance add up. If possible, use public transit, bike, or carpool to save money on commuting. Even a couple of days a week can make a big difference.",
# "#8: Buy Secondhand. From clothes to furniture, buying used can save you hundreds of dollars a year. Check out thrift stores, Facebook Marketplace, or Craigslist before buying new.",
# "#9: Automate Your Savings. Set up automatic transfers to your savings account so you ‘pay yourself first.’ Even $10 a week adds up over time!",
# '#10: Find Free Entertainment. Instead of expensive nights out, look for free activities—hiking, library events, or community festivals. Fun doesn’t have to be expensive!',

create_video(images, texts)

# %%

# %%
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
# 	"6. Interpretation: The LDS Church interprets Galatians 1:8 as a warning against preaching a different gospel that contradicts the fundamental message of Jesus Christ. The church teaches that its gospel is consistent with the Bible and the teachings of the apostles.",
# 	"In summary, the LDS Church responds to Galatians 1:8 by emphasizing the importance of understanding the context, defining the gospel, and recognizing the restoration of the gospel through Joseph Smith. The church teaches that its gospel is consistent with the Bible and the teachings of the apostles.",
# ]

# texts = [
	# 'Chiasmus is a literary structure in which words or phrases are arranged in a reverse order.',
	# 'The presence of Chiasmus in the Book of Mormon is a significant evidence of its authenticity and ancient origins. It suggests that the Book of Mormon is a complex and sophisticated text that was written by multiple authors and translated by Joseph Smith.',
# ]

texts = [
    "Chiasmus is a literary structure where words/phrases are arranged in reverse order, adding complexity and meaning.",
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


from huggingface_hub import snapshot_download

snapshot_download("SparkAudio/Spark-TTS-0.5B", local_dir="pretrained_models/Spark-TTS-0.5B")


