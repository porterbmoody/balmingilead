#%%
# import elevenlabs
# from elevenlabs.client import ElevenLabs
# from elevenlabs import *
from moviepy.editor import *
from gtts import gTTS
import os

texts = [
	'3 Evidences for the Book of Mormon',
	"""1. Chiasmus. Chiasmus is a literary structure commonly found in ancient Hebrew and other Near Eastern texts. It involves a mirrored or inverted parallelism where ideas are introduced in a certain order and then repeated in reverse. This structure was used to aid oral transmission and reinforce key messages.""",
	"""One of the strongest examples of chiasmus in the Book of Mormon is Alma 36 where Alma recounts his dramatic conversion. The structure follows this pattern:""",
	"""A. Alma’s afflictions and suffering B. Recalling his father’s prophecies about Christ C. Being racked with torment for sins D. Calling upon Jesus for mercy C'. Joy replaces torment\nB'. Recognizing the truth of Christ’s role A'. Rejoicing in salvation and desiring to share it\nThis complex pattern suggests a deliberate literary construction rather than random storytelling. Since Joseph Smith had limited formal education and chiasmus wasn’t widely recognized in 19th-century America, some scholars argue that this is evidence of an ancient Hebrew influence in the Book of Mormon.""",
	"""2. Arabian Geography & Nahom. The Book of Mormon states that Lehi’s family traveled through the Arabian Peninsula and buried Ishmael in a place called Nahom (1 Nephi 16:34). This location is significant for a few reasons: """,
	"""NHM Inscription Discovery In the 1990s, archaeologists found ancient inscriptions in Yemen dating back to around 700-600 BCE (the time Lehi’s family would have traveled) that reference a tribal region called NHM (which corresponds phonetically with Nahom in Semitic languages, which often omit vowels in written form).\nTrade Routes & Burial Customs\nThe NHM region in ancient Arabia was known for being near major incense trade routes and had burial sites, which aligns with the Book of Mormon’s mention of Ishmael being buried there. Lehi’s family also reportedly turned "nearly eastward" from Nahom (1 Nephi 17:1), which corresponds with the geography leading to the coast where Nephi’s group could have built a ship.\nUnlikely to Be Known by Joseph Smith\nThe Arabian Peninsula was largely unexplored by Western scholars in the early 19th century, and the specific name NHM would not have been available in sources accessible to Joseph Smith. The discovery of this location after the Book of Mormon was published is seen by some as evidence that the book describes real-world places.""",
	"""3. Mesoamerican Cultural Parallels. Although the Book of Mormon does not explicitly name its setting, many LDS researchers believe that the Nephites and Lamanites lived in ancient Mesoamerica (southern Mexico, Guatemala, and nearby regions).""",
	"""There are several cultural and historical parallels between Book of Mormon societies and pre-Columbian civilizations: City-Building & Complex Societies The Nephites and Lamanites built cities with walls, temples, roads, and public buildings (Mosiah 7:10, Alma 48:8). This aligns with evidence of advanced city-building cultures in Mesoamerica, such as the Maya and Olmec, who had complex urban centers. Temple Worship The Nephites constructed temples "after the manner of Solomon" (2 Nephi 5:16). While the Maya and other Mesoamerican cultures did not follow Jewish temple practices, they did build step-pyramids used for religious ceremonies, which some LDS scholars see as a parallel.\nWarfare & Weapons\nThe Book of Mormon describes wars involving large armies, armor, and fortifications (Alma 49:4-8). Mesoamerican civilizations also had frequent warfare, used obsidian-bladed weapons similar to those described in the Book of Mormon (e.g., the macuahuitl, which resembles a sword), and built defensive structures. Hebrew-Like Traditions Some Mesoamerican legends and myths contain themes that seem to echo biblical or Book of Mormon teachings, such as a bearded white god (Quetzalcoatl) who resembles descriptions of Christ’s visit to the Nephites in 3 Nephi 11.""",
]
folder = 'audio/'
for i, text in enumerate(texts):
	# create_audio(text, 'Roger', 'chiasmus/' + str(i))
	# text = "Hello, this is another test."
	tts = gTTS(text=text, lang='en', tld='ie')
	tts.save(folder + str(i) + ".mp3")
image_files = [f'images/chiasmus{i}.jpeg' for i in range(len(os.listdir(folder)))]
image_files = [
	'bom.jpeg',
	'chias_pattern.jpeg',
	# 'alma.jpeg',
	'alma3.jpeg',
	'chi_pattern.jpeg',
	'nahom.jpeg',
	'nahom2.jpeg',
	'mesoamerica.jpeg',
	'building.jpeg',
	# 'mesoamerican culture.jpeg',
	# 'metal.jpeg',
	# 'sword.jpeg',
	# 'horse.jpg',
]
audio_files = [folder + f'{i}.mp3' for i in range(len(os.listdir(folder)))]

narration_clips = [AudioFileClip(audio) for audio in audio_files]
iphone_resolution = (1080*1.5, 1080)

image_clips = []
for image, audio in zip(image_files, narration_clips):
	image = ImageClip(f'images/{image}').set_duration(audio.duration).resize(iphone_resolution)
	image_clips.append(image)

video = concatenate_videoclips(image_clips)

combined_audio = concatenate_audioclips(narration_clips)
video = video.set_audio(combined_audio)

audio_background = AudioFileClip('spirit of god.wav')
final_audio = CompositeAudioClip([video.audio, audio_background])
final_clip = video.set_audio(final_audio)

final_clip.write_videofile("vid.mp4", codec='libx264', fps=24, audio_codec='aac')


