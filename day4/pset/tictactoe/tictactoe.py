"""
Tic-Tac-Toe with Pygame
Maria V Zlatkova
CS50 at HSA, July 2018

Adapted from https://github.com/msanatan
"""

from helpers import *

def winner(board, symbol):
    """ TODO Return True if there is a winning row, column or diagonal,
    else return False
    """
    return False

def is_stalemate(board):
    """ TODO Return True if there is a stalemate, else return False """
    return False

def update(game, cell_clicked):
    """ Update the board by filling in the clicked cell
    with the appropriate symbol
    """

    for row in range(0,3):
        for col in range(0,3):
            key = row * 3 + col + 1

            if (cell_clicked == key and not game['board'][row][col]['played']):
                game['board'][row][col]['played'] = True
                game['board'][row][col]['symbol'] = game['current_player']
                return True

    return False

def main():
    def initialize(starting_config):
        return {
                'board': initialize_board(SCREEN_SIZE, starting_config),
                'current_player':  'X',
                'win': False,
                'stalemate': False,
                'change_player': False
                }

    if len(sys.argv) > 1:
        game = initialize(sys.argv[1])
    else:
        game = initialize("")

    while True:
        cell_clicked=0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                cell_clicked = mouse_clicked(SCREEN_SIZE)
                print(cell_clicked)

        keys_pressed = pygame.key.get_pressed()
        if not (game['win'] or game['stalemate']):
            game['change_player'] = update(game, cell_clicked)
        else:
            # Reset the game by pressing space bar
            if keys_pressed[pygame.K_SPACE]:
                game = initialize()

        # TODO
        # Update game['win'] and game['stalemate']

        render(screen, SCREEN_SIZE, game, clock)

        # TODO
        # If the last move didn't win/end the game, switch to the other player

if __name__ == '__main__':
    main()
