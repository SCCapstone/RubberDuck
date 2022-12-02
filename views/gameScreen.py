import pygame
import random
import os
import menuStructure as menuS
import main as main
#from assets import values
#import menuStructure as menuS

GRID_SIZE = 64
FPS = 30

pygame.init()
#CONTROLS
UP = pygame.K_w
DOWN = pygame.K_s
LEFT = pygame.K_a
RIGHT = pygame.K_d

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
DUCK_IMG = loadImage(os.path.join("assets", "sprites", "BaseDuck.png"),
                     scale=True)
SWAG_DUCK = loadImage(os.path.join("assets", "sprites", "SwagDuck.png"),
                      scale=True)
COIN_IMG = loadImage(os.path.join("assets", "sprites", "Coin.png"), scale=True)
DAMAGE_BUFF = loadImage(os.path.join("assets", "sprites", "Damage_Buff.png"),
                        scale=True)
DUCK_IMG2 = loadImage(os.path.join("assets", "sprites", "DuckFrame2.png"),
                      scale=True)
ENEMY_LASER = loadImage(os.path.join("assets", "sprites", "Laser_Proj.png"),
                        scale=False)
ENEMY_IMG = loadImage(os.path.join("assets", "sprites", "Enemy_Sprite.png"),
                      scale=True)
