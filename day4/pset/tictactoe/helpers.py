"""
Tic Tac Toe with Pygame
Maria V Zlatkova
CS50 at HSA, July 2018

Adapted from https://github.com/msanatan
"""

import os
import sys
import pygame
from pygame.locals import *

# SDL is the library which Pygame uses to put the window at the screen center
os.environ['SDL_VIDEO_CENTERED'] = '1'
SCREEN_SIZE = (800, 640)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (50, 255, 50)
BLUE = (50, 50, 255)
RED = (255, 50, 50)
REPLAY_MESSAGE = 'Press space to play again'

pygame.init()
board_font = pygame.font.SysFont('arial', 80)
game_over_font = pygame.font.SysFont('monospace', 80, bold=True)
replay_font = pygame.font.SysFont('monospace', 50)
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption('Tic Tac Toe')
clock = pygame.time.Clock()

def initialize_board(screen_size, starting_config):
    # Create a list of lists to represent the 3 x 3 grid, outer list contains each row
    board = [[] for _ in range(3)]

    # Calculate width and height of each cell, with even space for each cell
    rect_width = int(screen_size[0] / 3)
    rect_height = int(screen_size[1] / 3)

    top = 0
    for row in range(3):
        left = 0

        # Loop over the inner list which has 3 cells per row
        for col in range(3):
            # Add a dictionary to represent each cell to the row
            board[row].append({
                'played': False,
                'symbol': "", # Could be X or O, empty string by default
                'rect': pygame.Rect(left, top, rect_width, rect_height)
            })
            # Add more to the left values so cells don't overlap
            left += rect_width
        # Ensure that the top values are increased for every row
        top += rect_height

    return board

def end_game_message(screen, screen_size, main_message, main_font,
        replay_message, replay_font, colour):
    main_text = main_font.render(main_message, False, colour)
    main_rect = main_text.get_rect(center=(screen_size[0]/2, screen_size[1]/2))
    screen.blit(main_text, main_rect)
    replay_text = replay_font.render(replay_message, False, colour)
    replay_rect = replay_text.get_rect(center=(screen_size[0]/2,
        main_rect.bottom + 30))
    screen.blit(replay_text, replay_rect)


def mouse_clicked(screen_size):
    rect_width = int(screen_size[0] / 3)
    rect_height = int(screen_size[1] / 3)
    row, col = pygame.mouse.get_pos()

    if row < rect_width:
        row =  0
    elif row >= rect_width and row < rect_width * 2:
        row = 1
    elif row > rect_width * 2 and row <= rect_width * 3:
        row = 2

    if col < rect_height:
        col = 0
    elif col >= rect_height and col < rect_height * 2:
        col = 1
    elif col > rect_height * 2 and col <= rect_height * 3:
        col =  2

    return col*3+row+1


def render(screen, screen_size, game, clock):
    screen.fill(WHITE)
    draw_lines(screen, screen_size)

    # Draw the letters if they're played
    for row in game['board']:
        for cell in row:
            if cell['symbol'] == 'X':
                draw_letter(screen, 'X', BLUE, cell['rect'])
            elif cell['symbol'] == 'O':
                draw_letter(screen, 'O', GREEN, cell['rect'])

    if game['win']:
        win_message = 'Player ' + game['current_player'] + ' won!'
        end_game_message(screen, SCREEN_SIZE, win_message, game_over_font,
                REPLAY_MESSAGE, replay_font, RED)
    elif not game['win'] and game['stalemate']:
        stale_message = 'Stalemate!'
        end_game_message(screen, SCREEN_SIZE, stale_message, game_over_font,
                REPLAY_MESSAGE, replay_font, RED)

    pygame.display.update()
    clock.tick(60)

def draw_lines(screen, screen_size):
    # Draw vertical lines from top of screen to bottom of screen
    vertical_line_1 = int(screen_size[0] / 3) # lines mark 1/3 of the board
    pygame.draw.line(screen, BLACK, (vertical_line_1, 0), (vertical_line_1, screen_size[0]), 4)
    vertical_line_2 = vertical_line_1 * 2
    pygame.draw.line(screen, BLACK, (vertical_line_2, 0), (vertical_line_2, screen_size[0]), 4)
    # Draw horizontal lines
    horizontal_line_1 = int(screen_size[1] / 3)
    pygame.draw.line(screen, BLACK, (0, horizontal_line_1), (screen_size[0], horizontal_line_1), 4)
    horizontal_line_2 = horizontal_line_1 * 2
    pygame.draw.line(screen, BLACK, (0, horizontal_line_2), (screen_size[0], horizontal_line_2), 4)


def draw_letter(screen, letter, colour, position_rect):
    player_choice = board_font.render(letter, False, colour)

    """ Fonts are draw to the top left of a Pygame rectangle. To center them,
    after generating font image, create a special rectangle
    that's the center of the cell's rectangle
    """

    choice_rect = player_choice.get_rect(center=position_rect.center)
    # Blit is Pygame's way of drawing an image to a rectangle
    screen.blit(player_choice, choice_rect)
