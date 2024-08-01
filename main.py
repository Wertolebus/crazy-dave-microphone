# 01.08.2024
# crazy dave mic
# zbojpg

import numpy as np
import sounddevice as sd
import os
import random
import soundfile as sf

RATE = 44100  
CHUNK = 1024  
THRESHOLD = 0.0005  

# write your mic
MIC_DEVICE_INDEX = 1  

# write virtual mic index
VIRTUAL_MIC_DEVICE_INDEX = 6

is_playing = False

def play_random_sound(audio_folder="audio"):
    global is_playing
    sound_files = [f for f in os.listdir(audio_folder) if f.endswith(".ogg")]
    if sound_files and not is_playing:
        sound_file = os.path.join(audio_folder, random.choice(sound_files))
        data, fs = sf.read(sound_file, dtype='float32')
        is_playing = True
        sd.play(data, fs, device=VIRTUAL_MIC_DEVICE_INDEX, blocking=True)  
        is_playing = False


def audio_callback(indata, frames, time, status):
    global is_playing
    if status:
        print(status)
    audio_data = np.frombuffer(indata, dtype=np.int16)
    rms = np.sqrt(np.mean(np.square(audio_data)))
    volume = rms / 32768  # normalize
    print(volume)
    if volume > THRESHOLD and not is_playing:
        play_random_sound()

with sd.InputStream(device=MIC_DEVICE_INDEX, channels=1, callback=audio_callback, blocksize=CHUNK, samplerate=RATE):
    sd.sleep(int(1e6))  