import pygame
from pygame import mixer

pygame.init()

import os
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (20,20)

screen = pygame.display.set_mode((700, 1000))
pygame.display.set_caption("Lunar Lander FInal")

#Game Variables
doExit = False
clock = pygame.time.Clock()