# This file was created by Will Goodman on 11/16/2023
# Sources: ScriptLine Studios: https://www.youtube.com/watch?v=sVbFS9qEl4Y, https://www.youtube.com/watch?v=ilwcJrV1fdk&t=1s 
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
# Imports
import pygame as pg
import sys
from sprites import *
from settings import *
import math
pg.init()

# sets game window size, and creates game clock
display = pg.display.set_mode((960,720))
clock = pg.time.Clock()

game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'images')
snd_folder = os.path.join(game_folder, 'sounds')


player = Player(400, 300, 32, 32)
display_scroll = [0,0]
Player_Bullets = []


while True:
    # Sets the color of the backgroudn
    display.fill((24,164,86))

    mouse_x, mouse_y = pg.mouse.get_pos()

    for event in pg.event.get():
# allows you to close game window. Idk why i decided to use sys.exit() over pg.quit(), they both do the same thing
        if event.type == pg.QUIT:
            sys.exit()
        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                Player_Bullets.append(PB(player.x, player.y, mouse_x, mouse_y))
    clock.tick(60)
    # Allows for movement based on pressing keys. WASD are the controls
    # I don't think I'll add a jump key, I plan to have this game kinda act as a top down game
    keys = pg.key.get_pressed()

    pg.draw.rect(display, (255,255,255),(100-display_scroll[0], 100-display_scroll[1], 16, 16))

    if keys[pg.K_a]:
        display_scroll[0] += 5
        for bullet in Player_Bullets:
            bullet.x += 5
    if keys[pg.K_d]:
        display_scroll[0] -= 5
        for bullet in Player_Bullets:
            bullet.x -= 5
    if keys[pg.K_w]:
        display_scroll[1] += 5
        for bullet in Player_Bullets:
            bullet.y += 5
    if keys[pg.K_s]:
        display_scroll[1] -= 5
        for bullet in Player_Bullets:
            bullet.y -= 5
    
    player.main(display)

    for bullet in Player_Bullets:
        bullet.main(display)

    pg.display.update()





g = Game()

pg.quit()