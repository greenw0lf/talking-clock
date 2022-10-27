from helpers import with_or_without, play_audio, get_current_time


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
    if m == 1:
        return 'a_minute.wav'
    return str(m) + '.wav'


def ro_speak_the_clock(speed_rate=1):
    hour, minute = get_current_time()

    audio_names = ['the_time_is.wav', get_hour_filename(hour, minute)]
    if minute != 0:
        audio_names.append(with_or_without(minute))
    audio_names.append(get_minute_filename(minute))
    if minute != 0 and minute != 15 and minute != 30 and \
            minute != 45 and minute != 1 and minute != 59:
        if abs(minute - 30) > 10:
            audio_names.append('minutes_below_20.wav')
        else:
            audio_names.append('minutes_20_above.wav')

    play_audio(audio_names, speed_rate, './RomanianAudio/')
