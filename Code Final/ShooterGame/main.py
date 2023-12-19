# This file was created by Will Goodman on 12/2
'''
Some of the major things I'd like to add to my game engine are animations, both player and mob animations. 
I believe that some sort of interesting graphics or user interface is the most important thing when it comes
to designing this game, I would rather turn in an incomplete game while achieving my goal of having 
sprite animations than turn in a somewhat completed game with little to no visual appeal, I would also like 
to create some sort of projectile system, because while making my previous game, I did want to include some sort
of shooter aspect to it. 
'''
'''
Goals:
Character animations
Shooting capabilities
Mobs
Mob animations
'''


'''
Sources: scriptline studios: https://www.youtube.com/@ScriptLineStudios
# The majority of the tutorials I used for this assignment were from scriptline studios, 
along with the player and mob images
# Mr. Cozort: https://github.com/ccozort, majority of the baseline code, such as the classes setup, 
were from the source code that was given to us during the first videogame project. basically the stuff taken from kids can code

'''


import pygame
import sys
import math
import random
from settings import *
import os


# initialize pygame
pygame.init()


game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'images')

pg.image.load(os.path.join(img_folder, "skyrim.png")).convert()

# set display window and clock
display = pygame.display.set_mode((HEIGHT, WIDTH))
clock = pygame.time.Clock()

# sets images for player and player weapon
'''
For some reason the animation pictures will not load when I try to specify their paths in os, I'm sort of unsure why.
Currently, in order for code to function properly, you have to only open the code final folder. 
If the folder labeled "CODE FINAL" is not the only one opened, then the images will not load.
'''
player_walk_images = [pygame.image.load("player_walk_0.png"), pygame.image.load("player_walk_1.png"), pygame.image.load(img_folder, "player_walk_2.png"), pygame.image.load(img_folder, "player_walk_3.png")]

player_weapon = pygame.image.load("shotgun.png").convert()
player_weapon.set_colorkey((255,255,255))


# Create player class
class Player:
    def __init__(self, x, y, width, height):
        # set starting parameters for player
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        # Set the animation count to 0 first
        self.animation_count = 0
        self.moving_right = False
        self.moving_left = False
        # Hitpoints have been created, but I don't think I'll be able to implement damage before the project is due
        self.hitpoints = 100
    def handle_weapons(self, display):
        # This following code will get the live position of the mouse, and rotate the gun such that barrel faces the mouse pos
        mouse_x, mouse_y = pygame.mouse.get_pos()

        rel_x, rel_y = mouse_x - player.x, mouse_y - player.y
        angle = (180 / math.pi) * -math.atan2(rel_y, rel_x)

        player_weapon_copy = pygame.transform.rotate(player_weapon, angle)

        display.blit(player_weapon_copy, (self.x+15-int(player_weapon_copy.get_width()/2), self.y+25-int(player_weapon_copy.get_height()/2)))


    def main(self, display):
        # This portion creates an if statement to allow animations to be player
        if self.animation_count + 1 >= 16:
            self.animation_count = 0

        self.animation_count += 1

        '''
        basically, each animation, or picture in the animation, should display for aroudn 4 frames for it to look
        natural and smooth. So thus we force the animation count to reset once it is greater than 16, as
        the animation count has 1 added to it every frame, limiting to the total to 16 would mean that
        all 4 animation images will have to be played within 16 frames, ensuring that each gets 4.
        creating a somewhat smooth animation
        '''
