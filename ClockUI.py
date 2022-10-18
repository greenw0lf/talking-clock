#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import tkinter as tk
from tkinter import ttk
from tkinter import *
from main import speak_the_clock
from time import strftime

ClockUI = tk.Tk()
ClockUI.configure(bg='black')
ClockUI.geometry("1250x750")


def my_time():
    time_string = strftime('%H:%M:%S')
    DigitalTime.config(text=time_string)
    DigitalTime.after(1000, my_time)


def output_text():
    result = 'Deez nuts'


my_font = ('Terminal', 52, 'bold')
DigitalTime = tk.Label(ClockUI, font=my_font, bg='black', fg='cyan')
DigitalTime.grid(row=1, column=1, padx=300, pady=50)
SpeakTime = Button(ClockUI, text='Speak Time', bd='10',
                   command=speak_the_clock)  # here would be our main code
SpeakTime.grid(row=2, column=1, padx=300, pady=200)
SpeakTime.configure(background='blue', font=my_font)
my_time()
ClockUI.mainloop()
