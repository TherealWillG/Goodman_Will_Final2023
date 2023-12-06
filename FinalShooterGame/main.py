# This File was created by Will Goodman on 12/5
# Sources : Jcode on Youtube. @ https://www.youtube.com/@JCode777
# Mr. Cozort, for Code base resources. @ https://github.com/ccozort
'''
Goals:
I want to be able to create a rougelike game similar to that of binding of isaac or brotato. 
I want there to be multiple different levels/areas, different weapons, and different types of mobs. 
I want there to be random chances for things like bossfights, or weapon spawns, or buff spawns. 
I don't necessarily think I need an end goal, but the rougelike should have some sort of score system
that would allow players to work towards a goal. At the very least, If I cannot create levels, I want to create 
an endless survival game with weapons and multiple unique enemies. Something similar to galaga. 
'''
# Or
'''
If the game engine becomes impractical, I would want to create a screen scraper that would essentially
highlight or repeat key ideas on the page based off of certain words. 
'''

# Import all necessary libraries 
import pygame as pg
import sys
import math
import pygame.sprite as sprite
from settings import *
from sprites import * 
import os

'''
for some reason, while experimenting with file paths and image loading, that for some reason,
setting up file paths and folders is unecessary. I discovered that if the image files are within specifically the 
"code" folder, or the folder that contains every single subfolder containing my code, specifying my 
file paths was unecessary, and that simply saying "pg.image.load" is sufficient for the computer
to find my image files, i think that we were taught to avoid this for organizations sake. 
But for some reason, When i Name the file paths and attempt to blit/draw them, they dont appear.
'''


# initialize pygame
pg.init()

# create window
screen = pg.display.set_mode((HEIGHT, WIDTH))
clock = pg.time.Clock()

# Set background images
background = pg.image.load("background.png").convert()

player = Player()

while True:
    keys = pg.key.get_pressed()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()

    screen.blit(background, (0,0))   
    screen.blit(player.image, player.pos)

    pg.display.update()
    clock.tick(FPS)
 
