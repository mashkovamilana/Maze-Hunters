from pygame import *

window = display.set_mode((1600, 900))
display.set_caption('Maze Hunters')
background = transform.scale(image.load('images/background.png'), (1600, 900))
death_state = transform.scale(image.load('images/death_state.png'), (500, 500))
welcome_state = transform.scale(image.load('images/welcome_state.png'), (500, 500))
next_level = transform.scale(image.load('images/next_level.png'), (500, 500))
finish = transform.scale(image.load('images/finish.png'), (500, 500))

game = True
state = 'start'
FPS = 60
clock = time.Clock()
state_timer = 0
active_level = 0


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
        if keys_pressed[K_s] and self.rect.y < 850:
            self.rect.y += self.speed
        if keys_pressed[K_d] and self.rect.x < 1550:
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
treasure = GameSprite('images/diamond blue.png', 1540, 320, 0)

walls = []
enemies = []
levels = []


def level1():
    global enemies, walls, player, treasure
    walls = [Wall(0, 150), Wall(0, 0), Wall(560, 300), Wall(650, 300), Wall(1250, 250), WallH(50, 150), WallH(50, 0),
             WallH(200, 0), WallH(350, 300), WallH(200, 450), WallH(300, 450), WallH(450, 450), WallH(500, 300),
             WallH(600, 600), WallH(700, 600), WallH(850, 400), WallH(800, 600), WallH(950, 600), WallH(950, 400),
             WallH(1100, 600), WallH(1250, 600), WallV(1400, 500), WallV(1400, 400), WallV(1400, 500), WallH(1450, 400),
             WallH(1450, 250), WallH(1300, 250), WallV(1250, 300), WallH(1100, 400), WallH(700, 400), WallV(200, 150),
             WallV(350, 0), WallV(350, 150), WallV(200, 300), WallV(700, 300), WallV(550, 500)]
    enemies = [EnemyV('images/sprite2.png', 100, 50, 3, 700), EnemyH('images/sprite3.png', 0, 400, 3, 1500)]
    player = Player('images/sprite1.png', 50, 50, 10)
    treasure = GameSprite('images/diamond blue.png', 1540, 320, 0)


def level2():
    global enemies, walls, player, treasure
    walls = [Wall(0, 150), Wall(0, 0), Wall(560, 300), Wall(650, 300), Wall(1250, 250), WallH(50, 150), WallH(50, 0),
             WallH(200, 0), WallH(350, 300), WallH(200, 450), WallH(300, 450), WallH(450, 450), WallH(500, 300),
             WallH(600, 600), WallH(700, 600), WallH(850, 400), WallH(800, 600), WallH(950, 600), WallH(950, 400),
             WallH(1100, 600), WallH(1250, 600), WallV(1400, 500), WallV(1400, 400), WallV(1400, 500), WallH(1450, 400),
             WallH(1450, 250), WallH(1300, 250), WallV(1250, 300), WallH(1100, 400), WallH(700, 400), WallV(200, 150),
             WallV(350, 0), WallV(350, 150), WallV(200, 300), WallV(700, 300), WallV(550, 500)]
    enemies = [EnemyV('images/sprite2.png', 0, 50, 5, 700), EnemyH('images/sprite3.png', 0, 300, 5, 1400),
               EnemyV('images/sprite4.png', 50, 500, 5, 600), EnemyH('images/sprite5.png', 300, 400, 5, 1100)]
    player = Player('images/sprite1.png', 50, 50, 10)
    treasure = GameSprite('images/diamond blue.png', 1540, 320, 0)


levels.append(level1)
levels.append(level2)

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    window.blit(background, (0, 0))

    if state == 'game':
        player.update()
        player.reset()
        treasure.reset()
        if player.colliding_with(treasure):
            state = 'next_level'
        for wall in walls:
            wall.update()
            wall.reset()
            if player.colliding_with(wall):
                state = 'death'
        for enemy in enemies:
            enemy.update()
            enemy.reset()
            if player.colliding_with(enemy):
                state = 'death'
    elif state == 'death':
        window.blit(death_state, (550, 200))
        state_timer += 1
        if state_timer == 120:
            levels[active_level]()
            state = 'game'
            state_timer = 0
    elif state == 'next_level':
        window.blit(next_level, (550, 200))
        state_timer += 1
        if state_timer == 120:
            active_level += 1
            if len(levels) == active_level:
                state = 'finish'
            else:
                levels[active_level]()
                state = 'game'
            state_timer = 0
    elif state == 'finish':
        window.blit(finish, (550, 200))
        state_timer += 1
        if state_timer == 120:
            active_level = 0
            levels[active_level]()
            state = 'game'
            state_timer = 0
    elif state == 'start':
        window.blit(welcome_state, (550, 200))
        state_timer += 1
        if state_timer == 120:
            levels[active_level]()
            state = 'game'
            state_timer = 0

    display.update()
    clock.tick(FPS)
