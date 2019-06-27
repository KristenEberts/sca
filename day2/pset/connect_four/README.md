# Connect Four

### TL;DR

Create Connect Four!

### Background

Connect four is a classic game for two players. The players take turns
dropping tokens into the columns of an upright rectangular board. The
first player to have four of their tokens in a row horizontally,
vertically, or diagonally wins. In this problem, you will implement a
command line version of Connect Four.

#### Distribution code

If you look in `connect_four.py`, you will see that we have already
implemented some of the game logic. You can run the program by running
`python ./connect_four.py` in the terminal and quit the program by
pressing `Control-C`. Let's walk through the distribution code to make
sure we understand what is going on.

##### The Board

At the top of file, we define two variables, `BOARD_WIDTH` and
`BOARD_HEIGHT`. Just below where the variables are defined, they are
used to create the board, which is a list of lists. Each of the inner
lists represents a single **row** of the board. Each cell of the board
either contains `None`, which means it is empty, or the number of the
player whose token occupies that cell. The board is initialized to be
completely empty.


##### The Game Loop

At the bottom of the file, the high-level game logic is implemented in
a loop in `main`. Each turn is a single iteration of this loop. You
can see that on each turn the board is printed, and the current
player's input is processed. If the current player has won the final
board is printed and the loop is broken, ending the game. Otherwise,
if the current player did not win, the current player is switched and
a new turn begins.

At least, that's how it would work if all of the helper functions were
correctly implemented. Your job is to implement those helper functions
to make the game work.

### Your Mission

#### 1. Board Printing

If you run the program, you will quickly see that the board is not
very pretty. Your first task is to fix that by changing the
implementation of `print_board`. Feel free to make the board look like
anything you want, but you can use the layout below to as
inspiration. The only requirement is that the board be pretty.

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
represented with `.`.

#### 2. Validating Input

Next we need to be able to get input from the user. Right now the code
accepts any input, but we want the input to be validated, meaning bad
input should be rejected. Valid input is any integer between 1 and
`BOARD_WIDTH`, inclusive. The input identifies which column the user
wants to drop a token into. If the user enters bad input, they should
be repeatedly prompted until they enter valid input.

#### 3. Updating The Board

Now that we can get correct input from the user, we need to be able to
update the board accordingly. Go ahead and change the implementation
of `make_move` to update the board. `make_move` takes two arguments,
the `player` making the move and the `column` they want to
play. Remember that in Connect Four tokens always fall down as far as
possible, so there should never be an empty space under a token. Don't
worry about detecting wins yet; `make_move` should still just return
`False` at this point.

#### 4. Full Columns

Yay! Users can now take turns making moves. However, what happens if a
user plays on a full column? Try it out and see what happens. Your
code will probably either do nothing or crash. Neither result is what
we want, so go back to `get_move` and add to the input validation a
requirement that the chosen column is not full.

#### 5. Detecting Wins

The game is now fully playable except for the fact that it never
ends. Design an algorithm for checking if a player's move is a winning
move. Remember that a move is a winning move if it completes a
sequence of four identical tokens horizontally, vertically, or
diagonally. Implement your algorithm in `make_move`, returning `True`
if the move was a winning move and `False` otherwise.

This is the hardest part of this project, so we highly recommend that
you work with your neighbors to figure out a working algorithm.

#### 6. Handling Draws

Unfortunately the code currently has no way of detecting when a game
should be over because there are no more possible moves. Your final
task is to fix this in any way you see fit. Unlike the other tasks,
this one will require you to make changes to the game loop in `main`.


#### Bonus challenges

1. The distribution code uses four whole lines to switch the current
   player at the end of the turn. Can you figure out how to switch
   players with just one line of code?

2. Make the game have 3 players instead of just two.

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
   outer list. Does it work? Why or why not?
