import pygame
from pygame import mixer

pygame.init()

import os

os.environ["SDL_VIDEO_WINDOW_POS"] = "%d,%d" % (20, 20)

screen = pygame.display.set_mode((700, 1000))
pygame.display.set_caption("Lunar Lander FInal")

# Game Variables
doExit = False
clock = pygame.time.Clock()
FPS = 60

# Player Variables
xPos = 0
yPos = 0
xVel = 0
yVel = 0

LEFT = 0
RIGHT = 1
UP = 2
keys = [False, False, False]

isOnGround = False
rocketOn = False
crashed = False

# Fonts and strings to render
pygame.font.init()
font = pygame.font.SysFont("Comic Sans Ms", 30)
text1 = font.render("Vertical Velocity:", False, (0, 200, 200))
text2 = font.render(str(int(yVel)), 1, (0, 200, 200))
text3 = font.render("YOU CRASHED!", False, (200, 50, 50))
text4 = font.render("Vertical velocity:", False, (200, 20, 20))
text5 = font.render(str(int(yVel)), 1, (200, 20, 200))
text6 = font.render("Height:", False, (200, 20, 20))
text7 = font.render(str(int(yPos)), 1, (20, 20, 200))

while not doExit:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            doExit = True

    # Input Section
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            keys[LEFT] = True
        elif event.key == pygame.K_RIGHT:
            keys[RIGHT] = True
        elif event.key == pygame.K_UP:
            keys[UP] = True
    elif event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT:
            keys[LEFT] = False
        elif event.key == pygame.K_RIGHT:
            keys[RIGHT] = False
        elif event.key == pygame.K_UP:
            keys[UP] = False

    # Physics Section
    if keys[LEFT] == True:
        xVel = -1 / 60
    elif keys[RIGHT] == True:
        xVel = 1 / 60
    elif keys[UP] == True:
        yVel = 0.417 / 60
        isOnGround = False
        rocketOn = True
    else:
        xVel = 0
        yVel = 0
        rocketOn = False

    if isOnGround == False:
        yVel = 1

    xPos += xVel
    yPos += yVel

    # Render Section

pygame.quit()
