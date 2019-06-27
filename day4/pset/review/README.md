#### 0. I Can't Even...

Create a problem that, using a for loop, prints the numbers 1 through 15, line by line, with a string noting if the integer is even or odd.

##### Example Run
```
$ python oddoreven.py
1 odd
2 even
3 odd
4 even
5 odd
6 even
7 odd
8 even
9 odd
10 even
11 odd
12 even
13 odd
14 even
15 odd
```

{% next %}

#### 1. List o' Grades
Create a program that continuously asks a user for numerical grades until the user types `done`. These grades should be appended onto a list. Once the user is done entering grades, the average of the grades should be printed to the screen.

##### Example Run
```
$ python grades.py
What was your assignment grade (type done to finish)? 68
What was your assignment grade (type done to finish)? 72
What was your assignment grade (type done to finish)? 92
What was your assignment grade (type done to finish)? 89
What was your assignment grade (type done to finish)? 94
What was your assignment grade (type done to finish)? done
Your average grade is 83
```

{% next %}

#### 2. Decreasing

Write a **function** that takes a list of integers and returns true if the list is not in increasing order. Consecutive elements of the same value are allowed. To test, write a main function that calls this new function you created.

For example:
```
>> decreasing([1,2,3])
false
>> decreasing([3,2,1])
true
>> decreasing([5,2,2,2,1,1])
true
```

{% next %}

#### 3. Gridded

Write a program that takes in an integer between **1 and 9**, inclusive, for dimension and prints a square grid to the screen of that size. This square grid should have ascending integers in each spot on the grid like below:

```
$ python grid.py
What is the dimension of the grid? 4
| 1 | 2 | 3 | 4 |
| 5 | 6 | 7 | 8 |
| 9 | 10| 11| 12|
| 13| 14| 15| 16|
```

We want the grid to look exactly like the one above! Thus, how do we treat single-digit integers differently than double-digit ones? Hmm...

More Examples:
```
$ python grid.py
What is the dimension of the grid? 3
| 1 | 2 | 3 |
| 4 | 5 | 6 |
| 7 | 8 | 9 |

$ python grid.py
What is the dimension of the grid? 1
| 1 |
```

{% next %}

#### 4. Unzip

Imagine that you have a dictionary that represents a 'zipped' version of list. In other words, because there was repeats in the original list, it became nice to just store the number of times each value repeats.

For example say you had the following list:

```
old = [
         "green", "green", "green", "green",
         "green", "green", "blue", "blue",
         "blue", "red", "red", "red", "red",
         "red", "red", "red", "red", "red",
         "orange", "orange"
      ]
```

There's a lot of repetition here, so we want to condese this information in a dictionary where the key-value pairs are `color: count` like so:

```
zipped = {
            "green": 6,
            "blue": 3,
            "red": 9,
            "orange": 2
          }
```

This saves a lot of space because we don't need to repeat every color in a list. Rather we remember how many times the colors repeat! This is one way we can compress or zip a file!

But how do we bring it back?

Write a **function** that takes in a dict like `zipped` and returns a list like `old`, therefore "restoring" the original file. To test, call this function in a main function.
