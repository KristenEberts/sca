# Connect Four

### TL;DR

Create Connect Four!

### Background

Connect four is a classic game for two players. The players take turns
dropping tokens into the columns of an upright rectangular board. The
first player to have four of their tokens in a row horizontally,
vertically, or diagonally wins. In this problem, you will implement a
command line version of Connect Four.

![Connect Four](connect_four.jpg)

#### Distribution code

If you look in `connect_four.py`, you will see bare bones definitions
of the various functions you will need to complete to implement the
game. Each function has a docstring (in triple quotes) that describes
what it is supposed to do. Your task for this problem is to implement
each of these functions. That's a lot of functionality to implement,
but don't worry; we'll go one step at a time. But first, let's walk
through the distribution code to make sure we understand what is going
on.

##### The Board

At the top of file, we define two variables, `BOARD_WIDTH` and
`BOARD_HEIGHT`. Just below where the variables are defined, they are
used to create the board, which is a list of lists. Each of the inner
lists represents a single **row** of the board. Each cell of the board
either contains `None`, which means it is empty, or the number of the
player whose token occupies that cell. The board is initialized to be
completely empty.

To see the board visualized, add a call to `print_board` in `main` and
run the program. As you can see, the board is empty (all `None`). Temporarily, add
a line like `board[0][0] = 1` before your call to `print_board`. You
should now see that the board is no longer empty. Which board space is
no longer empty? Play around and try to figure out how to place a
token (as the number 1 or 2) in each corner of the board. Try to place four in a row
horizontally, vertically, and diagonally. Don't forget to remove this code after
you are finished playing around with the board!

### Your Mission

Now that we understand how the board works, it's time to implement
connect four! We'll take it one step at a time. Click the "Next"
button to get started.

{% next %}

#### 0. Board Printing

If you play around with the board a little bit, you will quickly see
that the board is not very pretty. Your first task is to fix that by
changing the implementation of `print_board`. Feel free to make the
board look like anything you want, but you can use the layout below to
as inspiration. The only requirement is that the board be pretty.

```
|1 2 3 4 5 6 7|
|. . . . . . .|
|. . . . . . .|
|. . . . . . .|
|X . . . O O X|
|O X . X O X X|
|O O X O X X O|
```

In this example layout Player 1's tokens are represented with `X`,
Player 2's tokens are represented with `O`, and empty spaces are
represented with `.`. Thus, if a 1 is on the board (meaning player 1 has played
at that spot), we want to print out an `X` instead!

Below is pseudocode describing how to print the example layout. Feel
free to use it if you get stuck on your own design!

>```
>headers := list of numbers 1 to BOARD_WIDTH
>print vertical bars ("|") around header numbers joined by spaces
>for each row in the board:
>    tokens := empty list
>    for each column in the row:
>        if cell at row, column is None, then append "." to tokens
>        if cell at row, column is 1, then append "X" to tokens
>        if cell at row, column is 2, then append "O" to tokens
>    print vertical bars around strings in cells joined by spaces
>```
>
> Challenge: How can you make the code shorter by using this dict?
>
> ```
> {None: ".", 1: "X", 2: "O"}
> ```

Don't forget to test your implementation of `print_board` by adding
tokens to the board and calling `print_board` in `main`!

{% next %}

#### 1. Validating Input

Now that we can display the board, we need to let the users add their
tokens to the board. The first step to do this is to get input from
the user. The function for this is `get_move`. Right now `get_move`
accepts any input, but we want the input to be validated, meaning bad
input should be rejected. Valid input is any integer between 1 and
`BOARD_WIDTH`, inclusive. The input identifies which column the user
wants to drop a token into. If the user enters bad input, they should
be repeatedly prompted until they enter valid input.

Add a call to `get_move` to `main` and implement input validation in `get_move`. When you are done, your program might look something like this:

```
$ python connect_four.py
Enter a column number: abc123
Invalid input. Enter a column number: 0
Invalid input. Enter a column number: 10
invalid input. Enter a column number: -1
invalid input. Enter a column number: 3
$
```

The messages can be whatever you want, but the important part is that
the program keeps asking for input until a valid column number is
given.

{% next %}

#### 2. Updating The Board

Now that we can get correct input from the user, we need to be able to
update the board accordingly. Go ahead and change the implementation
of `make_move` to update the board. `make_move` takes two arguments,
the `player` making the move and the `column` they want to
play. Remember that in Connect Four tokens always fall down as far as
possible, so there should never be an empty space under a token. Don't
worry about detecting wins yet; `make_move` should still just return
`False` at this point.

