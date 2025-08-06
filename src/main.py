import pygame
from pygame.locals import FULLSCREEN

# constant vars
SCREEN_X = 1920
SCREEN_Y = 1080


def main():
    # pygame setup
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_X, SCREEN_Y), FULLSCREEN)


if __name__ == "__main__":
    main()
