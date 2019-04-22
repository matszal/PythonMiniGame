# simple python crossroad game
# made with the help of pygame library

# setup the display 
import pygame

# screen size
SCREEN_TITLE = "My pygame Game"
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 1000
level = 1

# color rgb representation
WHITE_COLOR = (255, 255, 255)
BLACK_COLOR = (0, 0, 0)

# clock setup
clock = pygame.time.Clock()
pygame.font.init()
font = pygame.font.SysFont('comicsans', 75)

class Game:
    # refresh rate
    TICK_RATE = 60

    def __init__(self, image_path, title, width, height ):
        self.title = title
        self.width = width
        self.height = height
        # create window of specific size
        self.game_window = pygame.display.set_mode((width, height))

        # setup window background color
        self.game_window.fill(WHITE_COLOR)
        pygame.display.set_caption(title)

        background_image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(background_image, (width, height))
    def run_game_loop(self, speed_increase):
        is_game_over = False
        did_win = False
        direction = 0

        #background = GameObject('background.png', )
        player_character = Player('player.png', 366, 800, 75, 75)
        enemy_character = Enemy('enemy.png', 20, 450, 50, 50)
        enemy_character.SPEED += speed_increase
        treasure = Enemy('treasure.png', 375, 50, 50, 50)
        # render all the graphics
        while not is_game_over:

            global level

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
            self.game_window.blit(self.image, (0, 0))
            enemy_character.move(SCREEN_WIDTH)
            enemy_character.draw(self.game_window)
            treasure.draw(self.game_window)
            scoretext = font.render('Level = '+str(level), 1, (0,0,0))
            self.game_window.blit(scoretext, (5, 10))
            player_character.move(direction, SCREEN_HEIGHT)
            if player_character.detect_collision(enemy_character):
                is_game_over = True
                did_win = False
                text = font.render('you lost', True, BLACK_COLOR)
                self.game_window.blit(text, (300,350))
                pygame.display.update()
                clock.tick(1)
                break
            if player_character.detect_collision(treasure):
                is_game_over = True
                did_win = True
                text = font.render('you won', True, BLACK_COLOR)
                level+=1
                
                pygame.display.update()
                clock.tick(1)
                break
            player_character.draw(self.game_window)

            pygame.display.update()
            clock.tick(self.TICK_RATE)
        if did_win:
            self.run_game_loop(speed_increase+3)
        else:
            return
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

    def detect_collision(self,other_body):
        if self.y_pos> other_body.y_pos-25 + other_body.height:
            return False
        elif self.y_pos + self.height < other_body.y_pos:
            return False
        if self.x_pos+20 > other_body.x_pos + other_body.width:
            return False
        elif self.x_pos-20 + self.width < other_body.x_pos:
            return False
        return True


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

new_game = Game('background.png', SCREEN_TITLE, SCREEN_WIDTH, SCREEN_HEIGHT)
new_game.run_game_loop(1)

pygame.quit()
quit
