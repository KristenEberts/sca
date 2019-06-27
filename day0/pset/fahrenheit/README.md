# Fahrenheit

## TL;DR

Create a program that converts a temperature in Fahrenheit into Celsius.

## Background

It's amazing that the US is one a few countries that still uses Fahrenheit! Let's make a program that helps us calculate a relate temperature in Fahrenheit when given Celsius so that we may understand the temperature no matter where we go!

## Your Mission

We're going to create a program called `fahrenheit.py` that will help us with these temperature conversions. For this problem, we’re going to focus on converting in just one direction: from Celsius to Fahrenheit. As it happens, the formula for this conversion isn’t terribly complex. (Phew!) One simply takes the current temperature in degrees Celsius (°C), multiplies it by 9, divides by 5, and then adds 32. The result is the equivalent temperature in degrees Fahrenheit (°F). Not bad, right? For the more visually inclined, this translates to this formula:

```
F = ((C * 9) / 5) + 32
```

Let’s do a quick test to make sure things work as expected. Worldwide, the commonly accepted value for normal human body temperature is 37°C. If we plug "37" into that formula where °C goes and do the math (37 multiplied by 9 is 333, 333 divided by 5 is 66.6, 66.6 + 32 is 98.6) we get 98.6°F which is what folks in the United States know as normal human body temperature. So that checks out. Similarly if we plug in 0°C (the freezing point of water) into that formula does it convert to 32°F, and 100°C (the boiling point of water) is apparently equivalent to 212°F. Seems like things are going well.

We're ready to create a program! We want our program to behave like the below:

```
$ python fahrenheit.py
C: 100
F: 212.0
```
