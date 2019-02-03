# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 20:25:40 2019

@author: Ryan
"""

from utility_functions import CellsAroundCell

def GrassUpdate(grass, gameboard, new_objects):
    for block in CellsAroundCell(grass.x, grass.y, 1):
        if gameboard[block[0], block[1]] == "land":
            new_objects.extend({"type":"grass", "x":block[0], "y":block[1]})
            