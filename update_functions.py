# -*- coding: utf-8 -*-
"""
Created on Sun Jan 20 11:53:28 2019

@author: Ryan
"""

import numpy as np

def IsCellLive(array, x_position, y_position):
    if (array[y_position][x_position].type == "alive"):
        return True
    else:
        return False

def CountLiveCells(array, x_position, y_position):
    #Check all the cells around the cell. Don't go past boundries
    live_cell_count = 0
    surrond_array = [ [-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1],
                      [1, 0], [1, 1]]
    for offset in surrond_array:
        try:
            if (x_position + offset[0] >= 0 and y_position + offset[1] >= 0):
                if IsCellLive(array, x_position + offset[0], y_position + offset[1]) == True:
                    live_cell_count = live_cell_count + 1
        except IndexError:
            live_cell_count = live_cell_count
    return live_cell_count

def DeadCellsUpdate(array, block):
    count = CountLiveCells(array, block.x, block.y);
    if CountLiveCells(array, block.x, block.y) == 3:
        block.next_type = "alive"
    else:
        block.next_type = "dead"
    #if (block.x == 4 and block.y == 17):
    #    print("Dead Cell {}, {} counted {} live cells, and will be {}".format(block.x, block.y, count, block.next_type))
        
def LiveCellsUpdate(array, block):
    count = CountLiveCells(array, block.x, block.y);
    if count < 2:
        block.next_type = "dead"
    elif count < 4:
        block.next_type = "alive"
    else:
        block.next_type = "dead"    
    #if (block.x == 4 and block.y == 17):
    #    print("Live Cell {}, {} counted {} live cells, and will be {}".format(block.x, block.y, count, block.next_type))