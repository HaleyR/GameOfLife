# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 20:14:06 2019

@author: Ryan
"""

import complex_update

class BlockObjects:
    def __init__(self, input_type, x, y):
        if(input_type == "grass"):
            self.type = "grass"
            self.color = "green"
            self.x = x
            self.y = y
            self.age = 0
            self.hunger_limit = -1
            self.thirst_limit = -1
            self.exists = True
            self.update_function = complex_update.GrassUpdate
        else:
            self.type = "land"
            self.color = "white"
            self.x = x
            self.y = y
            self.age = 0
            self.hunger_limit = -1
            self.thirst_limit = -1
            self.exists = True
            self.update_function = complex_update.DummyUpdate