"""
This file contains code related to the language logic of time in the
French language.

Authors: Dragos Balan & Hubert Matuszewski
"""
from helpers import play_audio, get_current_time


def get_hour_filename(hr: int):
    return str(hr) + 'Hour.wav'


def get_minute_filename(m: int):
    return str(m) + '.wav'


def fr_speak_the_clock(speed_rate=1):
    hour, minute = get_current_time()

    # In French, it is simply said "It's <hour> hours"
    if minute != 0:
        audio_names = ['Its.wav', get_hour_filename(hour),
                       get_minute_filename(minute)]
    else:
        audio_names = ['Its.wav', get_hour_filename(hour)]

    play_audio(audio_names, speed_rate, 'FrenchAudio/')