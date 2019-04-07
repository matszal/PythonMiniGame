# simple python crossroad game
# made with the help of pygame library

# setup the display 
import pygame

# screen size
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
# color rgb representation
WHITE_COLOR = (255, 255, 255)
BLACK_COLOR = (0, 0, 0)

# clock setup
clock = pygame.time.Clock()
# tick rate
TICK_RATE = 60
# continue game
is_game_over = False

# create window of specific size
game_window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# setup window background color
game_window.fill(WHITE_COLOR)

# render all the graphics
while not is_game_over:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_game_over = True

    pygame.display.update()
    clock.tick(TICK_RATE)

pygame.quit()
quit
