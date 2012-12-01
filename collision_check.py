#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      aoisensi
#
# Created:     29/11/2012
# Copyright:   (c) aoisensi 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

import pygame
from pygame.locals import *

block_name = raw_input('Block name: ')
execfile('./block/'+block_name+'/block.py')
block = block_class()
for x in range(16):
    for y in range(16):
        print block.get_collision(x,y),
    print
