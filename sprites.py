# This file was created of 11/27 by Will Goodman

import pygame as pg
import sys
import math
import pygame.sprite as Sprite
from pygame.math import Vector2 as vec
from settings import *



game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'images')
snd_folder = os.path.join(game_folder, 'sounds')


class Player:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.width = w
        self.height = h
    def main(self, display):
        pg.draw.rect(display, (255, 0, 0), (self.x, self.y, self.width, self.height))

class PB:
    def __init__(self, x, y, mouse_x, mouse_y):
        self.x = x
        self.y = y 
        self.mouse_x = mouse_x
        self.mouse_y = mouse_y
        self.speed = 15
        self.angle = math.atan2(y-mouse_y, x-mouse_x)
        self.x_vel = math.cos(self.angle) * self.speed 
        self.y_vel = math.sin(self.angle) * self.speed
    def main(self,display):
        self.x -= int(self.x_vel)
        self.y -= int(self.y_vel)

        pg.draw.circle(display, (0,0,0), (self.x, self.y), 5)