# blits the animations onto the screen so that they play depending on which direction the player is moving in
# By specifying that the player has to be moving right or left, we ensure the animation doesn't play when still
        if self.moving_right:
            display.blit(pygame.transform.scale(player_walk_images[self.animation_count//4], (32, 42)), (self.x, self.y))
        elif self.moving_left:
# Since the animation should be different depending on whether you are moving right or left, I've flipped the animation for walking left
            display.blit(pygame.transform.scale(pygame.transform.flip(player_walk_images[self.animation_count//4], True, False), (32, 42)), (self.x, self.y))
        else:
            display.blit(pygame.transform.scale(player_walk_images[0], (32, 42)), (self.x, self.y))

        self.handle_weapons(display)

        self.moving_right = False
        self.moving_left = False

# Creates a class for the bullet, as it currently stands they don't exactly do anything
class PlayerBullet:
    def __init__(self, x, y, mouse_x, mouse_y):
        self.x = x
        self.y = y
        self.mouse_x = mouse_x
        self.mouse_y = mouse_y
        # Sets bullet speed
        self.speed = 5
        # Allows the bullet to go in the direction of the cursor
        self.angle = math.atan2(y-mouse_y, x-mouse_x)
        self.x_vel = math.cos(self.angle) * self.speed
        self.y_vel = math.sin(self.angle) * self.speed
    def main(self, display):
        self.x -= int(self.x_vel)
        self.y -= int(self.y_vel)
# Displays the bullets fired on screen
        pygame.draw.circle(display, (0,0,0), (self.x+16, self.y+16), 5)

class SlimeEnemy:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.hitpoints = 5
        # Sets images for slime animations
        self.animation_images = [pygame.image.load( "slime_animation_0.png"), pygame.image.load("slime_animation_1.png"),
        pygame.image.load("slime_animation_2.png"), pygame.image.load("slime_animation_3.png")]
        '''
        So, in order to create smoother mob movement, while still having the mob move towards the player,
        I've created an offset, meaning that rather than have the mob continously move towards the players
        real time coordinates, the mob will move towards coordinates surrounding the player, or the player's previous
        coordinates, making the mob seem as though it has some sort of patterned movement
        '''
        self.animation_count = 0
        self.reset_offset = 0
        self.offset_x = random.randrange(-300, 300)
        self.offset_y = random.randrange(-300, 300)
        # This is an attempt at creating collision, but for some reason the hitboxes aren't working
    # def collisions(self):
    #     hits = pygame.sprite.spritecollide(self, projectiles, True)
    #     if hits:
    #         self.hitpoints - 10
    #         if self.hitpoints < 0:
    #             pygame.quit()
    def main(self, display):
        # Allows the animations to be played
        if self.animation_count + 1 == 16:
            self.animation_count = 0
        self.animation_count += 1

# Allows the animations to repeat despite having no player interaction
        '''
        This allows for the offset factor to reset every time the slime animation finishes playing, meaning that 
        after any random number between 120-150 frames occurs, the offet will reset and make the offset a random
        value between the -300 and 300 that were stated earlier, basically meaning that every few seconds, 
        the slime's movement trajectory will change. The computer will pick a new location that is near the player
        and tell the slime to go towards it 
        '''
        if self.reset_offset == 0:
# This generates a random offset based off the players current position
# It basically takes the player's coords, adds any random amount between -300 and 300 to them, creating offset from player pos
            self.offset_x = random.randrange(-300, 300)
            self.offset_y = random.randrange(-300, 300)
# Every 120-150 frames, or 2-3 seconds the slime's trajectory will change, as the reset func runs every 120-150 frames
            self.reset_offset = random.randrange(120, 150)
        else:
            self.reset_offset -= 1
# If player pos + offset is to the right of the slime, it moves to the right.
        if player.x + self.offset_x > self.x-display_scroll[0]:
            self.x += 1
# If the players pos + offset is to the left of the slime, it will move to the left
        elif player.x + self.offset_x < self.x-display_scroll[0]:
            self.x -= 1
# If player pos + offset is to the top of the slime, the slime moves up
        if player.y + self.offset_y > self.y-display_scroll[1]:
            self.y += 1
# If the players pos + offset is to the bottom of the slime, the slime moves down
        elif player.y + self.offset_y < self.y-display_scroll[1]:
            self.y -= 1
# Blits animations on screen
        display.blit(pygame.transform.scale(self.animation_images[self.animation_count//4], (32, 30)), (self.x-display_scroll[0], self.y-display_scroll[1]))


# Spawns the starting point of the slime enemy and player
enemies = [SlimeEnemy(400, 300)]
player = Player(400, 300, 32, 32)
projectiles = PlayerBullet

display_scroll = [0,0]

player_bullets = []
# A while loop to keep the game running until closed
while True:
    display.fill((24,164,86))

    mouse_x, mouse_y = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                player_bullets.append(PlayerBullet(player.x, player.y, mouse_x, mouse_y))
# Sets the controls for the player, using WASD
    keys = pygame.key.get_pressed()

    pygame.draw.rect(display, (255,255,255), (100-display_scroll[0], 100-display_scroll[1], 16, 16))

    if keys[pygame.K_a]:
        display_scroll[0] -= 5

        player.moving_left = True

        for bullet in player_bullets:
            bullet.x += 5
    if keys[pygame.K_d]:
        display_scroll[0] += 5

        player.moving_right = True

        for bullet in player_bullets:
            bullet.x -= 5
    if keys[pygame.K_w]:
        display_scroll[1] -= 5

        for bullet in player_bullets:
            bullet.y += 5
    if keys[pygame.K_s]:
        display_scroll[1] += 5

        for bullet in player_bullets:
            bullet.y -= 5


    player.main(display)

    for bullet in player_bullets:
        bullet.main(display)


    for enemy in enemies:
        enemy.main(display)

# Sets the FPS, and updates all sprites and images in pygame.
    clock.tick(FPS)
    pygame.display.update()
