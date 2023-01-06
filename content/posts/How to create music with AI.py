
#%%
import wave

path = "C:/Users/PorterMoody/OneDrive - The Wolff Company/Desktop/balmingilead/content/I Love You..wav"
# Open the WAV file
wav_file = wave.open(path, "r")

# Read the WAV file
data = wav_file.readframes(wav_file.getnframes())

# Close the WAV file
wav_file.close()

#%%

data


#%%

from scipy.io import wavfile
samplerate, data = wavfile.read(path)
samplerate

#%%

from colabcode import ColabCode


ColabCode(port=)





# %%
