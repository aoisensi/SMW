#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      aoisensi
#
# Created:     28/11/2012
# Copyright:   (c) aoisensi 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

import pygame
from pygame.locals import *
import sys
import os

class Collision(object):
    left = False
    right = False
    up = False
    down = False
    def __init__(self):
        self.left = False
        self.right = False
        self.up = False
        self.down = False
    def _not_ander(self, left, right, up, down):
        self.left = self.left and (not left)
        self.right = self.right and (not right)
        self.up = self.up and (not up)
        self.down = self.down and (not down)

class BlockClasses(object):
    block_classes = {}   #dict <string, class>
    @staticmethod
    def __init__():
        for name in os.listdir("./block/"):
            if os.path.isdir("./block/"+name):
                execfile("./block/"+name+"/block.py", globals())
                BlockClasses.block_classes[name] = block_class
                print name
    @staticmethod
    def get_class(name):
        return BlockClasses.block_classes[name]

class SpriteClasses(object):
    sprite_classes = {} #dict <string, class>
    @staticmethod
    def __init__():
        for name in os.listdir("./sprite/"):
            if os.path.isdir("./sprite/"+name):
                execfile("./sprite/"+name+"/sprite.py", globals())
                SpriteClasses.sprite_classes[name] = sprite_class
                print name
    @staticmethod
    def get_class(name):
        return SpriteClasses.sprite_classes[name]


class Stage(object):
    stage = []     #list <list <block class>>
    def __init__(self, path):
        for stage_date_line in open(path):
            stage_line = []
            stage_date_line = stage_date_line.rstrip()
            for stage_date_block in stage_date_line.split(' '):
                stage_line.append(BlockClasses.get_class(stage_date_block)())
            self.stage.append(stage_line)

    def get_block(self, x, y):
        try:
            return self.stage[y][x]
        except IndexError:
            return None

    def get_height(self):
        return len(self.stage)

    def get_width(self):
        return len(self.stage[0])

    def get_block_pic(self, x, y):
        return self.get_block(x, y).get_picture()

    def _get_collision_natural(self, x, y):
        block = self.get_block(int(x/16),int(y/16))
        if block == None:
            return Collision()
        else:
            return block.get_collision(x%16, y%16)

    def get_collision(self, x, y):
        collision = self._get_collision_natural(x, y)
        up = self._get_collision_natural(x, y - 1).down
        down = self._get_collision_natural(x, y + 1).up
        left = self._get_collision_natural(x - 1, y).right
        right = self._get_collision_natural(x + 1, y).left

        collision._not_ander(left, right, up, down)

        return collision


SCREEN_SIZE = (320, 240)
FPS = 60

pygame.init()

font = pygame.font.Font(None, 12)

screen = pygame.display.set_mode(SCREEN_SIZE)

pygame.display.set_caption("Window")

player = pygame.image.load("player.png")
player.set_colorkey((255,255,255))
player_rect = player.get_rect()

BlockClasses() #load class

stage = Stage("stage.txt")

jump_flag = False
player_on_ground = False

pygame.time.set_timer(16, 31)

clock = pygame.time.Clock()

player_move_x = 0
player_move_y = 0

while True:
    clock.tick(FPS)

    do_jump = False

    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        if event.type == KEYDOWN:
            do_jump = event.key == K_SPACE

    screen.fill((0, 0, 255))

    #render_stage
    for y in range(0,stage.get_height()):
        for x in range(0,stage.get_width()):
            picture = stage.get_block_pic(x, y)
            if picture != None:
                screen.blit(picture, picture.get_rect().move(x*16, y*16))


    #move_player
    pkeys = pygame.key.get_pressed()
    if pkeys[K_LEFT]:
        if player_move_x == 0.0:
            player_move_x = -1.0
        elif player_move_x > -3.0:
            player_move_x -= 0.1
    elif pkeys[K_RIGHT]:
        if player_move_x == 0.0:
            player_move_x = +1.0
        elif player_move_x < +3.0:
            player_move_x += 0.1
    else:
        if player_move_x < 0.0:
            if player_move_x > -1.0:
                player_move_x = 0
            else:
                player_move_x += 0.2
        elif player_move_x > 0.0:
            if player_move_x < +1.0:
                player_move_x = 0
            else:
                player_move_x -= 0.2

    if not player_on_ground:
        if(player_move_y < 5):
            if(player_move_y < 0 and pkeys[K_SPACE]):
                player_move_y += 0.15
            else:
                player_move_y += 0.3
    #jump
    if do_jump:
        if player_on_ground:
            player_move_y = -5
            player_on_ground = False

    player_rect.move_ip(player_move_x, player_move_y)

    #landing
    if player_move_y >= 0:
        player_moving_x = abs(int(player_move_x))
        for local_y in range(14 - int(player_move_y) - player_moving_x, 16 + player_moving_x ):
            global_y = local_y + player_rect.top
            global_left_x = player_rect.left + 7
            global_right_x = global_left_x + 1
            if(stage.get_collision(global_left_x, global_y).up or stage.get_collision(global_right_x, global_y).up):
                player_on_ground = True
                player_move_y = 0
                player_rect.move_ip(0, local_y - 15)
                break
        else:
            for local_y in range(15 - int(player_move_y), 16):
                is_break = False
                global_y = local_y + player_rect.top
                for local_x in range(16):
                    global_x = local_x + player_rect.left
                    collision = stage.get_collision(global_x, global_y)
                    if(collision.up and (collision.left or collision.right)):
                        player_on_ground = True
                        player_move_y = 0
                        player_rect.move_ip(0, local_y - 15)
                        is_break = True
                        break
                if is_break:
                    break
            else:
                player_on_ground = False

    #wall hit left
    wall_left_hit = False
    for local_x in range(7,-1,-1):
        is_break = False
        global_x = local_x + player_rect.left
        for local_y in range(1,14):
            global_y = local_y + player_rect.top
            collision = stage.get_collision(global_x, global_y)
            if(collision.right and not collision.up):
                player_rect.move_ip(local_x + 1, 0)
                wall_left_hit = True
                player_move_x = 0
                is_break = True
                break
        if is_break:
            break

    #wall hit right
    wall_right_hit = False
    for local_x in range(8,16):
        is_break = False
        global_x = local_x + player_rect.left
        for local_y in range(1,14):
            global_y = local_y + player_rect.top
            collision = stage.get_collision(global_x, global_y)
            if(collision.left and not collision.up):
                player_rect.move_ip(local_x - 16, 0)
                wall_left_hit = True
                player_move_x = 0
                is_break = True
                break
        if is_break:
            break

    #strike
    if player_move_y <= 0:
        for local_y in range(7,-1,-1):
            is_break = False
            global_y = local_y + player_rect.top
            for local_x in range(1,15):
                global_x = local_x + player_rect.left
                collision = stage.get_collision(global_x, global_y)
                if(collision.down):
                    player_move_y = 0
                    player_rect.move_ip(0, local_y)
                    is_break = True
                    break


    screen.blit(player, player_rect)

    pygame.display.update()

    pygame.display.set_caption(str(clock.get_fps()))




