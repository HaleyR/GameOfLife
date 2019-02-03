# -*- coding: utf-8 -*-
"""
Created on Sun Jan 20 11:49:48 2019

@author: Ryan
"""

import update_functions

DEAD_COLOR = "white"
ALIVE_COLOR = "magenta"
ERROR_COLOR = "grey"

class GameOfLifeBlock:
    def __init__(self, input_type, x, y, dist):
        self.x = x
        self.y = y
        if input_type > dist:
            self.type = "dead"
            self.color = DEAD_COLOR
            self.update_function = update_functions.DeadCellsUpdate
        else:
            self.type = "alive"
            self.color = ALIVE_COLOR
            self.update_function = update_functions.LiveCellsUpdate
        self.next_type = ""
        
    
    def update(self):
#        print(self.x)
#        print(self.y)
#        print(self.type)
#        print(self.next_type)
#        print("|||")
        self.type = self.next_type
        self.next_type = ""
        if self.type == "dead":
            self.color = DEAD_COLOR
            self.update_function = update_functions.DeadCellsUpdate
        elif self.type == "alive":
            self.color = ALIVE_COLOR
            self.update_function = update_functions.LiveCellsUpdate
        else:
            self.color = ERROR_COLOR
#        print(self.x)
 #       print(self.y)
 #       print(self.type)
 #       print(self.next_type)            
 #       print("----")
        return self