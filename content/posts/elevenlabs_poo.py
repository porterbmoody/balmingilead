#%%

import elevenlabs
audio = elevenlabs.generate(
    text = "Hi, I'm from the past!",
    voice = "ZQe5CZNOzWyzPSCn5a3c"
)
# %%
from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs
from elevenlabs import play

key = 'sk_8fd134551544125f26049ad3e350afd83c2a5522d33489ef'

load_dotenv()

client = ElevenLabs()

audio = client.text_to_speech.convert(
    text="The first move is what sets everything in motion.",
    voice_id="JBFqnCBsd6RMkjVDRZzb",
    model_id="eleven_multilingual_v2",
    output_format="mp3_44100_128",
)

play(audio)


# %%
from elevenlabs.client import ElevenLabs
from elevenlabs import play

client = ElevenLabs(
  api_key="sk_8fd134551544125f26049ad3e350afd83c2a5522d33489ef",
)

voice = client.clone(
    name="Alex",
    description="An old American male voice with a slight hoarseness in his throat. Perfect for news", # Optional
    files=["pizza.mp3"],
)
# %%
