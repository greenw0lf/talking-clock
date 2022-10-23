import os

import librosa
import numpy as np
from playsound import playsound
from scipy.io import wavfile


def read_audio(filename: str, path: str):
    sr, audio = wavfile.read(path + filename)
    return audio


def get_sr(filename: str, path: str):
    sr, audio = wavfile.read(path + filename)
    return sr


def with_or_without(m: int):
    return 'to.wav' if m > 30 else 'and.wav'


def concatenate_audio(filenames, lang_path):
    audio = []
    sr = get_sr(filenames[0], lang_path)
    for name in filenames:
        audio = np.concatenate((audio, read_audio(name, lang_path)))
    return sr, audio


def play_audio(audio_names, speed_rate, lang_path):
    sr, result_audio = concatenate_audio(audio_names, lang_path)
    if speed_rate != 1:
        result_audio = librosa.effects.time_stretch(result_audio,
                                                    rate=float(speed_rate))

    result_audio = np.array(result_audio, dtype=np.int16)
    wavfile.write('result.wav', sr, result_audio)
    playsound('result.wav')
    os.remove('result.wav')
