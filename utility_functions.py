# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 20:30:40 2019

@author: Ryan
"""
import math

#Returns list of cells around the center cell within a certain distance
def CellsAroundCell(x, y, distance):
    list_of_cells = []
    for i in range(-int(distance), int(distance)):
        for j in range(-int(distance), int(distance)):
            list_of_cells.append([i, j])
    
    return list_of_cells