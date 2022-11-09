import pygame
GRID_SIZE = 64

def loadImage(filePath):
    img = pygame.image.load(filePath)
    img = pygame.transform.scale(img,(GRID_SIZE, GRID_SIZE))

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
    def __init__(self, x, y, image, effect):
        super().__init__(x,y,image)

        self.effect = effect

    def apply(self, duck):
        if effect == "Health":
            duck.health += 1
        if effect == "Speed":
            duck.speed += 2
        if effect == "Damage":
            duck.attack += 1

        if effect == "Slow":
            duck.speed -= 1
        if effect == "Hurt":
            duck.takeDamage(1)
        if effect == "Bomb":
            duck.takeDamage(3)
    

class Enemy(Entity):
    def __init__(self,x,y,speed,images):
        super().__init__(x,y,images[0])

        self.vy = speed

    def update(self, duck):
        pass




def gameScreen():
    #Do everything here???
