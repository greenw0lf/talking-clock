import tkinter as tk

from Irish import ie_speak_the_clock
from Polish import pl_speak_the_clock
from Romanian import ro_speak_the_clock
from time import strftime

ClockUI = tk.Tk()
ClockUI.configure(bg='black')
ClockUI.geometry("1250x750")


def my_time():
    time_string = strftime('%H:%M:%S')
    DigitalTime.config(text=time_string)
    DigitalTime.after(1000, my_time)


play_rates = [0.25, 0.5, 0.75, 1, 1.25, 1.5, 1.75, 2]


def slider_func(val):
    new_val = min(play_rates, key=lambda x: abs(x - float(SpeedRate.get())))
    SpeedRate.set(new_val)


time_font = ('Terminal', 52, 'bold')
button_font = ('Terminal', 20, 'bold')
scale_font = ('Terminal', 14, 'bold')
DigitalTime = tk.Label(ClockUI, font=time_font, bg='black', fg='#146cfa')
DigitalTime.grid(row=1, column=2, pady=(100, 200))
RoSpeakTime = tk.Button(ClockUI, text='Cât este ceasul?', bd='10',
                              command=lambda: ro_speak_the_clock(SpeedRate
                                                                 .get()))
RoSpeakTime.grid(row=2, column=1, padx=(100,0))
RoSpeakTime.configure(background='#146cfa', font=button_font)
IeSpeakTime = tk.Button(ClockUI, text='Cén t-am é?', bd='10',
                           command=lambda: ie_speak_the_clock(SpeedRate.get()))
IeSpeakTime.grid(row=2, column=2)
IeSpeakTime.configure(background='#146cfa', font=button_font)
PlSpeakTime = tk.Button(ClockUI, text='Która godzina?', bd='10',
                            command=lambda: pl_speak_the_clock(SpeedRate
                                                               .get()))
PlSpeakTime.grid(row=2, column=3)
PlSpeakTime.configure(background='#146cfa', font=button_font)
SpeedRate = tk.Scale(ClockUI, from_=0.5, to=2, command=slider_func,
                     orient="horizontal", digits=3, resolution=0.25)
SpeedRate.set(1)
SpeedRate.grid(row=3, column=2, pady=120)
SpeedRate.configure(bg='#146cfa', font=scale_font,
                    label='Change the speed rate', troughcolor='black',
                    length=246)
my_time()
ClockUI.mainloop()
