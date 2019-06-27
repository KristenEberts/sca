"""
Pong using Pygame
Spencer L Tiberi
HSA SCA, July 2018

"""

# imports
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
RADIUS = 10
PAD_WIDTH = 20
PAD_HEIGHT = 100

# Initial setup
pygame.init()
pygame.display.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
surface = pygame.Surface(screen.get_size()).convert()
clock = pygame.time.Clock()

def main():
    ball = Ball()
    leftPaddle = Paddle(K_w, K_s, (5, SCREEN_HEIGHT/2 - PAD_HEIGHT/2), (255,255,255))
    rightPaddle = Paddle(K_UP, K_DOWN, (SCREEN_WIDTH - PAD_WIDTH - 5, SCREEN_HEIGHT/2 - PAD_HEIGHT/2), (255,255,255))

    while True:
        screen.fill((0,0,0))
        leftPaddle.draw()
        rightPaddle.draw()
        ball.move()

        # Bounce of floor and ceiling, paddle, or reset
        if ball.y <= 0 or ball.y >= SCREEN_HEIGHT:
            ball.dy = -ball.dy
        if ball.touching(leftPaddle) or ball.touching(rightPaddle):
            ball.dx = -ball.dx
        if ball.x <= 0:
            ball.reset()

        elif ball.x >= SCREEN_WIDTH:
            ball.reset()

        ball.draw((ball.x, ball.y))

        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key in (K_w, K_s):
                    leftPaddle.move(event.key)
                elif event.key in (K_UP, K_DOWN):
                    rightPaddle.move(event.key)
            elif event.type == KEYUP:
                if event.key in (K_w, K_s):
                    leftPaddle.stop()
                elif event.key in (K_UP, K_DOWN):
                    rightPaddle.stop()
            elif event.type == QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()

class Ball():
    def __init__(self):
        self.color = (255,255,255)
        self.reset()

    def draw(self, position):
        pygame.draw.circle(screen, self.color, position, RADIUS)

    def move(self):
        self.x += self.dx
        self.y += self.dy

    def reset(self):
        self.x = SCREEN_WIDTH//2
        self.y = SCREEN_HEIGHT//2
        self.dx = random.choice((-8,-7,-6,-5,5,6,7,8))
        self.dy = random.choice((-8,-7,-6,-5,-4,-3,-2,-1,1,2,3,4,5,6,7,8))
        self.draw((self.x, self.y))

    def touching(self, paddle):
        return self.y <= paddle.y + PAD_HEIGHT and self.y >= paddle.y and \
               self.x >= paddle.x and self.x <= paddle.x + PAD_WIDTH

class Paddle():
    def __init__(self, up, down, position, color):
        self.x = position[0]
        self.y = position[1]
        self.color = color
        self.up = up
        self.down = down
        self.velocity = 0
        self.draw()

    def move(self, key):
        if key == self.up:
            self.velocity = -8
        elif key == self.down:
            self.velocity = 8

    def stop(self):
            self.velocity = 0
        # Set paddle velocity to 0

    def draw(self):
        self.y += self.velocity
        pygame.draw.rect(screen, self.color, (self.x, self.y, PAD_WIDTH, PAD_HEIGHT))

if __name__ == '__main__':
    main()
