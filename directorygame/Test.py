import pygame, sys
from pygame.locals import *
import os
import glob
import random

weapon_list = pygame.sprite.Group()
monster_list = pygame.sprite.Group()
all_list = pygame.sprite.Group()
block_list = pygame.sprite.Group()

BLACK = (  0,   0,   0)
RED   = (255,   0,   0)


list = []
list2 = []
list3 = []
list4 = []

directory = '/Users/Public/Documents/Test'

SpriteSheetBase = r'C:\Users\Rigney\Pictures\Pack 01 (Pixel Art)\hyptosis_sprites-and-tiles-for-you.png'
SpriteSheet3 = r'C:\Users\Rigney\Pictures\Pack 01 (Pixel Art)\hyptosis_tile-art-batch-3.png'

def getTexture(SpriteSheetName, location_x, location_y, width, height):
    #bruh this is like my favorite function ever. texturing is so easy now. I'm proud
    sheet2 = pygame.image.load(SpriteSheetName)
    textureObject = sheet2.subsurface(pygame.Rect(location_x, location_y, width, height))
    return textureObject
def getWeaponX(weaponNameX):
    return {
        'Spear': 143,
        'Dagger': 113
        }[weaponNameX]
def getWeaponY(weaponNameY):
    return {
        'Spear': 123,
        'Dagger': 123
        }[weaponNameY]
def getMonsterX(monsterX):
    return {
        'Bug': 390,
        'Rat': 390 + 32,
        'Bat': 390 + 64,
        'Lizard': 390 + 96
        }[monsterX]
def getMonsterY(monsterY):
    return {
        'Bug': 786,
        'Rat': 786,
        'Bat': 786,
        'Lizard': 786
        }[monsterY]        

class Weapon(pygame.sprite.Sprite):
    def __init__(self, weaponName):
        super().__init__()
        self.image = getTexture(SpriteSheetBase, getWeaponX(weaponName), getWeaponY(weaponName), 30, 30)
        self.rect = pygame.Rect(300, 300, 30, 30)

class Monster(pygame.sprite.Sprite):
    def __init__(self, monsterName, loc_x, loc_y):
        super().__init__()
        self.image = getTexture(SpriteSheetBase, getMonsterX(monsterName), getMonsterY(monsterName), 32, 32)
        self.rect = pygame.Rect(loc_x, loc_y, 32, 32)
    def update(self):
        r = random.randint(1,4)
        l = 0
        k = random.randint(1,10)
        
        if k == 10:
            if r == 1:
                while l < 10:
                    self.rect.y += 1
                    self.rect.x += 1
                    l += 1
                l = 0
            elif r == 2:
                while l < 10:
                    self.rect.y += 1
                    self.rect.x -= 1
                    l += 1
                l = 0
            elif r == 3:
                while l < 10:
                    self.rect.y -= 1
                    self.rect.x += 1
                    l += 1
                l = 0
            elif r == 4:
                while l < 10:
                    self.rect.y -= 1
                    self.rect.x -= 1
                    l += 1
                l = 0
        else:
            l = 0
        
class BlockLong(pygame.sprite.Sprite):
    def __init__(self, color, loc_x, loc_y):
        super().__init__()
        self.image = pygame.Surface([64, 32])
        self.image.fill(RED)
        self.rect = pygame.Rect(loc_x, loc_y, 64, 32)
class BlockWide(pygame.sprite.Sprite):
    def __init__(self, color, loc_x, loc_y):
        super().__init__()
        self.image = pygame.Surface([32, 64])
        self.image.fill(color)
        self.rect = pygame.Rect(loc_x, loc_y, 32, 64)
class Bat(Monster):
    def __init__(self, monsterName, loc_x, loc_y):
        super().__init__(monsterName, loc_x, loc_y)
SCREEN_X=512
SCREEN_Y=512
#Screen size

SPRT_RECT_X=0  
SPRT_RECT_Y=0
#This is where the sprite is found on the sheet




#make these into classes, so you can create new objects with the individual textures





def addBlocksTop():
    i = 0
    x = 0
    y = 0
    for i in range(8):
        block1 = BlockLong(RED, x, y)
        block_list.add(block1)
        all_list.add(block1)
        list.append(block1)
        print(list)
        x+=64
def addBlocksBottom():
    i = 0
    x = 0
    y = 512 - 32
    for i in range(8):
        block1 = BlockLong(RED, x, y)
        block_list.add(block1)
        all_list.add(block1)
        list2.append(block1)
        x+=64
