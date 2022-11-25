import pygame
import random
from assets import values
import menuStructure as menuS

GRID_SIZE = 64
FPS = 30


def loadImage(filePath, scale):
    img = pygame.image.load(filePath)
    if scale:
        img = pygame.transform.scale(img,(GRID_SIZE, GRID_SIZE))
    return img



#Image loading
BLOCK_IMG = loadImage(os.path.join("assets","sprites","Wall_block.png"),scale=True)
DUCK_IMG = loadImage(os.path.join("assets","sprites","BaseDuck.png"),scale=True)
SWAG_DUCK = loadImage(os.path.join("assets","sprites","SwagDuck.png"),scale=True)
COIN_IMG = loadImage(os.path.join("assets","sprites","Coin.png"),scale=True)
DAMAGE_BUFF = loadImage(os.path.join("assets","sprites","Damage_Buff.png"),scale=True)
DUCK_IMG2 = loadImage(os.path.join("assets","sprites","DuckFrame2.png"),scale=True)
ENEMY_LASER = loadImage(os.path.join("assets","sprites","Laser_Proj.png"),scale=False)
ENEMY_IMG = loadImage(os.path.join("assets","sprites","Enemy_Sprite.png"),scale=True)
ROCKET_IMG = loadImage(os.path.join("assets","sprites","Rocket.png"),scale=True)
HEALTH_IMG = loadImage(os.path.join("assets","sprites","Health_Symbol.png"),scale=True)
EXIT_IMG = loadImage(os.path.join("assets","sprites","Exit_Button.png"),scale=True)
PLAYER_LASER = loadImage(os.path.join("assets","sprites","PLAYER_Laser_Proj.png"),scale=False)
SPEED_IMG = loadImage(os.path.join("assets","sprites","Speed_Symbol.png"),scale=True)


DUCK_IMGS = [DUCK_IMG, DUCK_IMG2]


class Entity(pygame.sprite.Sprite):
    def __init__(self,x,y,image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y

        self.vy = 0
        self.vx = 0

    def levelUpdate(self, speed):
        self.rect.x -= speed

class Block(Entity):

    def __init__(self,x,y,image):
        super().__init__(x,y,image)

class Duck(Entity):

    def __init__(self, images):
        super.__init__(0,0,images[0])
        self.images = images

        self.health = 3
        self.maxHealth = 3

        self.image_index = 0
        self.steps = 0

        self.speed = 5
        self.baseSpeed = 5

        self.damage = 3

        self.dead = False

        self.invincibility = 0

        self.score = 0
        self.coins = 0

        self.activePowerups = []


    def moveLeft(self):
        self.vx = -self.speed
    def moveRight(self):
        self.vx = self.speed
    def moveDown(self):
        self.vy = self.speed
    def moveUp(self):
        self.vy = -self.speed
    def stop(self):
        self.vx = 0
        self.vy = 0

    def takeDamage(self, amount):
        if self.invincibility == 0:
            self.health -= self.amount
            self.invincibility = 20
        if self.health <= 0:
            self.dead = True

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

    def processPowerups(self, powerups):
        hit_list = pygame.sprite.spritecollide(self, powerups, True)
        for p in powerups:
            p.apply(self)
        

    def setImage(self):
        pass

    def checkBoundaries(self):
        pass

    def update(self, level):
        self.processEnemies(level.enemies)
        self.move(level.blocks)
        self.checkBoundaries(self)

        if self.health > self.maxHealth:
            self.health = self.maxHealth

        if self.invincibility > 0:
            self.invincibility -= 1

class Coin(Entity):
    def __init__(self, x, y, image):
        super().__init__(x,y,image)

        self.value = 50

class PowerUp(Entity):
    EFFECTS = ["Health", "Speed"]
    def __init__(self, x, y, effect):
        if effect == 0:
            self.image = HEALTH_IMG
        if effect == 1:
            self.image = SPEED_IMG
        super().__init__(x,y,self.image)

        self.effect = EFFECTS[effect]

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
    def __init__(self,x,y,speed,images):
        super().__init__(x,y,images[0])

        self.vy = speed

    def update(self, duck):
        pass



#Level made of tiles
#Tile one screen long with own sprites
#Upon passing width X, delete old tile, generate new
#Generate 3 tiles to begin

class Tile():
    EFFECTS = ["Health", "Speed"]
    def __init__(self, numBlocks, numEnemies, numPowerups, numCoins):
        self.blocks = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.coins = pygame.sprite.Group()
        self.powerups = pygame.sprite.Group()

        self.active_sprites = pygame.sprite.Group()
        self.inactive_sprites = pygame.sprite.Group()

        blocks = []
        enemies = []
        powerups = []
        coins = []
        
        for i in range(numBlocks):
            x = random.randint(20,screen.get_width()-60)
            y = random.randint(0,1)
            if y:
                y = 0
            else:
                y = screen.get_height() - 50 #block height instead of 50
            blocks.append(Block(x,y,BLOCK_IMG))
        for i in range(numEnemies):
            x = random.randint(20,screen.get_width()-60)
            y = random.randint(30,screen.get_height()-60)
            enemies.append(Enemy(x,y,ENEMY_IMG))
        for i in range(numPowerups):
            x = random.randint(20,screen.get_width()-60)
            y = random.randint(30,screen.get_height()-60)
            effect = random.randint(0,len(EFFECTS))
            powerups.append(Powerup(x,y,effect))
        for i in range(numCoins):
            x = random.randint(20,screen.get_width()-60)
            y = random.randint(30,screen.get_height()-60)
            coins.append(Coin(x,y,COIN_IMG))

        self.blocks.add(blocks)
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

        #Remove is self.blocks.remove(block)

        self.height = screen.get_height()

        self.tiles = []
        while len(self.tiles) < 3:
            self.generateTile()
        
    def generateTile(self):
        numEnemies = random.randint(1,self.difficulty)
        numCoins = random.randint(1,2)
        numPowerups = random.randint(0,1)
        if numPowerups:
            numPowerups = random.randint(0,1)
        numBlocks = random.randint(3,3+self.difficulty)

        newTile = Tile(numBlocks, numEnemies, numPowerups, numCoins)

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

        self.inactive_sprites.add(blocks, coins, powerups)
        self.active_sprites.add(enemies)

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
            self.inactive_sprites.remove(c)
        for p in t.powerups:
            self.powerups.remove(p)
            self.inactive_sprites.remove(p)
        
        self.tiles = self.tiles[1:]

difficulty = 1
def gameScreen():
    ##Set up
    screen = pygame.display.get_surface()
    #Background
    background = pygame.image.load(os.path.join("assets","backgrounds","tertiary.jpg"))
    background = pygame.transform.scale(background,(screen.get_width(),screen.get_height()))
    screen.blit(background, (0,0))

    #Font
    font = pygame.font.Font(os.path.join("assets","fonts","Ethocentric.ttf"),int(values.screenX * 0.019))
    
    #Level
    level = Level(difficulty)

    #Duck
    p = Duck(DUCK_IMGS)

    while True:
        #Game loop
        pass
