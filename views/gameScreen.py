import datetime
import pygame
import random
import math
import os
import time
import menuStructure as menuS
import main as main
from assets import values
from fileio import settingIO
from fileio import statsIO
from fileio import highScoreIO
from fileio import customizationIO
from views import gameScreen

global BACKGROUND_IMG
global DUCK_IMG
global noiseMaker

#import menuStructure as menuS

GRID_SIZE = 64
FPS = 30

pygame.init()
#CONTROLS

#for some reason this is causing an error when running tests
#AttributeError: module 'fileio.settingIO' has no attribute 'keys'
if settingIO.keys == "wasd":
    UP = pygame.K_w
    DOWN = pygame.K_s
    LEFT = pygame.K_a
    RIGHT = pygame.K_d
elif settingIO.keys == "arrows":
    UP = pygame.K_UP
    DOWN = pygame.K_DOWN
    LEFT = pygame.K_LEFT
    RIGHT = pygame.K_RIGHT

pygame.display.init()
pygame.display.set_mode((0, 0), flags=pygame.FULLSCREEN)
SCREEN = pygame.display.get_surface()
WIDTH = SCREEN.get_width()
HEIGHT = SCREEN.get_height()

FONT = pygame.font.Font("assets/fonts/ethnocentric.ttf", 64)
FONT_SM = pygame.font.Font("assets/fonts/ethnocentric.ttf", 32)
FONT_LG = pygame.font.Font("assets/fonts/ethnocentric.ttf", 96)


def loadImage(filePath, scale):
    img = pygame.image.load(filePath)
    if scale:
        img = pygame.transform.scale(img, (GRID_SIZE, GRID_SIZE))
    return img


#COLORS
TRANSPARENT = (0, 0, 0, 0)
WHITE = (255, 255, 255)

#Image loading
BLOCK_IMG = loadImage(os.path.join("assets", "sprites", "Wall_block.png"),
                      scale=True)
BLOCK_IMG2 = pygame.transform.flip(BLOCK_IMG, False, True)
DUCK_IMG = loadImage(values.current_skin, scale=True)
SWAG_DUCK = loadImage(os.path.join("assets", "sprites", "SwagDuck.png"),
                      scale=True)
COIN_IMG = loadImage(os.path.join("assets", "sprites", "Coin.png"), scale=True)
DAMAGE_BUFF = loadImage(os.path.join("assets", "sprites", "Damage_Buff.png"),
                        scale=True)
#DUCK_IMG2 = loadImage(os.path.join("assets", "sprites", "DuckFrame2.png"),
#scale=True)
ENEMY_LASER = loadImage(os.path.join("assets", "sprites", "Laser_Proj.png"),
                        scale=False)
ENEMY_IMG = loadImage(os.path.join("assets", "sprites", "Enemy_Sprite.png"),
                      scale=True)
ROCKET_IMG = loadImage(os.path.join("assets", "sprites", "Rocket.png"),
                       scale=True)
EXPLOSION_IMG = loadImage(os.path.join("assets", "sprites", "Boom.png"),
                          scale=True)
HEALTH_IMG = loadImage(os.path.join("assets", "sprites", "Health_Symbol.png"),
                       scale=True)
EXIT_IMG = loadImage(os.path.join("assets", "sprites", "Exit_Button.png"),
                     scale=True)
PLAYER_LASER = loadImage(os.path.join("assets", "sprites",
                                      "PLAYER_Laser_Proj.png"),
                         scale=False)
SPEED_IMG = loadImage(os.path.join("assets", "sprites", "Speed_Symbol.png"),
                      scale=True)
BACKGROUND_IMG = loadImage(values.getBG(customizationIO.current_background),
                           False)
HEART_IMG = loadImage(os.path.join("assets", "sprites", "Heart.png"), True)

COIN_IMG_SM = pygame.transform.scale(COIN_IMG, (32, 32))
ROCKET_IMG = pygame.transform.scale(ROCKET_IMG, (32, 20))

