# simple python crossroad game
# made with the help of pygame library

# setup the display 
import pygame

# screen size
SCREEN_TITLE = "My pygame Game"
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 1000

# color rgb representation
WHITE_COLOR = (255, 255, 255)
BLACK_COLOR = (0, 0, 0)

# clock setup
clock = pygame.time.Clock()

class Game:
    # refresh rate
    TICK_RATE = 60

    def __init__(self, title, width, height ):
        self.title = title
        self.width = width
        self.height = height
        # create window of specific size
        self.game_window = pygame.display.set_mode((width, height))

        # setup window background color
        self.game_window.fill(WHITE_COLOR)
        pygame.display.set_caption(title)

    def run_game_loop(self):
        is_game_over = False
        # render all the graphics
        while not is_game_over:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    is_game_over = True
        
                print(event)

            pygame.display.update()
            clock.tick(self.TICK_RATE)

pygame.init()

new_game = Game(SCREEN_TITLE, SCREEN_WIDTH, SCREEN_HEIGHT)
new_game.run_game_loop()



#player_image = pygame.image.load('player.png')
#player_image = pygame.transform.scale(player_image, [150, 150])

  #pygame.draw.rect(game_window, BLACK_COLOR, [350, 450, 100, 100])
            #pygame.draw.circle(game_window, BLACK_COLOR, (400, 400), 50)
            #game_window.blit(player_image, (325, 825))

pygame.quit()
quit
