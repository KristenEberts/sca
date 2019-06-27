# Double vision

## TL;DR

Create a program that asks the user for a string, and then doubles the characters in the string and prints the resulting string.

## Background

To solidify for loops, strings, and concatenating, we're going to play around with a problem that double the characters in a string.

## Your Mission
Write program called `double_char.py`, that asks the user for a string and prints a string where for every char in the original, there are two chars. 

For the following inputs, your program should pronounce the following output:

```
The --> TThhee
AAbb --> AAAAbbbb
Hi There --> HHii  TThheerree
```

You might find it useful to utilize a for loop to go through each character in the string, and for each character, add the same letter twice to a new string.

Note that you can create a blank string like so:
```
stuff = ""
```

You'll want to use string concatenation to add the same letters twice. Check the following resources for help.
- [http://www.pythonforbeginners.com/concatenation/string-concatenation-and-formatting-in-python](http://www.pythonforbeginners.com/concatenation/string-concatenation-and-formatting-in-python)
- [https://www.digitalocean.com/community/tutorials/an-introduction-to-working-with-strings-in-python-3](https://www.digitalocean.com/community/tutorials/an-introduction-to-working-with-strings-in-python-3)

### Example Run
```
$ python double_char.py
Please enter a string: Hello World!
HHeelloo  WWoorrlldd!!
```