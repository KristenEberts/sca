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
    # print column numbers at top
    nums = []
    for i in range(1, BOARD_WIDTH + 1):
        nums.append(str(i))
    print(f"|{' '.join(nums)}|")

    # print rows
    for row in board:
        cells = []
        for cell in row:
            if cell == None:
                cells.append(".")
            elif cell == 1:
                cells.append("X")
            elif cell == 2:
                cells.append("O")
        print(f"|{' '.join(cells)}|")


def get_move():
    """Validates and returns player's input"""
    while True:
        column = get_string("input: ")
        if not column.isdigit():
            continue

        # get 0-indexed column
        column = int(column) - 1
        if column < 0 or column >= BOARD_WIDTH:
            continue

        # check for empty space
        if board[0][column] != None:
            continue

        # return 0-indexed column
        return column


def make_move(player, column):
    """Insert a token for `player` in the given column of the
    board. Return True if that is a winning move and False
    otherwise.
    """
    # find last empty row
    row = 0
    while row + 1 < BOARD_HEIGHT and board[row + 1][column] == None:
        row += 1

    # place token
    board[row][column] = player

    # iterate through win directions
    dirs = [(0, 1), (1, 1), (1, 0), (-1, 1)]
    for row_diff, col_diff in dirs:
        adjacent = 1

        # probe forward and backward
        for direction in [1, -1]:
            probe_row = row + row_diff * direction
            probe_col = column + col_diff * direction

            # probe until out of bounds or wrong contents
            while (probe_row >= 0 and probe_row < BOARD_HEIGHT and
                   probe_col >= 0 and probe_col < BOARD_WIDTH and
                   board[probe_row][probe_col] == player):
                adjacent += 1
                probe_row += row_diff * direction
                probe_col += col_diff * direction

        # win if at least four adjacent in this direction
        if adjacent >= 4:
            return True
    # no wins
    return False


def main():
    """Implements the game loop including input and output"""
    current_player = 1
    did_win = False
    for _ in range(BOARD_WIDTH * BOARD_HEIGHT):
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

    # check for draw
    if not did_win:
        print_board()
        print("It's a draw!")


if __name__ == "__main__":
    main()