To test your implementation of `make_move`, place the following in the body of `main`:

```
column = get_move()
make_move(1, column)
print_board()
```

When you run the program you should be able to make a move and see
that a token for Player 1 is placed at the bottom of the correct
column.

{% next %}

#### 3. The Game Loop

Now that we have the functionality in place for a player to make a
move and see the results, it's time to implement the high-level logic
of the game. Specifically, players should be able to alternate taking
turns and seeing the results until someone wins. Don't worry that you
haven't implemented win detection in `make_move` yet; for now just
assume that it works as specified in `make_move`'s docstring and we
will go back and implement it for real later.

Implement the following pseudocode for the game logic in `main`. When
you're done, you should be able to have two players alternate taking
turns, with the board state being printed before each turn. The game
will probably never end, since we haven't implemented that part yet,
so to quit the program you will have to press `Control-C`.

At the bottom of the file, the high-level game logic is implemented in
a loop in `main`. Each turn is a single iteration of this loop. You
can see that on each turn the board is printed, and the current
player's input is processed. If the current player has won the final
board is printed and the loop is broken, ending the game. Otherwise,
if the current player did not win, the current player is switched and
a new turn begins.

```
current player := 1
repeat:
    print the board
    print a message saying whose turn it is
    get input and make a move
    if that was the winning move:
        print the final board
        print a message announcing the win
        stop repeating and end program
    otherwise switch the current player and repeat
```

{% next %}

#### 4. Full Columns

Yay! Users can now take turns making moves. However, what happens if a
user plays on a full column? Try it out and see what happens. Your
code will probably either do nothing or crash. Neither result is what
we want, so go back to `get_move` and add to the input validation a
requirement that the chosen column is not full.

{% next %}

#### 5. Detecting Wins

The game is now fully playable except for the fact that it never
ends. Design an algorithm for checking if a player's move is a winning
move. Remember that a move is a winning move if it completes a
sequence of four identical tokens horizontally, vertically, or
diagonally. Implement your algorithm in `make_move`, returning `True`
if the move was a winning move and `False` otherwise.

This is the hardest part of this project, so we highly recommend that
you work with your neighbors to figure out a working algorithm. It
would also be a good idea to write down the algorithm as pseudocode on
paper before trying to implement it.

If you are truly stuck, you can press the Next button to see
pseudocode for a solution to this problem, but do try to work with
your neighbors to come up with an algorithm on your own first. A lot
of the fun of programming is trying to come up with algorithms like
this!

{% next %}

Here's pseudocode for detecting wins:

```
for direction in horizontal, vertical, diagonal left, and diagonal right:
    adjacent_matches := 1
    for each step in forward direction from move location
            until we are off the board or see a different player's token:
        adjacent_matches += 1
    for each step in backward direction from move location
            until we are off the board or see a different player's token:
        adjacent_matches += 1
    if adjacent matches >= 4, this is a winning move
```

The main idea is to move forward and backward along every possible win
direction (horizontal, vertical, and both diagonals) from the location
of the player's move, counting the number of adjacent identical tokens
as we go. The trick is in how you represent directions. Think about
how row numbers and column numbers change as you travel in each of
these directions.

{% next %}

#### 6. Handling Draws

Unfortunately the code currently has no way of detecting when a game
should be over because there are no more possible moves. Your final
task is to fix this in any way you see fit. This will require you to
make changes to the game loop in `main`.

{% next %}

Congrats! You have a working command line version of Connect
Four. Here are some optional bonus challenges to make the program more
interesting and flexible.

#### Bonus challenges

1. Switch the player at the end of the turn using a single line of
   code without using an `if`.

2. Make the game have three players instead of just two.

3. Take the size of the board and the number of players as command
   line arguments so they can be different each time the program is
   run.

4. The board initialization uses list multiplication to create rows of
   the correct length, but uses a loop to create the right number of
   rows. Comment out the distribution code's board initialization loop
   and replace it with the following:

   ```
   # board = []
   # for row in range(BOARD_HEIGHT):
   #     board.append([None] * BOARD_WIDTH)
   board = [[None] * BOARD_WIDTH] * BOARD_HEIGHT   
   ```

   This code uses list multiplication to create both the inner lists and
   outer list. Does it work? Can you explain why or why not?
