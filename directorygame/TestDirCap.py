import glob
import os
import pygame
import constants
import SpriteSheet
directory = '/Users/Public/Documents/Test'
i = 0

while i < 2:
    if not os.path.exists(directory):
        os.makedirs(directory)
    else:
        print("oofed")
    i = i + 1
    for file in glob.glob("*.txt"):
        print(file)
pygame.init()

screen = pygame.display.set_mode((constants.SCREEN_HEIGHT, constants.SCREEN_WIDTH))

BACKGROUND = (0, 0, 37, 37)
BACKGROUND2 = (37, 0, 37, 37)
class Ground(pygame.sprite.Sprite):
    def __init__(self, sprite_sheet_data):
        """ Platform constructor. Assumes constructed with user passing in
            an array of 5 numbers like what's defined at the top of this
            code. """
        super().__init__()
 
        sprite_sheet = SpriteSheet("hyptosis_tile-art-batch-3.png")
        # Grab the image for this platform
        self.image = sprite_sheet.get_image(sprite_sheet_data[0],
                                            sprite_sheet_data[1],
                                            sprite_sheet_data[2],
                                            sprite_sheet_data[3])
 
        self.rect = self.image.get_rect()


while i < 1000:
    pygame.sprite.Group().draw(screen)
    i = i + 1
