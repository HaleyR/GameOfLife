# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 20:43:33 2019

@author: Ryan
"""

import blockobjects as anObject
import draw_grid
import itertools
import random

def TypeAssigner(number):
    if number == 0:
        return "grass"
    else:
        return "land"

length = 150
width = 150

object_list = [ anObject("grass", 1, 1) ]
#object_list = [ [anObject("grass", x, y) if random.randint(0,100) < 33 for x, y in itertools.permutations(range(length),range(width))]
[]
draw_grid.draw_grid([ x.color for x in list(itertools.chain.from_iterable(gameboard))], length, width)