ROCKET_IMG = loadImage(os.path.join("assets", "sprites", "Rocket.png"),
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
BACKGROUND_IMG = loadImage(
    os.path.join("assets", "backgrounds", "base_bg.png"), False)
HEART_IMG = loadImage(os.path.join("assets", "sprites", "Heart.png"), True)

COIN_IMG_SM = pygame.transform.scale(COIN_IMG, (32, 32))
ROCKET_IMG = pygame.transform.scale(ROCKET_IMG, (32, 20))

DUCK_IMGS = [DUCK_IMG, DUCK_IMG2]
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

    def levelUpdate(self, speed):
        self.rect.x -= speed


class Rocket(Entity):

    def __init__(self, x, y, image):
        super().__init__(x, y, image)

        pos = pygame.mouse.get_pos()
        xTarget = pos[0]
        yTarget = pos[1]

        xOrigin = x
        yOrigin = y

        rise = yTarget - yOrigin
        run = xTarget - xOrigin

        self.speed = 20

        if run > 0:
            self.vx = 10
        else:
            self.vx = -10

        if run == 0:
            slope = 1000
            self.vx = 0
        else:
            slope = rise / run

        self.vy = slope * self.vx

        if rise > 0 and self.vy < 0:
            self.vy *= -1
        elif rise < 0 and self.vy > 0:
            self.vy *= -1
        '''if self.vy > 10:
            self.vy = 10
        elif self.vy < -10:
            self.vy = -10'''

    def update(self, enemies):

        self.rect.x += self.vx
        self.rect.y += self.vy

        hit_list = pygame.sprite.spritecollide(self, enemies, True)
        if hit_list:

            self.kill()


class Block(Entity):

    def __init__(self, x, y, image):
        super().__init__(x, y, image)


class Duck(Entity):

    def __init__(self, images):
        super().__init__(0, HEIGHT / 2 - 20, images[0])
        self.images = images

        self.health = 3
        self.maxHealth = 3

        self.image_index = 0
        self.steps = 0

        self.speed = 10
        self.baseSpeed = 10

        self.damage = 3

        self.dead = False

        self.invincibility = 0

        self.score = 0
        self.coins = 0

        self.activePowerups = []

        self.rockets = []
        self.rocketGroup = pygame.sprite.Group()
        self.rocketCD = 0
        self.rocketCooldown = 40

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
            self.health -= amount
            self.invincibility = 20
        if self.health <= 0:
            self.dead = True

    def shoot(self):
        if not self.rocketCD:
            newRocket = Rocket(self.rect.right, self.rect.y, ROCKET_IMG)
            self.rockets.append(newRocket)
            self.rocketGroup.add(newRocket)
            self.rocketCD = self.rocketCooldown

    def move(self, blocks):

        self.rect.x += self.vx
        hit_list = pygame.sprite.spritecollide(self, blocks, False)

        for block in hit_list:
            if self.vx > 0:
                self.rect.right = block.rect.left
                self.vx = 0
            elif self.vx < 0:
                self.rect.left = block.rect.right
                self.vx = 0

        self.rect.y += self.vy
        hit_list = pygame.sprite.spritecollide(self, blocks, False)

        for block in hit_list:
            if self.vy > 0:
                self.rect.bottom = block.rect.top
                self.vy = 0
            elif self.vy < 0:
                self.rect.top = block.rect.bottom
                self.vy = 0

    def processEnemies(self, enemies):
        hit_list = pygame.sprite.spritecollide(self, enemies, True)
        for enemy in hit_list:
            self.takeDamage(enemy.power)

    def processCoins(self, coins):
        hit_list = pygame.sprite.spritecollide(self, coins, True)
        for coin in hit_list:
            self.score += coin.value
            self.coins += 1
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

    def update(self, level):
        self.processEnemies(level.enemies)
        self.processCoins(level.coins)
        self.processPowerups(level.powerups)
        self.move(level.blocks)

        self.checkBoundaries()

        if self.rocketCD > 0:
            self.rocketCD -= 1

        self.rocketGroup.update(level.enemies)

        if self.health > self.maxHealth:
            self.health = self.maxHealth

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
            duck.health += 1
        if self.effect == "Speed":
            duck.speed += 2
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

    def update(self, duck):

        if self.rect.y - duck.rect.y > 10:
            directiony = -1
        elif self.rect.y - duck.rect.y < -10:
            directiony = 1
        else:
            directiony = 0

        self.vx = self.speed * -1
        self.vy = self.speed * directiony

        self.rect.x += self.vx
        self.rect.y += self.vy


#Level made of tiles
#Tile one screen long with own sprites
#Upon passing width X, delete old tile, generate new
#Generate 3 tiles to begin


class Tile():

    def __init__(self, numBlocks, numEnemies, numPowerups, numCoins):
        self.blocks = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.coins = pygame.sprite.Group()
        self.powerups = pygame.sprite.Group()

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
            stack = random.randint(3, 6)
            if y:
                y = 0
                bimg = BLOCK_IMG2
                for b in range(stack):
                    blocks.append(Block(x, y, bimg))
                    y += bimg.get_height() - 4
            else:
                y = HEIGHT - BLOCK_IMG.get_height()
                bimg = BLOCK_IMG
                for b in range(stack):
                    blocks.append(Block(x, y, bimg))
                    y -= bimg.get_height() - 4

            blocks.append(Block(x, y, bimg))
        self.blocks.add(blocks)
        for i in range(3):
            x = random.randint(200, WIDTH - 60)  #do for all
            y = random.randint(30, HEIGHT - 60)
            enemies.append(Enemy(x, y, ENEMY_IMGS))
        for i in range(numPowerups):
            x = random.randint(100, WIDTH - 60)
            y = random.randint(30, HEIGHT - 60)
            effect = random.randint(0, len(EFFECTS) - 1)
            powerups.append(Powerup(x, y, effect, self.blocks))
        for i in range(numCoins):
            x = random.randint(100, WIDTH - 60)
            y = random.randint(30, HEIGHT - 60)
            coins.append(Coin(x, y, COIN_IMG, self.blocks))

        self.enemies.add(enemies)
        self.powerups.add(powerups)
        self.coins.add(coins)


class Level():

    def __init__(self, difficulty):
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

    def update(self, duck):
        pass

    def reset(self):
        self.tiles = []
        while len(self.tiles) < 1:
            self.generateTile()

    def generateTile(self):
        numEnemies = random.randint(1, self.difficulty)
        numCoins = random.randint(1, 4)
        numPowerups = random.randint(0, 2)
        if numPowerups:
            numPowerups = random.randint(0, 2)
        numBlocks = random.randint(3, 3 + self.difficulty)

        newTile = Tile(numBlocks, numEnemies, numPowerups, numCoins)

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

        self.inactive_sprites.add(t.blocks)
        self.active_sprites.add(t.enemies, t.coins, t.powerups)

    def deleteTile(self):
        t = self.tiles[0]
        for b in t.blocks:
            self.blocks.remove(b)
            self.inactive_sprites.remove(b)
        for e in t.enemies:
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

    def __init__(self):

        self.difficulty = 1

        self.window = pygame.display.get_surface()
        self.WIDTH = self.window.get_width()
        self.HEIGHT = self.window.get_height()

        self.clock = pygame.time.Clock()

        self.done = False

        self.reset()

    def reset(self):
        self.duck = Duck(DUCK_IMGS)
        self.level = Level(self.difficulty)

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
            if event.type == pygame.QUIT:
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
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                    menuS.set_game_menu(menuS.menu.HOME)
                    main.main()
            elif self.stage == Game.SPLASH:
                self.stage = Game.START
            elif self.stage == Game.START:
                if event.type == pygame.KEYDOWN:
                    self.stage = Game.PLAYING
            elif self.stage == Game.GAME_OVER:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        menuS.set_game_menu(menuS.menu.HOME)
                        main.main()

                    elif event.key == pygame.K_r:
                        self.reset()

    def update(self):
        if self.stage == Game.PLAYING:
            self.duck.update(self.level)
            for e in self.level.enemies:
                e.update(self.duck)

        if self.duck.health <= 0:
            self.stage = Game.GAME_OVER

        self.level.update(self.duck)

    def draw(self):
        self.level.active_layer.fill(TRANSPARENT)
        self.level.active_sprites.draw(self.level.active_layer)
        self.level.inactive_sprites.draw(self.level.inactive_layer)
        self.duck.rocketGroup.draw(self.level.active_layer)

        if self.duck.invincibility % 3 < 2:
            self.level.active_layer.blit(self.duck.image,
                                         [self.duck.rect.x, self.duck.rect.y])

        SCREEN.blit(self.level.background_layer, [0, 0])
        SCREEN.blit(self.level.inactive_layer, [0, 0])
        SCREEN.blit(self.level.active_layer, [0, 0])

        self.display_stats()

        if self.stage == Game.SPLASH:
            self.display_splash()
        elif self.stage == Game.START:
            self.display_message("DUCKS IN SPACE!", "Press any key to start!")
        elif self.stage == Game.PAUSED:
            self.display_message(
                "PAUSED",
                "'ESC' to resume. 'R' to restart. 'Q' to quit to menu.")
        elif self.stage == Game.GAME_OVER:
            menuS.set_game_menu(menuS.menu.GAMEOVER)
            main.main()

        pygame.display.update()
        pygame.display.flip()

    def loop(self):
        while not self.done:
            self.process_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)


def gameScreen():
    game = Game()
    game.reset()
    game.loop()
    #pygame.quit()
    #sys.exit()
