#создай игру "Лабиринт"!
from pygame import *
#создай окно игры
window = display.set_mode((700, 500))
display.set_caption('Maze')
clock = time.Clock()
mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()
FPS = 60
background = transform.scale(image.load('background.jpg'), (700, 500))
x = 0
y = 0
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (75, 75))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__(player_image, player_x, player_y, player_speed)
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 10:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 395:
            self.rect.y += self.speed
        if keys_pressed[K_LEFT] and self.rect.x > 10:
            self.rect.x -= self.speed
        if keys_pressed[K_RIGHT] and self.rect.x < 620:
            self.rect.x += self.speed




class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_heidth):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = wall_width
        self.heidth = wall_heidth
        self.image = Surface((self.width, self.heidth)) 
        self.image.fill((color_1, color_2, color_3)) 
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

sprite = Player(('hero.png'), 50, 350, 10)
sprite2 = GameSprite(('cyborg.png'), 620, 250, 10)
sprite3 = GameSprite(('treasure.png'), 590, 370, 0)



game = True

while game:
    
    
    window.blit(background, (0, 0))
    
    sprite.reset()
    sprite2.reset()
    sprite3.reset()

    sprite.update()

    for e in event.get():   
        if e.type == QUIT:
            game = False

    clock.tick(FPS)
    display.update()
    