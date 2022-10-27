import librosa
import numpy as np
import pygame
from scipy.io import wavfile
import time


def get_current_time():
    current_time = time.strftime('%H:%M')
    split_time = current_time.split(':')
    return int(split_time[0]), int(split_time[1])


def cut_silence(signal,sr=16000,threshold=0.09,padding=40):
    # Max amplitude
    max_signal = max(signal)
    # Determine the threshold as %age of max amplitude
    _threshold = threshold * max_signal
    # Based on the sampling rate, we determine the length of the padding
    # (converted to seconds)
    len_padding = (padding / 1000) * sr
    # Indices of our beginning and end stage.
    cutoff = np.where(signal > _threshold)
    # Extract the actual array
    _cutoff = cutoff[0]
    # Take the first element and go back by the amount of samples stipulated
    # in the padding
    first_cutoff = int(_cutoff[0] - len_padding)
    # Take the last element and go forwards by the amount of samples stipulated
    # in the padding
    last_cutoff = int(_cutoff[-1] + len_padding)
    if first_cutoff < 0:
        # In case someone passes a padding which is too large,
        # to avoid negative indices
        first_cutoff = 0
    if last_cutoff > len(signal):
        # In case someone passes a padding which is too large,
        # to avoid going out of range of array
        last_cutoff = len(signal)
    # Trim our signal according to our calculated endpoints
    _signal = signal[first_cutoff:last_cutoff]
    signal = _signal
    return signal


def read_audio(filename: str, path: str):
    sr, audio = wavfile.read(path + filename)
    if path != './RomanianAudio/':
        audio = cut_silence(audio,sr=sr)
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
    pygame.mixer.init()
    aud = pygame.mixer.Sound('result.wav')
    aud.play()
    time.sleep(aud.get_length())
    pygame.mixer.music.unload()
