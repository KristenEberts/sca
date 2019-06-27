"""
Snake using Pygame
Maria V Zlatkova
CS50 at HSA, July 2018

Adapted from https://github.com/ternus
"""

import pygame
import sys
import time
import random
from pygame.locals import *

# Constants
FPS = 15
SCREEN_WIDTH, SCREEN_HEIGHT = 640, 480
GRIDSIZE = 10
GRID_WIDTH = SCREEN_WIDTH / GRIDSIZE
GRID_HEIGHT = SCREEN_HEIGHT / GRIDSIZE
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# Initial setup
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
surface = pygame.Surface(screen.get_size()).convert()
clock = pygame.time.Clock()

def main():
    snake = Snake()
    apple = Apple()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_UP:
                    snake.point(UP)
                elif event.key == K_DOWN:
                    snake.point(DOWN)
                elif event.key == K_LEFT:
                    snake.point(LEFT)
                elif event.key == K_RIGHT:
                    snake.point(RIGHT)

        # Refill as snake moves so that the path it took doesn't remain black
        surface.fill((255,255,255))

        # Keep moving snake forward
        snake.move()

        # Check if snake reached apple
        check_eat(snake, apple)

        # Draw snake and apple on surface
        snake.draw(surface)
        apple.draw(surface)

        # Set up score indicator with the value of the snake length
        score = pygame.font.Font(None, 36).render(str(snake.length),
                                                  1, (10, 10, 10))
        score_position = score.get_rect()
        score_position.centerx = 20

        # Draw surface (background) and  score onto the window
        surface.blit(score, score.get_rect())
        screen.blit(surface, (0,0))

        # Update the contents of the entire display
        pygame.display.flip()

        # Delay snake movement for better gameplay
        clock.tick(FPS + snake.length / 3)

def draw_box(surface, color, position):
    """Draw each rectangle that makes up the snake or apple"""
    pygame.draw.rect(surface,
                     color,
                     pygame.Rect((position[0], position[1]),
                                 (GRIDSIZE, GRIDSIZE)))

def check_eat(snake, apple):
    """ Checks whether snake reached and ate apple"""
    # TODO if snake reached apple, increase snake length by 1
    # and randomly place apple in new position

class Snake():
    def __init__(self):
        self.restart()
        self.color = (0,0,0)

    # Method to initialize position, direction and length when game is restarted
    def restart(self):
        # TODO Set snake length, position and direction to initial values
        print("restart unimplemented")

    # Method returns the position of the head/front of the snake
    def get_head_position(self):
        # TODO Return position of snake head
        return (0, 0)

    # Method to point snake in new direction, specified by point
    def point(self, point):
        # TODO Point snake in new direction
        print("point unimplemented")

    # Method to move snake forward
    def move(self):
        # Calculate current position and direction
        cur_position = self.positions[0]
        x, y = self.direction

        # Calculate new position to advance snake forward
        new_position = (((cur_position[0] + (x * GRIDSIZE)) % SCREEN_WIDTH),
                        (cur_position[1] + (y * GRIDSIZE)) % SCREEN_HEIGHT)

        # TODO Move snake forward

    # Method to draw snake on surface
    def draw(self, surface):
        for p in self.positions:
            draw_box(surface, self.color, p)

class Apple():
    def __init__(self):
        self.position = (0,0)
        self.color = (255,0,0)
        self.randomize()

    # Method to place apple in random location
    def randomize(self):
        #TODO Set apple's position to random location on screen
        print("randomize not implemented")

    # Method to draw apple
    def draw(self, surface):
        draw_box(surface, self.color, self.position)

if __name__ == '__main__':
    main()
