import pygame, sys, random
from pygame.locals import *

# set up ppygame
pygame.init()
mainClock = pygame.time.Clock()

# set up the colors
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 255)
DEEPPINK = (255, 10, 247)
colorList = [RED, GREEN, BLUE, WHITE, DEEPPINK, YELLOW]

# set up the window
WINDOWWIDTH = 1000
WINDOWHEIGHT = 680
foodCounter = 0
NEWFOOD = 60
FOODSIZE = 10
PLAYERSIZE = 80

windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('myApp v 3.9.1')

# set up player and foods data structures
player = pygame.Rect(random.randint(0, WINDOWWIDTH - PLAYERSIZE), random.randint(0, WINDOWHEIGHT - PLAYERSIZE), PLAYERSIZE, PLAYERSIZE)
foods = []
for i in range(50):
    foods.append(pygame.Rect(random.randint(0, WINDOWWIDTH - FOODSIZE), random.randint(0, WINDOWHEIGHT - FOODSIZE), FOODSIZE, FOODSIZE))

# set up the movement data structures
moveLeft =False
moveRight = False
moveUp = False
moveDown = False

MOVESPEED = 10

playerColor = colorList[random.randint(0, 4)]
foodsColor = colorList[random.randint(0, 4)]
# run the game loop
while True:
    # check for events
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            # change the keyboard variables
            if event.key == K_LEFT or event.key == ord('a'):
                moveLeft = True
                moveRight = False
            if event.key == K_RIGHT or event.key == ord('d'):
                moveLeft = False
                moveRight = True
            if event.key == K_UP or event.key == ord('w'):
                moveUp = True
                moveDown = False
            if event.key == K_DOWN or event.key == ord('s'):
                moveUp = False
                moveDown = True
        if event.type == KEYUP:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == K_LEFT or event.key == ord('a'):
                moveLeft = False
            if event.key == K_RIGHT or event.key == ord('d'):
                moveRight = False
            if event.key == K_UP or event.key == ord('w'):
                moveUp = False
            if event.key == K_DOWN or event.key == ord('s'):
                moveDown = False
            if event.key == ord('g'):
                player.left = random.randint(0, WINDOWWIDTH - player.width)
                player.top = random.randint(0, WINDOWHEIGHT - player.height)

        if event.type == MOUSEBUTTONUP:
            foods.append(pygame.Rect(event.pos[0], event.pos[1], FOODSIZE, FOODSIZE))

    foodCounter += 1
    if foodCounter >= NEWFOOD:
        # add new food
        foodCounter = 0
        foods.append(pygame.Rect(random.randint(0, WINDOWWIDTH - FOODSIZE), random.randint(0, WINDOWHEIGHT - FOODSIZE), FOODSIZE, FOODSIZE))

    # draw the black background onto the surface
    windowSurface.fill(BLACK)

    # move player
    if moveLeft and (player.left > 0):
        player.left -= MOVESPEED
    if moveRight and (player.right < WINDOWWIDTH):
        player.right += MOVESPEED
    if moveDown and (player.bottom < WINDOWHEIGHT):
        player.bottom += MOVESPEED
    if moveUp and (player.top > 0):
        player.top -= MOVESPEED

    # draw the player onto the surface
    pygame.draw.rect(windowSurface, playerColor, player)

    # chect if player has intersected with any food squares
    for food in foods[:]:
        if player.colliderect(food):
            foods.remove(food)

    # draw the foods onto the surface
    for i in range(len(foods)):
        pygame.draw.rect(windowSurface, foodsColor, foods[i])

    # draw the surface onto the screen
    pygame.display.update()
    mainClock.tick(30)