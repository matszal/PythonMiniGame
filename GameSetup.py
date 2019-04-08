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

class GameObject:

    def __init__(self, image_path, x, y, width, height):
        object_image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(object_image, [width, height])
        self.x_pos = x
        self.y_pos = y
        self.width = width
        self.height = height

    def draw(self, background):
        background.blit(self.image, (self.x_pos, self.y_pos))

#class Player(GameObject):


pygame.init()

new_game = Game(SCREEN_TITLE, SCREEN_WIDTH, SCREEN_HEIGHT)
gameObject = GameObject('player.png', 150, 150, 50, 50)
#gameObject.draw(gameObject)
new_game.run_game_loop()

pygame.quit()
quit