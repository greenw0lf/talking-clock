# Dragoș & Hubert's Speaking Clock

## Project description
This is the speaking/talking clock that we developed in Python 3.9 for an
assignment for the course "Introduction to Voice Technology" as part of the Voice Technology
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

Special cases: 
1. When the amount of minutes is 0, Romanian works similar to English by
adding `o'clock` right after the hour is said.
2. When the amount of minutes is 1 or 59, we use "a minute" instead of "one minute". Example: "The time is `<hour>` and/without a minute"

Examples (Add "Ora este", equivalent to "The time is" in English, before each example):
- 19:00 = 9 fix.
- 15:15 = 15 și un sfert
- 07:45 = 8 fără un sfert
- 13:25 = 13 și 25 de minute
- 13:07 = 13 și 7 minute
- 14:44 = 15 fără 16 minute
- 16:35 = 17 fără 25 de minute
- 12:01 = 12 și un minut
- 22:59 = 23 fără un minut

### Irish
Irish works similar to English in structure. The format is:

`"It's" + minutes/"quarter"/"half" + "past/to" + hour + "AM/PM"`

If the amount of minutes is above 30, we subtract it from 60 
and the hour is incremented by 1 (as in English).
If the amount of minutes is 15/45, we use "quarter". For 30 minutes, we use "half" (halfhour more literally; "leathuair").

When it comes to hours, we use the 12-hour format with AM and PM added at the end. So,
if 0 <= hour < 12, we add "AM" at the end, otherwise we add "PM".

When counting, the prefix "a" (not an article such as a/the in English) is added in front of the number. This affects numbers which begin with a vowel, since in Irish, an "h" is added when two vowels clash together. Thus instead of saying "deich tar éis aon" (ten past one), you say "deich tar éis a haon" ("ocht" (eight) also becomes "a hocht" by this rule). The "a" isn't a strict grammatical rule, but rather convention.

Counting in Irish is rather convoluted, but luckily in telling time, not that much complexity is encountered. To get a sense of how complicated it can be, have a read of this article: https://www.wikihow.com/Count-to-10-in-Irish.

Special cases:
1. When the amount of minutes is 0: "It's `<hour>` o'clock"
2. There are different ways of telling time around midnight, different regions will have their own way of communicating it. Thus our programme chose one of many ways to express this. When the hour is 0, the word "midnight" is used if the amount of minutes <= 30.
For example, "It's 17 past midnight". However, if the hour is 23 and the minute > 30,
the code outputs "It's <60-minutes> to 12 AM".
3. When the time is 12:00 AM, Irish people simply say "It's midnight".

Examples (Add "Tá sé" before each example):
- 00:00 - `meán oíche`
- 00:13 - `trí déag tar éis meán oíche`
- 23:45 - `ceathrú chun a dó dhéag iarnóin`
- 01:27 - `fiche seacht tar éis a haon roimh nóin`
- 03:45 - `ceathrú chun a ceathar roimh nóin`
- 12:00 - `Dó dhéag a chlog`
- 13:30 - `leathuair tar éis a haon iarnóin`
### Polish
The format of telling time in Polish when the amount of minutes < 30:

`"It's" + minutes + "and" + hour`

For > 30 minutes:
`"It's to" + minutes + (hour + 1)`

Where `minutes` is the current minute and `hour` is the current hour
(so we increment the hour by 1, same as in the previous languages).

If the time is "hour" o'clock (with the exception mentioned in the special cases section),
Polish people say `It's <hour>`.

The minute can determine a different grammatical case for the hour. If 1 <= minutes <= 30, we use
the possessive form, otherwise we use the non-possessive one (in the audio file names, they
can be found as the numbers that end in "th" and "tha" respectively).

Special cases:
1. When it's 30 minutes, Polish uses the form `It's half to <hour+1>`.
This is different from the other languages we have seen, since the others
use `half past <hour>`.
2. When it's exactly midnight, Polish people simply say "It's midnight", similar to Irish. It is also acceptable to say "It's 24:00".
3. The possessive also applies to midnight for 1 <= minutes <= 30.
(`Past_Midnight.wav` in the audio files).

Examples (Add "Jest" before each example):
- 00:00 - `Północ`
- 00:13 - `Trzynaście po północy`
- 23:45 - `Za piętnaście północ`
- 13:27 - `Dwadzieścia siedem po trzynastej`
- 03:45 - `Za piętnaście czwarta`
- 12:00 - `Dwunasta`
- 16:30 - `W pół do siedemnastej`
### French
French has the most straightforward logic for telling time. It uses a 24-hour format, and there is no
subtraction to be done or any hour increment/special keywords for "quarter" or "midnight". The format is:

`"It's" + hour + "hour(s)" + minute`

Where `hour` is the current hour, `minute` is the current minute.

There are two small things to note for French:
French never explicitly references 12:00. It's either "midi" for midday, and "minuit" for midnight. These are still notated as 12 and 0 in the audio files.

One "un" always carries and "et" in front of it. Thus the time is normally hour + "hour(s)" + and + one. This also applies to any time between 21:00-21:59, but then we use "une" as hour is feminine. Thus one says "vingt-et-une heures" (twenty and one hours)

Examples (Add "Il est" before each example):
- 12:00 - `midi`
- 13:25 - `treize heures vingt cinq`
- 4:50 - `quatre heures cinquante`
- 21:01 - `vingt-et-une heures et un`

## GDPR Compliance
The audio files used were generated using TTS APIs. For Romanian, Polish, Irish and French, Narakeet was used (https://www.narakeet.com/languages/).
The voice used for Romanian was Alina, for Polish, Justyna, for Irish, Dearbhla, and for French, Marion.
The French voice is meant to resemble Metropolitan French, whereas the Irish voice resembles Ulster (or colloquially known as Donegal) Irish.

No consent forms were required for the collection of this data since there were no individuals recorded by us
to generate this speech. The data used for the speaking clock therefore complies
with GDPR regulations.
