"""
The main point of our application. This contains the code pertaining the GUI.

Authors: Dragos Balan & Hubert Matuszewski
"""
import tkinter as tk

from Irish import ie_speak_the_clock
from Polish import pl_speak_the_clock
from Romanian import ro_speak_the_clock
from French import fr_speak_the_clock
from time import strftime


# Config the digital clock shown at the top
def my_time():
    time_string = strftime('%H:%M:%S')
    DigitalTime.config(text=time_string)
    DigitalTime.after(1000, my_time)


# Used to set the proper values for the speed rate slider
#
# Warnings are thrown if no variable is given, despite us not needing it
def slider_func(val):
    new_val = min(play_rates, key=lambda x: abs(x - float(SpeedRate.get())))
    SpeedRate.set(new_val)


# Set up the window
ClockUI = tk.Tk()
ClockUI.title('Quattrolingo™ Clock')
ClockUI.configure(bg='black')
ClockUI.geometry("1280x720")


# Set up the steps for speed rate
play_rates = [0.25, 0.5, 0.75, 1, 1.25, 1.5, 1.75, 2]
# Fonts used throughout the application
time_font = ('Terminal', 52, 'bold')
button_font = ('Terminal', 20, 'bold')
scale_font = ('Terminal', 14, 'bold')


# The digital clock object, placed at the top
DigitalTime = tk.Label(ClockUI, font=time_font, bg='black', fg='#146cfa')
DigitalTime.place(x=425, y=50)


# The button for telling time in Romanian
RoSpeakTime = tk.Button(ClockUI, text='Cât este ceasul?', bd='10',
                              command=lambda: ro_speak_the_clock(SpeedRate
                                                                 .get()))
RoSpeakTime.place(x=200, y=270)
RoSpeakTime.configure(background='#146cfa', font=button_font, width=21)


# The button for telling time in Polish
PlSpeakTime = tk.Button(ClockUI, text='Jaka jest godzina?', bd='10',
                            command=lambda: pl_speak_the_clock(SpeedRate
                                                               .get()))
PlSpeakTime.place(x=660, y=270)
PlSpeakTime.configure(background='#146cfa', font=button_font, width=21)


# The button for telling time in Irish
IeSpeakTime = tk.Button(ClockUI, text='Cén t-am é?', bd='10',
                           command=lambda: ie_speak_the_clock(SpeedRate.get()))
IeSpeakTime.place(x=200, y=370)
IeSpeakTime.configure(background='#146cfa', font=button_font, width=21)


# The button for telling time in French
FrSpeakTime = tk.Button(ClockUI, text='Quelle heure est-il?', bd='10',
                            command=lambda: fr_speak_the_clock(SpeedRate
                                                               .get()))
FrSpeakTime.place(x=660, y=370)
FrSpeakTime.configure(background='#146cfa', font=button_font, width=21)


# The speech rate slider
SpeedRate = tk.Scale(ClockUI, from_=0.5, to=2, command=slider_func,
                     orient="horizontal", digits=3, resolution=0.25)
SpeedRate.set(1)
SpeedRate.place(x=505, y=580)
SpeedRate.configure(bg='#146cfa', font=scale_font,
                    label='Change the speed rate', troughcolor='black',
                    length=246)


# Run and display the window
my_time()
ClockUI.mainloop()
