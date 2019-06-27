# Hours

## TL;DR

Write a program that tells what time it will be in a user inputted amount of hours.

```
$ python hours.py
What hour is it? 9
How many hours will pass? 6
In 6 hours it will be 3 o'clock
```

## Background

To better understand how the modulus (`%`) operator works, lets play around with the concept of time! What happens when it's 9 pm and 4 hours pass by? Surely it's not 13 pm, right? Hmm... How can modulus help us represent time in this way?

## Your Mission

Write a program called `hours.py` that asks for the current hour, a number of hours to pass, and then prints the time after. Only the numbers 1-12 should be used for hours (HINT: % 12 will limit to 0-11, but 0 is equivalent to what hour?. Hmm...)

### Example Run

```
$ python hours.py
What hour is it? 9
How many hours will pass? 6
In 6 hours it will be 3 o'clock
```
