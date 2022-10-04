from scipy.io import wavfile
from playsound import playsound
import numpy as np
import time


def read_audio(filename: str):
    sr, audio = wavfile.read('./audio_files/' + filename)
    return audio


def get_sr(filename: str):
    sr, audio = wavfile.read('./audio_files/' + filename)
    return sr


def get_current_time():
    current_time = time.strftime('%H:%M')
    split_time = current_time.split(':')
    return int(split_time[0]), int(split_time[1])


def get_hour_filename(hr: int, m: int):
    if m > 30:
        hr += 1
    return str(hr) + '.wav'


def get_minute_filename(m: int):
    if m == 0:
        return 'o_clock.wav'
    elif m == 15 or m == 45:
        return 'quarter.wav'
    elif m == 30:
        return 'half.wav'
    elif m > 30:
        m = 60 - m
    return str(m) + '.wav'


def with_or_without(m: int):
    return 'to.wav' if m > 30 else 'and.wav'


def concatenate_audio(filenames):
    audio = []
    sr = get_sr(filenames[0])
    for name in filenames:
        audio = np.concatenate((audio, read_audio(name)))
    return sr, audio


def main():
    hour, minute = get_current_time()
    print("The time is " + str(hour) + ':' + str(minute))

    audio_names = ['the_time_is.wav', get_hour_filename(hour, minute)]
    if minute != 0:
        audio_names.append(with_or_without(minute))
    audio_names.append(get_minute_filename(minute))
    if minute != 0 and minute != 15 and minute != 30 and minute != 45:
        audio_names.append('minutes.wav')

    sr, result_audio = concatenate_audio(audio_names)
    result_audio = np.array(result_audio, dtype=np.int16)

    wavfile.write('result.wav', sr, result_audio)
    playsound('result.wav')


main()
