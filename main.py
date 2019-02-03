# -*- coding: utf-8 -*-
"""
Created on Sat Oct  6 15:53:11 2018

@author: Ryan
"""

import draw_grid
import test_functions
from gameoflifeblock import GameOfLifeBlock as blocks
import random
import itertools

length = 150
width = 150
alive_dist = 10

#dumb_list = ['red', 'blue', 'green', 'purple']#[1, 2, 3, 4]
#dumb_list = [test_functions.numb_to_color(random.randint(0,10)) for x in range(length * width)]

#draw_grid.draw_grid(dumb_list, length, width)
#draw_grid.test_colors()

#random.seed(10)
gameboard = [ [blocks(random.randint(0,100), x, y, alive_dist) for x in range(length)] for y in range(width) ]
draw_grid.draw_grid([ x.color for x in list(itertools.chain.from_iterable(gameboard))], length, width)

print("Press 'q' to quit")
while True:
    for j in list(itertools.chain.from_iterable(gameboard)):
        j.update_function(gameboard, j)
    for j in list(itertools.chain.from_iterable(gameboard)):
        blocks.update(j)
    
    if(draw_grid.draw_grid([ x.color for x in list(itertools.chain.from_iterable(gameboard))], 
                            length, width) == False):
        print("Quitting...")
        break;

draw_grid.close_grid()