# Dragoș & Hubert's Speaking Clock

## Project description
This is the speaking/talking clock that we developed in Python 3.9 for an
assignment for the course "Introduction to Voice Technology" of the Voice Technology
MSc at RUG - Campus Fryslan.

## Requirements before installing
Make sure you have `Python 3.9` installed. Download the latest 3.9 version from here: https://www.python.org/downloads/

## Installation
1. Click on the green `Code` button at the top of the repository > `Download ZIP`.
2. Extract the ZIP to the location where you want to install it on your computer.

(You can also just clone the repository locally if you are familiar with Git. In that case,
the steps above can be skipped)

3. Open the terminal (or command prompt, depending on the OS you use) and navigate
to where you extracted the zip via the terminal.
4. Run `pip install -r requirements.txt` to install the dependencies required.

## Usage
Run `python main.py` in the terminal. Make sure to be in the same directory where
the repository is installed in the terminal. It will open an interactive GUI with which
you can interact with.

Each button will tell the current time in a different language. The text on each 
button says "What's the time?" in the language it will speak. For example, in Romania
people say "Cât e(ste) ceasul?" to ask about the current time.

The slider at the bottom adjusts the speed at which the time is said. A setting of
`1.5` will tell the time 1.5x faster than the default speech rate.

## Languages supported
- Romanian
- Irish
- Polish
- French

## Linguistic rules for telling time
### Romanian
In Romanian, the format of telling time is:

`"The time is" + hour + "and/without" + minutes/"quarter"/"half" + (optional) "minutes"`

Where `hour` corresponds to the current hour and `minutes` corresponds to the
amount of minutes past/to. The words between "" represent the actual word, in Romanian.

The hour system used is the 24-hour format. If the amount of minutes is above 30, we say
the hour that follows instead of the current one since we also convert the amount of
minutes accordingly (see next section and the examples below for more information).

If the amount of minutes is equal to 15 or 45, then we use "quarter" and in that case
we do not add the word "minutes" after it. If the amount is 30, we use "half" and same logic
applies as for "quarter". Otherwise, we either say the `amount` if it is smaller than 30 (and none of the
other options from above apply) or `60-amount` if it is larger than 30. As for when to use "and" or "without", 
we use "and" when `amount <= 30`, otherwise we use "without" and increment the hour amount by 1.

Extra information about minutes: When `20 <= amount <= 40, amount != 30`, Romanians say "`amount` of minutes"
instead of just "`amount` minutes".

Special case: When the amount of minutes is 0, Romanian works similar to English by
adding `o'clock` right after the hour is said.

Examples (Add "Ora este", equivalent to "The time is" in English, before each example):
- 19:00 = 9 fix.
- 15:15 = 15 și un sfert
- 07:45 = 8 fără un sfert
- 13:25 = 13 și 25 de minute
- 13:07 = 13 și 7 minute
- 14:44 = 15 fără 16 minute
- 16:35 = 17 fără 25 de minute

### Irish

### Polish

### French