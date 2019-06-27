import os
import sys
import random
import pygame


# game settings
FPS = 60
SCREEN_WIDTH, SCREEN_HEIGHT = 640, 480
ASTEROID_PROBABILITY = 0.01


# initialize pygame objects
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()


# load assets
ship_sprite = pygame.image.load(os.path.join("assets", "ship.png")).convert_alpha()
asteroid_sprite = pygame.image.load(os.path.join("assets", "asteroid.png")).convert_alpha()


class Entity:
    def __init__(self, sprite, x, y, angle=0, vel_x=0, vel_y=0, vel_angle=0):
        self.sprite = sprite
        self.radius = sprite.get_width() * .4
        self.x = x
        self.y = y
        self.angle = angle
        self.vel_x = 0
        self.vel_y = 0
        self.vel_angle = 0

    def update(self):
        self.x += self.vel_x
        self.y += self.vel_y
        self.angle += self.vel_angle

    def draw(self, screen):
        rotated = pygame.transform.rotate(self.sprite, self.angle)
        dest = pygame.Rect(self.x - rotated.get_width() / 2,
                           self.y - rotated.get_height() / 2,
                           rotated.get_width(),
                           rotated.get_height())
        screen.blit(rotated, dest)

    def intersects(self, other):
        diff_x = self.x - other.x
        diff_y = self.y - other.y
        hypotenuse = self.radius + other.radius
        return diff_x * diff_x + diff_y * diff_y <= hypotenuse * hypotenuse


def main():
    ship = Entity(ship_sprite, 200, 200)
    asteroids = []

    # input
    up = False
    down = False
    left = False
    right = False
    rleft = False
    rright = False

    while True:
        # handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # shut down window and end program
                pygame.display.quit()
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    up = True
                elif event.key == pygame.K_a:
                    left = True
                elif event.key == pygame.K_s:
                    down = True
                elif event.key == pygame.K_d:
                    right = True
                elif event.key == pygame.K_j:
                    rleft = True
                elif event.key == pygame.K_k:
                    rright = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    up = False
                elif event.key == pygame.K_a:
                    left = False
                elif event.key == pygame.K_s:
                    down = False
                elif event.key == pygame.K_d:
                    right = False
                elif event.key == pygame.K_j:
                    rleft = False
                elif event.key == pygame.K_k:
                    rright = False

        # determine movement
        ship.vel_x = 0
        if left and not right:
            ship.vel_x = -10
        elif right and not left:
            ship.vel_x = 10

        ship.vel_y = 0
        if up and not down:
            ship.vel_y = -10
        elif down and not up:
            ship.vel_y = 10

        ship.vel_angle = 0
        if rleft and not rright:
            ship.vel_angle = 10
        elif rright and not rleft:
            ship.vel_angle = -10

        # possibly add asteroid
        if random.random() < ASTEROID_PROBABILITY:
            x = random.random() * SCREEN_WIDTH
            y = random.random() * SCREEN_HEIGHT
            asteroids.append(Entity(asteroid_sprite, x, y))

        # update game state
        for asteroid in asteroids:
            asteroid.update()
        ship.update()

        # clear screen
        screen.fill((0,0,0))

        # draw game objects
        ship.draw(screen)
        for asteroid in asteroids:
            asteroid.draw(screen)

        # display updated screen and wait
        pygame.display.flip()
        clock.tick(FPS)


if __name__ == "__main__":
    main()
