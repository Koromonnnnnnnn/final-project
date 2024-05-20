import pygame
from pygame import mixer

pygame.init()
mixer.init()

import os

os.environ["SDL_VIDEO_WINDOW_POS"] = "%d,%d" % (20, 20)

# Create game window
screenWidth = 700
screenHeight = 1000

screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Lunar Lander Final")

# Game Variables
doExit = False
clock = pygame.time.Clock()
FPS = 60

music = pygame.mixer.music.load("01.mp3")
pygame.mixer.music.set_volume(0.35)
pygame.mixer.music.play(-1)

# Player Variables
xPos = screenWidth // 2
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
fuel = 150

# Fonts and strings to render
pygame.font.init()
font = pygame.font.SysFont("Comic Sans Ms", 30)
text1 = font.render("Vertical Velocity:", False, (0, 200, 200))
text2 = font.render(str(int(yVel)), 1, (0, 200, 200))
text3 = font.render("YOU CRASHED!", False, (200, 50, 50))
text4 = font.render("Vertical Velocity:", False, (200, 20, 20))
text5 = font.render(str(int(yVel)), 1, (200, 20, 20))
text6 = font.render("Height:", False, (200, 20, 20))
text7 = font.render(str(int(yPos)), 1, (20, 20, 200))
text8 = font.render("Fuel:", False, (20, 200, 20))
text9 = font.render(str(fuel), 1, (20, 200, 20))


# This function below was NOT created by me
def reset_game():
    global xPos, yPos, xVel, yVel, fuel, isOnGround, crashed
    xPos = screenWidth // 2
    yPos = 0
    xVel = 0
    yVel = 0
    fuel = 150
    isOnGround = False
    crashed = False


reset_game()

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

    # Left and right movement
    if keys[LEFT]:
        xVel -= 0.1
    elif keys[RIGHT]:
        xVel += 0.1
    else:
        xVel *= 0.99

    # Up/down velocity
    if keys[UP] and fuel > 0:
        yVel -= 0.1
        rocketOn = True
        isOnGround = False
        fuel -= 1
    else:
        rocketOn = False
        if not isOnGround:
            yVel += 1.62 / FPS  # Moon gravitational pull

    # Update position
    xPos += xVel
    yPos += yVel

    # Boundaries (Lander kept falling out of the screen so the code wouldn't register a crash. That's why I added these)
    if xPos < 0:
        xPos = 0
        xVel = 0
    elif xPos > screenWidth - 50:
        xPos = screenWidth - 50
        xVel = 0

    if yPos >= screenHeight - 50:
        isOnGround = True
        yPos = screenHeight - 50

        if abs(yVel) > 2:
            crashed = True
            screen.blit(text3, (200, 500))
            pygame.display.update()
            pygame.time.wait(1000)
            reset_game()
        else:
            yVel = 0

    text2 = font.render(str("%.2f" % (yVel * -1)), 1, (0, 200, 200))
    text5 = font.render(str("%.2f" % (yVel * -1)), 1, (200, 20, 20))
    text7 = font.render(str(int(screenHeight - yPos)), 1, (20, 20, 200))
    text9 = font.render(str(fuel), 1, (20, 200, 20))

    # Render Section
    screen.fill((0, 0, 0))  # Clear screen

    # Draw the lander
    pygame.draw.rect(screen, (255, 255, 255), (xPos, yPos, 50, 50))
    if rocketOn:
        pygame.draw.ellipse(
            screen, (255, 255, 0), (xPos + 10, yPos + 50, 30, 50)
        )  # Rocket fire

    # Display text
    screen.blit(text1, (10, 10))
    screen.blit(text2, (250, 10))
    screen.blit(text6, (10, 50))
    screen.blit(text7, (150, 50))
    screen.blit(text8, (10, 90))
    screen.blit(text9, (100, 90))

    pygame.display.update()

pygame.quit()
