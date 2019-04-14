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
        direction = 0

        player_character = Player('player.png', 325, 800, 150, 150)
        enemy_character = Enemy('enemy.png', 20, 400, 100, 100)
        # render all the graphics
        while not is_game_over:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    is_game_over = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        direction = 1
                    elif event.key == pygame.K_DOWN:
                        direction = -1
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        direction = 0        
                print(event)

            self.game_window.fill(WHITE_COLOR)
            enemy_character.move(SCREEN_WIDTH)
            enemy_character.draw(self.game_window)
            player_character.move(direction, SCREEN_HEIGHT)
            player_character.draw(self.game_window)

            pygame.display.update()
            clock.tick(self.TICK_RATE)


# class to represent game object
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

# class to represent character controlled by the player
class Player(GameObject, object):

    SPEED = 10

    def __init__(self, image_path, x, y, width, height):
        super(Player, self).__init__(image_path, x, y, width, height)
        
    def move(self, direction, max_height):
        if direction > 0:
            self.y_pos -= self.SPEED
        elif direction < 0:
            self.y_pos += self.SPEED

        if self.y_pos <= -40:
            self.y_pos = -40
        elif self.y_pos > max_height-150:
            self.y_pos = max_height-150


class Enemy(GameObject, object):

    SPEED = 5

    def __init__(self, image_path, x, y, width, height):
        super(Enemy, self).__init__(image_path, x, y, width, height)
        
    def move(self, max_width):
        if self.x_pos <= -20:
            self.SPEED = abs(self.SPEED)
        elif self.x_pos >= max_width - 70:
            self.SPEED = -abs(self.SPEED)
        self.x_pos += self.SPEED


pygame.init()

new_game = Game(SCREEN_TITLE, SCREEN_WIDTH, SCREEN_HEIGHT)
new_game.run_game_loop()

pygame.quit()
quit
