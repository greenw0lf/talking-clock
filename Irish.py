"""
This file contains code related to the language logic of time in the
Irish language.

Authors: Dragos Balan & Hubert Matuszewski
"""
from helpers import with_or_without, play_audio, get_current_time


def get_hour_filename(hr: int, m: int):
    # Similar to English where we increment the hour when the amount of
    # minutes is above 30
    if m > 30:
        hr += 1
    if hr == 0:
        return 'Midnight.wav'
    else:
        # Convert from 24-hour to 12-hour format
        if hr >= 12:
            hr = hr - 12
            return str(hr) + 'IRI.wav'
        else:
            return str(hr) + 'IRI.wav'


def get_minute_filename(m: int):
    if m == 0:
        return 'oclock.wav'
    if m > 30:
        m = 60 - m
    return str(m) + 'IRI.wav'


def ie_speak_the_clock(speed_rate=1):
    # 2 is used for midnight, which is a special word, so we do not use
    # AM or PM
    am = 2
    hour, minute = get_current_time()
    if hour >= 12:
        am = 0
    elif hour != 0:
        am = 1
    audio_names = ['Its.wav']
    if minute != 0:
        audio_names.append(get_minute_filename(minute))
        audio_names.append(with_or_without(minute))
        audio_names.append(get_hour_filename(hour, minute))
    else:
        audio_names.append(get_hour_filename(hour, minute))
        audio_names.append(get_minute_filename(minute))

    if am == 0:
        audio_names.append('pm.wav')
    if am == 1:
        audio_names.append('am.wav')

    play_audio(audio_names, speed_rate, 'IrishAudio/')
