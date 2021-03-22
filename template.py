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

# game loop
while playing:
    #Events handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
    #Game logic goes here

    #Drawing goes here
    screen.fill([255, 0, 0])

    # This must be at the end of the drawing
    pygame.display.flip()

    # Set the FPS to 60
    clock.tick(60)
        