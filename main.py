from pygame import *

window = display.set_mode((1600, 900))
display.set_caption('Maze Hunters')
background = transform.scale(image.load('images/background.png'), (1600, 900))

game = True
FPS = 60
clock = time.Clock()


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, x, y, speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (50, 50))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

    def colliding_with(self, other):
        collide = sprite.collide_rect(self, other)
        return collide


class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 450:
            self.rect.y += self.speed
        if keys_pressed[K_d] and self.rect.x < 650:
            self.rect.x += self.speed
        if keys_pressed[K_a] and self.rect.x > 0:
            self.rect.x -= self.speed

class EnemyV(GameSprite):
    def __init__(self, player_image, x, y, speed, distance):
        super().__init__(player_image, x, y, speed)
        self.direction = True
        self.y1 = y
        self.y2 = self.y1 + distance

    def update(self):
        if self.direction:
            self.rect.y += self.speed
            if self.rect.y >= self.y2:
                self.direction = False
        else:
            self.rect.y -= self.speed
            if self.rect.y <= self.y1:
                self.direction = True

class EnemyH(GameSprite):
    def __init__(self, player_image, x, y, speed, distance):
        super().__init__(player_image, x, y, speed)
        self.direction = True
        self.x1 = x
        self.x2 = self.x1 + distance

    def update(self):
        if self.direction:
            self.rect.x += self.speed
            if self.rect.x >= self.x2:
                self.direction = False
        else:
            self.rect.x -= self.speed
            if self.rect.x <= self.x1:
                self.direction = True

class Wall(sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = transform.scale(image.load('images/wall.png'), (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class WallV(sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = transform.scale(image.load('images/wallV.png'), (50, 150))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class WallH(sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = transform.scale(image.load('images/wallH.png'), (150, 50))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))



player = Player('images/sprite1.png', 50, 50, 10)
walls = []
walls.append(Wall(0, 150))
walls.append(Wall(0, 0))
walls.append(Wall(560, 300))
walls.append(Wall(650, 300))
walls.append(Wall(1250, 250))
walls.append(WallH(50, 150))
walls.append(WallH(50, 0))
walls.append(WallH(200, 0))
walls.append(WallH(350, 300))
walls.append(WallH(200, 450))
walls.append(WallH(300, 450))
walls.append(WallH(450, 450))
walls.append(WallH(500, 300))
walls.append(WallH(600, 600))
walls.append(WallH(700, 600))
walls.append(WallH(850, 400))
walls.append(WallH(800, 600))
walls.append(WallH(950, 600))
walls.append(WallH(950, 400))
walls.append(WallH(1100, 600))
walls.append(WallH(1250, 600))
walls.append(WallV(1400, 500))
walls.append(WallV(1400, 400))
walls.append(WallV(1400, 500))
walls.append(WallH(1450, 400))
walls.append(WallH(1450, 250))
walls.append(WallH(1300, 250))
walls.append(WallV(1250, 300))
walls.append(WallH(1100, 400))
walls.append(WallH(700, 400))
walls.append(WallV(200, 150))
walls.append(WallV(350, 0))
walls.append(WallV(350, 150))
walls.append(WallV(200, 300))
walls.append(WallV(700, 300))
walls.append(WallV(550, 500))
enemies = []
enemies.append(EnemyV('images/sprite2.png', 0, 50, 3, 400))
enemies.append(EnemyH('images/sprite3.png', 0, 300, 3, 600))

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    window.blit(background, (0, 0))
    player.update()
    player.reset()
    for wall in walls:
        wall.update()
        wall.reset()
    for enemy in enemies:
        enemy.update()
        enemy.reset()
    display.update()
    clock.tick(FPS)
