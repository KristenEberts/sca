# Xs and Os

### TL;DR

Create a program that allows two people to play the game Tic-Tac-Toe.

### Background

#### Tic-Tac-Toe

Welcome to the classic and simple game of [Tic-Tac-Toe](https://en.wikipedia.org/wiki/Tic-tac-toe), in which two players take turns strategically placing their chosen symbol (and X or an O) in a 3 x 3 grid. The game ends when one of the players manages to place their symbol in the three slots constituting a row, a column or diagonal, or when all the slots become filled up and no one wins, resulting in a stalemate.

![grid](grid.png)

If you're familiar with the game, you'll know that there are strategies you can follow that ensure you always win the game (or that at least you [never lose!](https://www.quora.com/Is-there-a-way-to-never-lose-at-Tic-Tac-Toe])). You'll get enough time to practice such strategies when you've finished implementing our incomplete version of Tic-Tac-Toe, for which we've provided you with some initial code, but we're hoping you can help up finish it up! We're going to be using Python to complete the game! First, we're going to familiarize ourselves with some data structures, including **lists** and **dictionaries**.

#### Lists

In Python, we can create the **list** data structure, which quite literally stores a sequence of elements in order such as the one below:

```
grades = [91, 92, 87, 74, 95]
```

If we want to know what the first element in this list is (remember that in computer science we tend to use 0 to indicate the first element, 1 to indicate the second element, etc.), we can print it like so:

```
# This will print 91
print(grades[0])
```

However, lists are useful when we want to store more than just simple values like numbers. In real-world, we often use more complex structures to represent information. For example, we might often need to somehow represent two-dimensional data, such as data you might store in a table or a matrix. Turns out, Python allows you to store lists within a list, which in other programming contexts and languages may be referred to as 2D lists. If the above list consisted of a simple list of grades of one student in a single class, let's imagine we wanted to store all of the same student's grades, but he is taking 3 classes instead of one. How do we ensure that the grades for one class are distinct from the grades of another? We can use a list of lists, like so:

```
grades = [[91, 94, 89, 85, 89], [92, 92, 88, 89, 90], [90, 91, 86, 85, 90]]
```

The above can be formatted to look like this:

```
grades = [
		  [89, 94, 89, 85, 91],
		  [86, 92, 88, 89, 90],
		  [90, 91, 86, 85, 90],
		  [91, 93, 96, 89, 90]
		 ]
```

And you can see how the above 2D list might correspond to a table like the following:

| Class         |    |    |    |    |    |
|---------------|----|----|----|----|----|
| AP Chemistry  | 89 | 94 | 89 | 85 | 91 |
| AP Biology    | 86 | 92 | 88 | 89 | 84 |
| AP Psychology | 90 | 91 | 86 | 85 | 90 |
| AP English    | 91 | 93 | 96 | 89 | 92 |

The first element of `grades` here — `grades[0]` — is a list of numbers `[89, 94, 89, 85, 91]`. The first element of this new list is `grades[0][0] == 89` and
`grades[0][1] == 94`
`grades[0][2] == 89`
`grades[1][0] == 86`
`grades[1][1] == 92`
`grades[1][4] == 84`

When working with a list of lists, we tend to use nested loops. The first loop iterates through the row number, the second loop runs through the elements inside of a row. For example, this is how we might print the contents of a 2D numerical list on the screen line by line, separating the numbers with spaces:

```
a = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end=' ')
    print()
```

The above snippet of code outputs:
```
1 2 3 4
5 6
7 8 9
```

Now that we are a bit more familiar with 2D lists, we'll use them to represent a 3 x 3 tic-tac-toe board!

#### Lists in `tictactoe.py`

Open up `tictactoe.py` and on the first line of the `main()` function, you'll see the following:

`board = [[] for _ in range(3)]`

In Python, this is known as a list comprehension, which is a very pythonic and concise way of creating lists. The other square brackets contain an expression follow by a for clause, which essentially resembles a shorthand for the for loop itself. The below list comprehension and for loop both achieve the same thing, creating the list `[0, 1, 2]`:

```
new_list = [i for i in range(3)]

new_list = []
for i in range(3):
	new_list.append(i)
```

Finally, sometimes in Python we don't really care about putting real values in a list and we simply want to create a list containing a set number of values. If we wanted to create a list of three 1s using a list comprehension, we could do it like so: `new_list = [1 for _ in range(3)]`, which would create the list `[1, 1, 1]`.

Thus, going back to the first line of main, what do you think that line itself creates? Place a print statement to check your understanding of the content of the variable `board`.

Now, let's look at the nested for loop following the initialization of the `board` variable. On line 39 we have a for loop and in line 40 we have a second (nested) for loop. Immediately after this, on line 41, we access the `board` variable `board[row]`. Thinking back to what the `board` variable contains, in the  2D lists section, we found that board is itself a list of 3 lists, each of the lists responding to a row in the 3 x 3 Tic-Tac-Toe grid. Thus, in the first iteration of the for loop when `row = 0`, when accessing `board[0]`, we access the first list within `board`, which corresponds to the first row of the Tic-Tac-Toe grid.

Thus, with the outer for loop, we access each of the rows, `board[0]`, `board[1]` and `board[2]`. Then, in the inner for loop, to each of the rows we append a number between 1 and 9, which will be displayed on the grid so that the players can select a slot.

### Your Mission

We're going to create a program that allows two people to play the game Tic-Tac-Toe ! Although the program is partially created, it looks like there's more work to be done!

You're going to tackle a few `TODO`'s in `tictactoe.py`.

#### 0. `winner(board)`

In `tictactoe.py`, you'll see the function `def winner(board):`, which needs to check whether in the current board configuration (which you'll be able to access and check through the `board` variable) there is a winning pattern. In order to do this, you'll need to:

1. Check all rows to see if any one row has three identical symbols in it
2. Check all columns to see if any one row has three identical symbols in it
3. Check both diagonals to see if either of them has three identical symbols in it

![game](game.jpg)

If any row, column or diagonal contains three identical symbols, that means that the game was one, and you can return `True`. Otherwise, you should return `False`.

#### 1. `stalemate(board)`

You need to create the function that checks whether in the current board configuration (which you can access through the `board` variable), there is a stalemate. This happens when all the cells in the 3 x 3 board are filled in a there is no row, column or diagonal that contains three identical consecutive symbols.

You should return `True` if there is a stalemate, and `False` otherwise.

Hint: Remember that you can check whether a given cell has been played (i.e. already has a symbol in it), when accessing the `board` variable. If the top left element (the first element in the first row) is filled in, then `board[0][0]` will contain an alphabetical character. If all slots are filled in, they will all contain alphabetical characters (either 'X' or 'O'); however, if there are empty slots, some will have numerical characters, since the board starts out with 1-9. Think of how you might use Python's `isalpha()` method (you can read more about it [here](https://docs.python.org/3/library/stdtypes.html#str.isalpha) and [here](https://www.tutorialspoint.com/python/string_isalpha.htm)) to determine whether all slots are filled in.

If you can be clever about it, you could implement this function in one line! You might want to look into using Python's built-in `all()` function, which returns `True` when all elements are true in an iterable object. To read up on `all()`, visit this [tutorial](https://www.programiz.com/python-programming/methods/built-in/all) or the Python [documentation](https://docs.python.org/2/library/functions.html#all).