#DUCK_IMGS = [DUCK_IMG, DUCK_IMG2]
ENEMY_IMGS = [ENEMY_IMG]
POWERUP_IMGS = {"Health": HEALTH_IMG, "Speed": SPEED_IMG}


class Entity(pygame.sprite.Sprite):

    def __init__(self, x, y, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y

        self.vy = 0
        self.vx = 0

    def levelUpdate(self, speed, level, duck):
        self.rect.x -= speed
        if self.rect.right < 0:
            level.active_sprites.remove(self)


class Rocket(Entity):

    def __init__(self, x, y, image):
        noiseMaker.playSound("rocket")
        super().__init__(x - 30, y + 15, image)

        pos = pygame.mouse.get_pos()
        xTarget = pos[0]
        yTarget = pos[1]

        xOrigin = x
        yOrigin = y

        dx = xTarget - xOrigin
        dy = yOrigin - yTarget
        vBase = 20
        # Getting the angle of the rocket trajectory
        if xOrigin == xTarget:
            # Here, the rocket is going straight up
            theta = 90
        elif dx < 0:
            # Need to make the angle between 90 and 270
            theta = 180 + math.degrees(math.atan(dy / dx))
        else:
            theta = math.degrees(math.atan(dy / dx))
        # Now we have theta, so we can rotate the image
        if theta < 0 and dx > 0:
            theta = 360 + theta
        self.image = pygame.transform.rotate(image, theta)
        self.speed = vBase
        # Set velocity
        dr = math.sqrt(dx**2 + dy**2)

        self.vx = vBase * dx / dr
        self.vy = -vBase * dy / dr

    def update(self, level, duck):

        self.rect.x += self.vx
        self.rect.y += self.vy

        hit_list = pygame.sprite.spritecollide(self, level.enemies, True)
        bit_list = pygame.sprite.spritecollide(self, level.blocks, False)
        if hit_list or bit_list:
            noiseMaker.playSound("boom")
            level.addBoom(self.rect.x, self.rect.y)
            self.kill()
            duck.enemiesKilled += 1
            duck.score += 75
            values.game_score += 75


class Block(Entity):

    def __init__(self, x, y, image):
        super().__init__(x, y, image)

    def levelUpdate(self, speed, level, duck):
        self.rect.x -= speed
        if self.rect.right < 0:
            level.active_sprites.remove(self)

        hit_list = pygame.sprite.spritecollide(self, [duck], False)

        if hit_list:
            duck.rect.right = self.rect.left


class RocketCD(pygame.sprite.Sprite):

    def __init__(self, x, y, cd):
        super().__init__()
        self.rect = pygame.rect.Rect(0, 0, 3, 56)

        self.rect.x = x
        self.rect.y = y

        self.cd = cd
        self.time = 0
        self.yoffset = 0

        self.avail = True

    def update(self, duck):

        self.rect.x = duck.rect.x - 10
        self.rect.y = duck.rect.y + 4 + self.yoffset

        if not self.avail:
            self.time += 1
            if self.time >= self.cd:
                self.avail = True
                self.rect.height = 56
                self.yoffset = 0
            else:
                prop = self.time / self.cd
                self.rect.height = math.floor(56 * prop)
                self.yoffset = 56 - self.rect.height

    def shoot(self):
        self.avail = False
        self.time = 0
        self.yoffset = 0


class Duck(Entity):

    def __init__(self, images):
        super().__init__(GRID_SIZE, HEIGHT / 2 - 20, images[0])
        self.images = images

        self.health = 3
        self.maxHealth = 3
        self.point_decimals = 0

        self.image_index = 0
        self.steps = 0

        self.speed = 10
        self.baseSpeed = 10

        self.damage = 3

        self.dead = False

        self.invincibility = 0

        self.score = 0
        self.coins = 0
        self.enemiesKilled = 0
        values.resetGameScore()
        values.resetCoinsinGame()

        self.activePowerups = []

        self.rockets = []
        self.rocketGroup = pygame.sprite.Group()

        self.rocketCooldown = 30
        self.RocketCD = RocketCD(0, 0, self.rocketCooldown)

    def moveLeft(self):
        self.vx = -self.speed

    def moveRight(self):
        self.vx = self.speed

    def moveDown(self):
        self.vy = self.speed

    def moveUp(self):
        self.vy = -self.speed

    def stop(self, xBool, yBool):
        if xBool:
            self.vx = 0
        if yBool:
            self.vy = 0

    def takeDamage(self, amount):
        if self.invincibility == 0:
            noiseMaker.playSound("oof")
            self.health -= amount
            self.invincibility = 20
        if self.health <= 0:
            self.dead = True

    def shoot(self):
        if self.RocketCD.avail:
            newRocket = Rocket(self.rect.right, self.rect.y, ROCKET_IMG)
            self.rockets.append(newRocket)
            self.rocketGroup.add(newRocket)
            self.RocketCD.shoot()

    def move(self, blocks):

        self.rect.x += self.vx
        hit_list = pygame.sprite.spritecollide(self, blocks, False)

        for block in hit_list:
            '''if self.vx > 0:
                self.rect.right = block.rect.left
                self.vx = 0
            elif self.vx < 0:
                self.rect.left = block.rect.right
                self.vx = 0'''
            if self.rect.centerx < block.rect.centerx:
                self.rect.right = block.rect.left
                self.vx = 0
            elif self.vx < 0:
                self.rect.left = block.rect.right
                self.vx = 0

        self.rect.y += self.vy
        hit_list = pygame.sprite.spritecollide(self, blocks, False)
        
        # Add points for moving forward
        if self.vx > 0:
            self.point_decimals += .1 * self.speed / 10
            if self.point_decimals >= 1:
                self.score += int(self.point_decimals)
                values.game_score += int(self.point_decimals)
                self.point_decimals -= int(self.point_decimals)

        for block in hit_list:
            if self.vy > 0:
                self.rect.bottom = block.rect.top
                self.vy = 0
            elif self.vy < 0:
                self.rect.top = block.rect.bottom
                self.vy = 0

    def processEnemies(self, level):
        hit_list = []
        for e in level.enemies:
            if e.rect.collidepoint(self.rect.center):
                hit_list.append(e)
        for enemy in hit_list:
            level.addBoom(self.rect.centerx, self.rect.centery)
            self.takeDamage(enemy.power)
            enemy.kill()

    def processCoins(self, coins):
        hit_list = pygame.sprite.spritecollide(self, coins, True)
        for coin in hit_list:
            self.score += coin.value
            values.game_score += coin.value
            self.coins += 1
            values.coins_in_game += 1
            noiseMaker.playSound("coin")
            coin.kill()

    def processPowerups(self, powerups):
        hit_list = pygame.sprite.spritecollide(self, powerups, True)
        for p in hit_list:
            p.apply(self)
            powerups.remove(p)
            p.kill()

    def setImage(self):
        pass

    def checkBoundaries(self):
        if self.rect.y < 0:
            self.rect.y = 0
        if self.rect.y >= HEIGHT - self.rect.height:
            self.rect.y = HEIGHT - self.rect.height
        if self.rect.right >= WIDTH:
            self.rect.x = WIDTH - self.rect.width

    def update(self, level):
        self.processEnemies(level)
        self.processCoins(level.coins)
        self.processPowerups(level.powerups)
        self.move(level.blocks)

        self.checkBoundaries()

        self.RocketCD.update(self)

        self.rocketGroup.update(level, self)

        if self.health > self.maxHealth:
            self.health = self.maxHealth
            self.score += 30

        if self.invincibility > 0:
            self.invincibility -= 1


class Coin(Entity):

    def __init__(self, x, y, image, blocks):
        super().__init__(x, y, image)

        self.value = 50

        hit_list = pygame.sprite.spritecollide(self, blocks, False)

        while hit_list:
            hit_list = pygame.sprite.spritecollide(self, blocks, False)
            for block in hit_list:
                self.rect.right = block.rect.left


EFFECTS = ["Health", "Speed"]


class Powerup(Entity):

    def __init__(self, x, y, effect, blocks):
        if effect == 0:
            self.image = HEALTH_IMG
        if effect == 1:
            self.image = SPEED_IMG

        super().__init__(x, y, self.image)

        self.effect = EFFECTS[effect]

        hit_list = pygame.sprite.spritecollide(self, blocks, False)

        for block in hit_list:
            self.rect.right = block.rect.left

    def apply(self, duck):
        if self.effect == "Health":
            noiseMaker.playSound("heal")
            duck.health += 1
        if self.effect == "Speed":
            noiseMaker.playSound("boost")
            if random.randint(0, 9) == 0:
                duck.speed -= 3
            duck.speed += 3
        if self.effect == "Damage":
            duck.attack += 1

        if self.effect == "Slow":
            duck.speed -= 1
        if self.effect == "Hurt":
            duck.takeDamage(1)
        if self.effect == "Bomb":
            duck.takeDamage(3)


class Enemy(Entity):

    def __init__(self, x, y, images):
        super().__init__(x, y, images[0])

        self.speed = 6
        self.power = 1
        self.directiony = 1

    def update(self, duck, blocks):

        if self.rect.y - duck.rect.y > 100:
            self.directiony = -1

        if self.rect.y - duck.rect.y < -100:
            self.directiony = 1

        self.vx = self.speed * -1
        self.vy = self.speed * self.directiony

        self.rect.x += self.vx
        self.rect.y += self.vy

        if self.rect.top < 0:
            self.rect.y = 0
        elif self.rect.bottom > HEIGHT:
            self.rect.y = HEIGHT - self.rect.height

        hit_list = pygame.sprite.spritecollide(self, blocks, False)

        for block in hit_list:
            if self.rect.centerx > block.rect.x + GRID_SIZE and self.rect.left < 10:
                self.rect.left = block.rect.right


#Level made of tiles
#Tile one screen long with own sprites
#Upon passing width X, delete old tile, generate new
#Generate 3 tiles to begin


class Tile():

    def __init__(self, numBlocks, numEnemies, numPowerups, numCoins, offset):
        self.blocks = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.coins = pygame.sprite.Group()
        self.powerups = pygame.sprite.Group()

        self.offset = WIDTH * offset
        self.stackLimit = (HEIGHT // (2 * GRID_SIZE)) - 1

        blocks = []
        blockXs = []
        enemies = []
        powerups = []
        coins = []

        for i in range(numBlocks):
            x = random.randint(150, WIDTH - 60)
            for xBlock in blockXs:
                while abs(x - xBlock) <= BLOCK_IMG.get_width() * 2:
                    x -= BLOCK_IMG.get_width() * 2
            blockXs.append(x)
            y = random.randint(0, 1)
            stack = random.randint(4, self.stackLimit)
            if y:
                y = 0
                bimg = BLOCK_IMG2
                for b in range(stack):
                    blocks.append(Block(x + self.offset, y, bimg))
                    y += bimg.get_height() - 4
            else:
                y = HEIGHT - BLOCK_IMG.get_height()
                bimg = BLOCK_IMG
                for b in range(stack):
                    blocks.append(Block(x + self.offset, y, bimg))
                    y -= bimg.get_height() - 4

            #blocks.append(Block(x, y, bimg))
        self.blocks.add(blocks)
        #Generate enemies
        for i in range(numEnemies):
            x = random.randint(200, WIDTH - 60)  #do for all
            y = random.randint(30, HEIGHT - 60)
            enemies.append(Enemy(x + self.offset, y, ENEMY_IMGS))
        #Generate powerups
        for i in range(numPowerups):
            x = random.randint(100, WIDTH - 60)
            y = random.randint(30, HEIGHT - 60)
            effect = random.randint(0, len(EFFECTS) - 1)
            powerups.append(Powerup(x + self.offset, y, effect, self.blocks))
        #Generate coins
        for i in range(numCoins):
            x = random.randint(100, WIDTH - 60)
            y = random.randint(30, HEIGHT - 60)
            coins.append(Coin(x + self.offset, y, COIN_IMG, self.blocks))

        self.enemies.add(enemies)
        self.powerups.add(powerups)
        self.coins.add(coins)


class Boom(Entity):

    def __init__(self, x, y):
        super().__init__(x, y, EXPLOSION_IMG)
        self.timer = 8

    def levelUpdate(self, speed, level, duck):
        self.rect.x -= speed
        self.timer -= 1
        if self.rect.right < 0 or self.timer <= 0:
            level.active_sprites.remove(self)


class Level():

    def __init__(self, difficulty):
        BACKGROUND_IMG = loadImage(
            values.getBG(customizationIO.current_background), False)

        self.x = 0

        self.difficulty = difficulty

        self.blocks = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.coins = pygame.sprite.Group()
        self.powerups = pygame.sprite.Group()

        self.active_sprites = pygame.sprite.Group()
        self.inactive_sprites = pygame.sprite.Group()

        self.active_layer = pygame.Surface([WIDTH, HEIGHT], pygame.SRCALPHA,
                                           32)
        self.inactive_layer = pygame.Surface([WIDTH, HEIGHT], pygame.SRCALPHA,
                                             32)
        self.background_layer = pygame.Surface([WIDTH, HEIGHT],
                                               pygame.SRCALPHA, 32)

        # fit background to screen
        for x in range(0, WIDTH, BACKGROUND_IMG.get_width()):
            for y in range(0, HEIGHT, BACKGROUND_IMG.get_height()):
                self.background_layer.blit(BACKGROUND_IMG, (x, y))

        self.reset()

    def addBoom(self, x, y):
        newBoom = Boom(x, y)
        self.active_sprites.add(newBoom)

    def update(self, duck):
        pass

    def reset(self):
        self.tiles = []

        self.generateTile(0)
        self.generateTile(1)
        self.generateTile(2)

    def generateTile(self, offset):
        numEnemies = random.randint(1, self.difficulty)
        numCoins = random.randint(1, 4)
        numPowerups = random.randint(0, 2)
        if numPowerups:
            numPowerups = random.randint(0, 2)
        numBlocks = random.randint(3, 3 + self.difficulty)

        newTile = Tile(numBlocks, numEnemies, numPowerups, numCoins, offset)

        self.addTile(newTile)

        self.tiles.append(newTile)

        if len(self.tiles) > 3:
            self.deleteTile()

    def addTile(self, t):
        for b in t.blocks:
            self.blocks.add(b)
        for e in t.enemies:
            self.enemies.add(e)
        for c in t.coins:
            self.coins.add(c)
        for p in t.powerups:
            self.powerups.add(p)

        #self.inactive_sprites.add(t.blocks)
        self.active_sprites.add(t.enemies, t.coins, t.powerups, t.blocks)

    def deleteTile(self):
        t = self.tiles[0]
        for b in t.blocks:
            self.blocks.remove(b)
            self.inactive_sprites.remove(b)
        for e in t.enemies:
            values.enemysKilled += 1
            self.enemies.remove(e)
            self.active_sprites.remove(b)
        for c in t.coins:
            self.coins.remove(c)
            self.active_sprites.remove(c)
        for p in t.powerups:
            self.powerups.remove(p)
            self.active_sprites.remove(p)

        self.tiles = self.tiles[1:]


difficulty = 1


class Game():

    SPLASH = 0
    START = 1
    PLAYING = 2
    PAUSED = 3
    GAME_OVER = 4
    SETTINGS = 5
    CONTROLS = 6

    def __init__(self):

        #Distance, Time, Points, Currency, Enemies, Spaceships, Meteroids
        #self.totalDistanceTraveled, self.?, self.duck.score, self.duck.coins, self.duck.enemiesKilled, ? , ?
        #Bradley

        self.elapsedTime = 0
        self.difficulty = 1
        self.difficultyModifier = settingIO.DifficultyLevel.value
        values.startTime = time.time()
        values.enemyKilled = 0

        self.gameSpeed = (self.difficulty + 2) * 2

        self.distanceTraveled = 0
        self.totalDistanceTraveled = 0

        self.window = pygame.display.get_surface()
        self.WIDTH = self.window.get_width()
        self.HEIGHT = self.window.get_height()

        self.clock = pygame.time.Clock()

        self.done = False

        self.reset()

    def reset(self):
        DUCK_IMG = loadImage(values.current_skin, scale=True)
        BACKGROUND_IMG = loadImage(
            values.getBG(customizationIO.current_background), False)
        # print(values.getBG(customizationIO.current_background)) prints the correct image location???
        self.elapsedTime = 0
        self.duck = Duck([DUCK_IMG])
        self.level = Level(self.difficulty)

        self.distanceTraveled = 0
        self.totalDistanceTraveled = 0
        self.gameSpeed = (self.difficulty + 2) * 2
        values.startTime = time.time()
        values.enemyKilled = 0
        self.stage = Game.SPLASH

    def display_splash(self):
        FONT_LG.render("DUCKS IN SPACE!", 1, WHITE)
        FONT_SM.render("Press any key to start.", 1, WHITE)

        #Skip actually

    def display_message(self, text, text2):
        line1 = FONT.render(text, 1, WHITE)
        line2 = FONT_SM.render(text2, 1, WHITE)

        x1 = WIDTH / 2 - line1.get_width() / 2
        y1 = HEIGHT / 3 - line1.get_height() / 2
        x2 = WIDTH / 2 - line2.get_width() / 2
        y2 = y1 + line1.get_height() + 16

        SCREEN.blit(line1, (x1, y1))
        SCREEN.blit(line2, (x2, y2))

    def display_message2(self, text, text2, text3):
        line1 = FONT.render(text, 1, WHITE)
        line2 = FONT_SM.render(text2, 1, WHITE)
        line3 = FONT_SM.render(text3, 1, WHITE)

        x1 = WIDTH / 2 - line1.get_width() / 2
        y1 = HEIGHT / 3 - line1.get_height() / 2
        x2 = WIDTH / 2 - line2.get_width() / 2
        y2 = y1 + line1.get_height() + 16
        x3 = WIDTH / 2 - line3.get_width() / 2
        y3 = y2 + line1.get_height() + 16

        SCREEN.blit(line1, (x1, y1))
        SCREEN.blit(line2, (x2, y2))
        SCREEN.blit(line3, (x3, y3))

    def display_message3(self, text, text2, text3, text4):
        line1 = FONT.render(text, 1, WHITE)
        line2 = FONT_SM.render(text2, 1, WHITE)
        line3 = FONT_SM.render(text3, 1, WHITE)
        line4 = FONT_SM.render(text4, 1, WHITE)

        x1 = WIDTH / 2 - line1.get_width() / 2
        y1 = HEIGHT / 3 - line1.get_height() / 2
        x2 = WIDTH / 2 - line2.get_width() / 2
        y2 = y1 + line1.get_height() + 16
        x3 = WIDTH / 2 - line3.get_width() / 2
        y3 = y2 + line1.get_height() + 16
        x4 = WIDTH / 2 - line4.get_width() / 2
        y4 = y3 + line1.get_height() + 16

        SCREEN.blit(line1, (x1, y1))
        SCREEN.blit(line2, (x2, y2))
        SCREEN.blit(line3, (x3, y3))
        SCREEN.blit(line4, (x4, y4))

    def display_stats(self):
        scoreLine = FONT_SM.render("Score: " + str(self.duck.score), 1, WHITE)
        coinLine = FONT_SM.render(" x" + str(self.duck.coins), 1, WHITE)

        heartX = 10
        for h in range(self.duck.health):
            SCREEN.blit(HEART_IMG, (heartX, 10))
            heartX += HEART_IMG.get_width()

        x1 = 15 + COIN_IMG_SM.get_width()
        y1 = 15 + HEART_IMG.get_height()

        y2 = y1 + 5 + COIN_IMG_SM.get_height()

        SCREEN.blit(COIN_IMG_SM, (10, y1))
        SCREEN.blit(coinLine, (x1, y1))
        SCREEN.blit(scoreLine, (20, y2))

    def process_events(self):
        global sound_on
        global paused

        pressed = pygame.key.get_pressed()
        if pressed[UP]:
            self.duck.moveUp()
        elif pressed[DOWN]:
            self.duck.moveDown()
        else:
            self.duck.stop(False, True)
        if pressed[LEFT]:
            self.duck.moveLeft()
        elif pressed[RIGHT]:
            self.duck.moveRight()
        else:
            self.duck.stop(True, False)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  #Bradley
                self.end_game_process()
                values.distanceTraveled = self.totalDistanceTraveled

                values.newHighScore = False
                menuS.menu.QUIT
                main.quit_game()

            if event.type == pygame.KEYDOWN and self.stage == Game.PLAYING:

                if event.key == pygame.K_ESCAPE:
                    self.stage = Game.PAUSED
            elif event.type == pygame.MOUSEBUTTONUP and self.stage == Game.PLAYING:
                self.duck.shoot()
            elif self.stage == Game.PAUSED:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    self.stage = Game.PLAYING
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                    self.reset()
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_s:
                    #settings pop up and able to change
                    self.stage = Game.SETTINGS

                elif event.type == pygame.KEYDOWN and event.key == pygame.K_c:
                    self.stage = Game.CONTROLS
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                    self.end_game_process()
                    values.distanceTraveled = self.totalDistanceTraveled
                    #change to quit to home screen instead of highScore / GameOver Screen
                    menuS.set_game_menu(menuS.menu.HOME)
                    """
                    if (values.newHighScore):
                        menuS.set_game_menu(menuS.menu.HIGH_SCORE)
                    else:
                        menuS.set_game_menu(menuS.menu.GAMEOVER)
                    """

                    main.main()
            elif self.stage == Game.SPLASH:
                self.stage = Game.START
            elif self.stage == Game.START:
                if event.type == pygame.KEYDOWN:
                    self.stage = Game.PLAYING
            elif self.stage == Game.SETTINGS:
                #events for in-game settings screen
                if event.type == pygame.KEYDOWN and event.key == pygame.K_b:
                    self.stage = Game.PAUSED
            elif self.stage == Game.CONTROLS:
                #events for in-game controls screen
                if event.type == pygame.KEYDOWN:
                    self.stage = Game.PAUSED

            elif self.stage == Game.GAME_OVER:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        self.end_game_process()
                        values.distanceTraveled = self.totalDistanceTraveled
                        if (values.newHighScore):
                            menuS.set_game_menu(menuS.menu.HIGH_SCORE)
                        else:
                            menuS.set_game_menu(menuS.menu.GAMEOVER)

                        main.main()

                    elif event.key == pygame.K_r:
                        self.reset()

    def update(self):

        self.gameSpeed = min(20, (self.difficulty + 2) * 2)

        self.elapsedTime += 1 / FPS
        if self.stage == Game.PLAYING:
            self.duck.update(self.level)
            for e in self.level.enemies:
                e.update(self.duck, self.level.blocks)

            #SIDESCROLL
            for sprite in self.level.active_sprites:
                sprite.levelUpdate(self.gameSpeed, self.level, self.duck)
                #sprite.rect.x -= self.gameSpeed
                #if sprite.rect.right < 0:
                #    self.level.active_sprites.remove(sprite)

            self.duck.rect.x -= self.gameSpeed / 2

            self.distanceTraveled += self.gameSpeed
            self.totalDistanceTraveled += self.gameSpeed

        if self.duck.health <= 0 or self.duck.rect.right < 0:
            self.stage = Game.GAME_OVER

        if self.distanceTraveled > WIDTH:
            self.level.deleteTile()
            self.level.generateTile(2)
            self.level.difficulty += self.difficultyModifier
            self.difficulty += self.difficultyModifier
            self.duck.speed += 0.5
            self.distanceTraveled -= WIDTH

        self.level.update(self.duck)

    def draw(self):
        self.level.active_layer.fill(TRANSPARENT)
        self.level.active_sprites.draw(self.level.active_layer)
        self.level.inactive_sprites.draw(self.level.inactive_layer)
        self.duck.rocketGroup.draw(self.level.active_layer)

        if self.duck.invincibility % 3 < 2:
            self.level.active_layer.blit(self.duck.image,
                                         [self.duck.rect.x, self.duck.rect.y])
        #Draw cd
        pygame.draw.rect(self.level.active_layer, (255, 0, 0),
                         self.duck.RocketCD.rect)

        SCREEN.blit(self.level.background_layer, [0, 0])
        SCREEN.blit(self.level.inactive_layer, [0, 0])
        SCREEN.blit(self.level.active_layer, [0, 0])

        self.display_stats()

        if self.stage == Game.SPLASH:
            self.display_splash()
        elif self.stage == Game.START:
            self.display_message2("DUCKS IN SPACE!",
                                  "Press 'ESC' at any time to pause game",
                                  "Press any key to start!")
        elif self.stage == Game.PAUSED:
            self.display_message3(
                "PAUSED",
                "'ESC' to resume. 'R' to restart. 'Q' to quit to menu.",
                "'S' to quit to Settings screen.", "'C' to see Controls.")
        elif self.stage == Game.GAME_OVER:
            self.end_game_process()
            values.distanceTraveled = self.totalDistanceTraveled

            if values.newHighScore:
                menuS.set_game_menu(menuS.menu.HIGH_SCORE)
            else:
                menuS.set_game_menu(menuS.menu.GAMEOVER)
            main.main()

        elif self.stage == Game.SETTINGS:
            #display in-game settings Screen
            menuS.set_game_menu(menuS.menu.SETTING)
            main.main()
        elif self.stage == Game.CONTROLS:
            if settingIO.keys == "wasd":
                self.display_message2(
                    "CONTROLS",
                    "WASD to move. Left Click to shoot. ESC to pause.",
                    "Press any key to continue.")
            elif settingIO.keys == "arrows":
                self.display_message2(
                    "CONTROLS",
                    "Arrows to move. Space to shoot. ESC to pause.",
                    "Press any key to continue.")

        pygame.display.update()
        pygame.display.flip()

    def loop(self):
        while not self.done:
            self.process_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)
        values.updateCoins()

    def end_game_process(self):
        #find game time using values.start_time
        game_time = time.time() - values.startTime
        #convert to MM:SS
        values.gameTime = time.strftime('%M:%S', time.gmtime(game_time))

        # Game Format is [Distance, Time, Points, Currency, Enemies, Spaceships, Meteroids]
        game = [
            self.totalDistanceTraveled,
            math.floor(self.elapsedTime), self.duck.score, self.duck.coins,
            self.duck.enemiesKilled
        ]
        statsIO.postgame_update(game)
        statsIO.create_game_log(game)
        #make YYYY-MM-DD
        day = str(
            str(datetime.datetime.now().year) + "-" +
            str(datetime.datetime.now().month) + "-" +
            str(datetime.datetime.now().day))

        score = [settingIO.Player_Name, values.game_score, day]
        highScoreIO.check_for_high_score(score)


def gameScreen(noises):
    global UP, DOWN, LEFT, RIGHT
    global noiseMaker
    noiseMaker = noises
    game = Game()
    game.reset()
    game.loop()
    if settingIO.keys == "wasd":
        UP = pygame.K_w
        DOWN = pygame.K_s
        LEFT = pygame.K_a
        RIGHT = pygame.K_d
    elif settingIO.keys == "arrows":
        UP = pygame.K_UP
        DOWN = pygame.K_DOWN
        LEFT = pygame.K_LEFT
        RIGHT = pygame.K_RIGHT
    #pygame.quit()
    #sys.exit()
