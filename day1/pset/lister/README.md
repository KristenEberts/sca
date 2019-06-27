# Lister

## TL;DR

Create a program that asks the user for a length of a shopping list, allows the user to fill that list, and then prints the contents of that list to the screen.

## Background

To solidify for loops, lists, and appending, we're going to play around with a problem that allows us to create a shopping list.

## Your Mission
Create a program called `lister.py` that asks the user for an integer representing a length of a needed shopping list to be constructed. Then, with a for loop, fill the contents of a list of strings of the length given to you. Lastly, print the contents to the screen!

Note that you can create a blank list like so:
```
stuff = []
```

You'll want to append (add on to the end) new items as the user enters them. Check the following resources for help.
- [https://developers.google.com/edu/python/lists](https://developers.google.com/edu/python/lists)
- [https://www.tutorialspoint.com/python/list_append.htm](https://www.tutorialspoint.com/python/list_append.htm)

### Example Run
```
$ python lister.py
How many item? 5
Give me an item: pizza
Give me an item: hot dogs
Give me an item: hamburger
Give me an item: sushi
Give me an item: Oreos
["pizza", "hot dogs", "hamburger", "sushi", "Oreos"]
```
