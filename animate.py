import pygame

# This line must be in all pygames
pygame.init()
# variable to hold the screen size
size = [700, 500]
# variable to hold a reference to the screen
screen = pygame.display.set_mode(size)
# variable to control the game loop
playing = True
# variable is used to control how fast the screen updates
clock = pygame.time.Clock()
# Control position and velocity
xPos = 10
yPos = 10
xVel = 2
yVel = 2

# Colors
RED = [225, 0, 0]
BLACK = [0, 0, 0]
WHITE = [255, 255, 255]
# game loop
while playing:
    #Events handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
    #Game logic goes here
    if xPos < 0 or xPos > size[0]:
        xVel = xVel * -1
    if yPos < 0 or yPos > size[1]:
        yVel = yVel * -1

    #Drawing goes here
    screen.fill(RED)
    pygame.draw.rect(screen, BLACK, [xPos, yPos, 50, 50], )


    # This must be at the end of the drawing
    pygame.display.flip()

    xPos = xPos + xVel
    yPos = yPos + yVel
    
    # Set the FPS to 60
    clock.tick(60)
        