def addBlocksLeft():
    i = 0
    x = 0
    y = 0
    for i in range(8):
        block1 = BlockWide(RED, x, y)
        block_list.add(block1)
        all_list.add(block1)
        list3.append(block1)
        y+=64
def addBlocksRight():
    i = 0
    x = 512 - 32
    y = 0
    for i in range(8):
        block1 = BlockWide(RED, x, y)
        block_list.add(block1)
        all_list.add(block1)
        list4.append(block1)
        y+=64
def spawnMonster(Monster):
    if Monster == Bat:
        monster_list.add(Bat)
        all_list.add(Bat)
    elif Monster == Rat:
        monster_list.add(Bat1)
        all_list.add(Bat1)
    elif Monster == 3:
        monster_list.add(Bat1)
        all_list.add(Bat1)
    elif Monster == 4:
        monster_list.add(Bat1)
        all_list.add(Bat1)
def addSprites():
    addBlocksTop()
    addBlocksBottom()
    addBlocksLeft()
    addBlocksRight()
    weapon_list.add(Spear)
    #weapon_list.add(Dagger)
    
    all_list.add(Spear)
    all_list.add(Dagger)
    
def addMonster():
    monster_list.add(Bug)
    monster_list.add(Rat)
    monster_list.add(Bat)
    monster_list.add(Lizard)
    monster_list.add(Bat1)
    all_list.add(Bug)
    all_list.add(Rat)
    all_list.add(Bat)
    all_list.add(Lizard)
    all_list.add(Bat1)
def randomLoc():
    rand = random.randint(112, 412)
    return rand
Spear = Weapon('Spear')
Dagger = Weapon('Dagger')

Bug = Monster('Bug', randomLoc(), randomLoc())
Rat = Monster('Rat', randomLoc(), randomLoc())
Bat = Monster('Bat', randomLoc(), randomLoc())
Lizard = Monster('Lizard', randomLoc(), randomLoc())
Bat1 = Monster('Bat', randomLoc(), randomLoc())

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_X, SCREEN_Y)) #Create the screen
    
    newTexture = getTexture(SpriteSheet3, 200, 200, 100, 100)
    
    
    addSprites()
    addMonster()
    backdrop = pygame.Rect(0, 0, SCREEN_X, SCREEN_Y) #Create the whole screen so you can draw on it
    
    clock = pygame.time.Clock()
    done = False
    score = 0
    
        
        
    
    while not done:
        for event in pygame.event.get():
            if event.type == QUIT:
                done = True
        screen.fill(BLACK)
        all_list.draw(screen)
        pos = pygame.mouse.get_pos()
        Spear.rect.x = pos[0]
        Spear.rect.y = pos[1]
        monsters_killed_list = pygame.sprite.spritecollide(Spear, monster_list, True)
        for Monster in monsters_killed_list:
            score+=1
            print(score)
            print(Monster)
            randomLoc()
        i = 0
        n = 1
        for i in range(7):
            monsters_escaped_list = pygame.sprite.spritecollide(list[n], monster_list, True)
            for Monster in monsters_escaped_list:
                score-=1
                print(score)
                monster_list.remove(Monster)
                all_list.remove(Monster)
               
            n+=1
        i = 0
        n = 1
        for i in range(7):
            monsters_escaped_list = pygame.sprite.spritecollide(list2[n], monster_list, True)
            for Monster in monsters_escaped_list:
                score-=1
                print(score)
                monster_list.remove(Monster)
                all_list.remove(Monster)
                
            n+=1
        i = 0
        n = 1
        for i in range(7):
            monsters_escaped_list = pygame.sprite.spritecollide(list3[n], monster_list, True)
            for Monster in monsters_escaped_list:
                score-=1
                print(score)
                monster_list.remove(Monster)
                all_list.remove(Monster)
                
            n+=1
        i = 0
        n = 1
        for i in range(7):
            monsters_escaped_list = pygame.sprite.spritecollide(list4[n], monster_list, True)
            for Monster in monsters_escaped_list:
                score-=1
                print(score)
                monster_list.remove(Monster)
                all_list.remove(Monster)
                
            n+=1        
        clock.tick(60)
        
        #spawnMonster()
        
        monster_list.update()
        pygame.display.flip()
if __name__ == '__main__': main()