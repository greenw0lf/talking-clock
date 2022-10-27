"""
This file contains code related to the language logic of time in the
Polish language.

Authors: Dragos Balan & Hubert Matuszewski
"""
from helpers import with_or_without, play_audio, get_current_time


def get_hour_filename(hr: int, m: int):
    if m >= 30:  # Poland has 30-60 as (x to)
        hr += 1
    if hr == 0 and m == 0:
        return 'Midnight.wav'  # midnight -polnoc
    elif hr == 0 and m > 0:
        return 'Past_Midnight.wav'  # past midnight has grammar - polnoc(y)
    else:
        if m == 0 or m > 30:
            return str(hr) + 'tha.wav'  # non-possessive
        else:
            return str(hr) + 'th.wav'  # possessive


def get_minute_filename(m: int):
    if m == 30:
        return 'half_to.wav'
    if m > 30:
        m = 60 - m
    return str(m) + 'POL.wav'


def pl_speak_the_clock(speed_rate=1):
    hour, minute = get_current_time()
    audio_names = ['Its.wav']
    if minute != 0:
        # In Polish, there is a difference between "past" and "to"
        # Here, we have the format "<minute> past <hour>"
        if minute < 30:
            audio_names.append(get_minute_filename(minute))
            audio_names.append(with_or_without(minute))
        # Here, however, it is something along the lines of
        # "in <minute> <hour+1>" (In 20 minutes it will be 13 for 12:40)
        elif minute > 30:
            audio_names.append(with_or_without(minute))
            audio_names.append(get_minute_filename(minute))
        # Otherwise, we simply add "half to" to obtain
        # "It's half to <hour+1>"
        else:
            audio_names.append(get_minute_filename(minute))
    audio_names.append(get_hour_filename(hour, minute))

    play_audio(audio_names, speed_rate, 'PolishAudio/')
