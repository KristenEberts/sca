"""
Tic-Tac-Toe
Maria V Zlatkova
CS50 at HSA, July 2018
"""

def print_board(board):
    """ Pretty prints 3 x 3 Tic-Tac-Toe board """
    print('\n -----')
    print('|' + board[0][0] + '|' + board[0][1] + '|' + board[0][2] + '|')
    print(' -----')
    print('|' + board[1][0] + '|' + board[1][1] + '|' + board[1][2] + '|')
    print(' -----')
    print('|' + board[2][0] + '|' + board[2][1] + '|' + board[2][2] + '|')
    print(' -----\n')

def winner(board):
    """ Determines whether game has been won """
    for row in range(0,3):
        if ((board[row][0] == board[row][1] == board[row][2]) or
            (board[0][row] == board[1][row] == board[2][row])):
            return True

    if ((board[0][0] == board[1][1] == board[2][2]) or
        (board[0][2] == board[1][1] == board[2][0])):
        return True

    return False

def stalemate(board):
    """ Determines whether game has resulted in a stalemate """
    return all([all([r.isalpha() for r in row]) for row in board])

def main():
    # Create list of lists to represent the Tic-Tac-Toe board
    board = [[] for _ in range(0,3)]

    # Populate board with the numbers 1-9
    for row in range(0,3):
        for col in range(0,3):
            board[row].append(str(row * 3 + col + 1))

    # Begin with player 1 and symbol X
    X = True

    while not winner(board) and not stalemate(board):
        print_board(board)

        if X:
            print("Player 1")
        else:
            print("Player 2")

        # Get user choice
        choice = int(input("Move: ")) - 1

        # Ensure user selected number between 1-9
        if (not board[choice / 3][choice % 3].isdigit()
            or choice > 8 or choice < 0):
            print("Please select a free slot.")
        else:
            # Set selected slot to X or O
            if X:
                board[choice / 3][choice % 3] = 'X'
            else:
                board[choice / 3][choice % 3] = 'O'
            # It's the other player's turn
            X = not X

        if winner(board):
            print_board(board)
            print("Player " + str(int(X + 1)) + " wins!\n")
        elif stalemate(board):
            print_board(board)
            print("Draw!")

if __name__ == '__main__':
    main()
