from scipy.io import wavfile
import time


def main():
    current_time = time.strftime('%H:%M')
    split_time = current_time.split(':')
    hour = split_time[0]
    minute = split_time[1]
    print("The time is " + hour + ':' + minute)

main()
