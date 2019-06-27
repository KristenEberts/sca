# connect_four.py
#
# Implements a command-line version of the classic game "Connect Four"

from cs50 import get_string


BOARD_WIDTH = 7
BOARD_HEIGHT = 6


# initialize the board to be empty (all None)
board = []
for row in range(BOARD_HEIGHT):
    board.append([None] * BOARD_WIDTH)


def print_board():
    """Prints the game state to the terminal"""
    # TODO: make this output pretty
    for row in board:
        print(row)


def get_move():
    """Validates and returns player's input"""
    # TODO: validate input
    column = get_string("input: ")
    return column


def make_move(player, column):
    """Insert a token for `player` in the given column of the
    board. Return True if that is a winning move and False
    otherwise.
    """
    return False


def main():
    """Implements the game loop including input and output"""
    current_player = 1
    while True:
        # print game information
        print_board()
        print(f"Player {current_player}'s turn")

        # take move
        column = get_move()
        did_win = make_move(current_player, column)

        if did_win:
            # current player won, so print winner and exit
            print_board()
            print(f"Player {current_player} wins!")
            break

        # switch current player
        if current_player == 1:
            current_player = 2
        else:
            current_player = 1


if __name__ == "__main__":
    main()
