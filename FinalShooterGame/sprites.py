# This file was created by Will Goodman on 12/5
import pygame as pg
import sys
import math
import pygame.sprite as Sprite
from pygame.math import Vector2 as vec
from settings import *

class Player(pg.sprite.Sprite):
    def __init__ (self):
        super().__init__()
        self.image = pg.transform.rotozoom(pg.image.load("character.png").convert_alpha(), 0, player_size)
        self.pos = pg.math.Vector2(player_start_x, player_start_y)
        self.speed = player_speed

    def player_input(self):
        self.velocity_x = 0 
        self.velocity_y = 0 

        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            self.velocity_y = -5
        if keys[pg.K_s]:
            self.velocity_y = 5
        if keys[pg.K_a]:
            self.velocity_x = 5
        if keys[pg.K_d]:
            self.velocity_x = -5
        
            
