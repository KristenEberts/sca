# Initials

## TL;DR

Implement a program that, given a person’s name, prints a person’s initials, per the below.

```
$ python initials.py
Regulus Arcturus Black
RAB
```

## Background

To practice playing around with strings, we're going to make a program where we print initials given a name!

## Your Mission

Design and implement a program, initials, that, given a person’s name, prints a person’s initials.

- Implement your program in a file called `initials.py`
- Your program should prompt a user for their name using `cs50.get_string()` or `input()` to obtain their name as a string
- You may assume that the user’s input will contain only letters (uppercase and/or lowercase) plus spaces. You don’t need to worry about names like Joseph Gordon-Levitt, Conan O’Brien, or David J. Malan
- But the user’s input might be sloppy, in which case there might be one or more spaces at the start and/or end of the user’s input or even multiple spaces in a row.
- Your program should print the user’s initials (i.e., the first letter of each word in their name) with no spaces or periods, followed by a newline (`\n`).
  - Note that `print()` adds a newline by default! To change this, use something like `print("Hello!", end="")`, signifying that you want to end the line with no special character (`""`).

### Example Runs

```
$ python initials.py
Zamyla Chan
ZC
```
```
$ python initials.py
   robert   thomas bowden
RTB
```
