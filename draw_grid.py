# -*- coding: utf-8 -*-
"""
Created on Sat Oct  6 15:56:21 2018

@author: Ryan
"""
import numpy as np
import cv2

LINE_WDITH = 1
SQUARE_WIDTH = 5
IMAGE_SIZE = 900

def draw_grid(color_array, length, width):
    
    img = np.zeros((IMAGE_SIZE,IMAGE_SIZE,3),np.uint8)
    
    if len(color_array) != length * width:
        print("ERROR: Array size does not match length * width parameters")
        return False
    width_per_square = np.int(np.floor((IMAGE_SIZE - width + LINE_WDITH)/width))
    length_per_square = np.int(np.floor((IMAGE_SIZE - length + LINE_WDITH)/length))
    if ( width_per_square < SQUARE_WIDTH or length_per_square < SQUARE_WIDTH ):
        print("Error: Squares are too small")
        return False
    
    bgr_array = [ colors_to_bgr(x) for x in color_array ]
    
    x = 0
    y = 0
    
    for color in bgr_array:
        #print("Color {}, x: {}, y {}".format(color, x, y))
        for i in range(3):
            img[y : y + length_per_square, x : x + width_per_square, i ] = color[i]
        x = x + width_per_square + LINE_WDITH
        if ( x >= IMAGE_SIZE ):
            y = y + length_per_square + LINE_WDITH
            x = 0
    
    cv2.imshow('image',img)
    k = cv2.waitKey(10)
    if (k == 113):  # "q"
        return False
    return True

def close_grid():
    cv2.destroyAllWindows()
    
def colors_to_bgr(color_name):
    if color_name == "blue":
        return [255, 0, 0]
    elif color_name == "green":
        return [0, 255, 0]
    elif color_name == "grey":
        return [160, 160, 160]
    elif color_name == "magenta":
        return [127, 0, 255]
    elif color_name == "orange":
        return [0, 128, 255]
    elif color_name == "pink":
        return [204, 153, 255]
    elif color_name == "purple":
        return [153, 0, 153]
    elif color_name == "red":
        return [0, 0, 255]
    elif color_name == "turquoise":
        return [255, 255, 0]
    elif color_name == "white":
        return [255, 255, 255]
    elif color_name == "yellow":
        return [51, 255, 255]
    else: #black
        return [0, 0, 0]
    
    
def test_colors():
    img = np.zeros((IMAGE_SIZE,IMAGE_SIZE,3),np.uint8)
    
    color_array = ["red", "orange", "yellow", "green", "turquoise", "blue",
                   "purple", "magenta", "pink", "white", "grey", "black"]
    print(color_array)
    bgr_array = [ colors_to_bgr(x) for x in color_array ]
    
    j = np.int(0)
    for color_value in bgr_array:
        jump_value = np.int(np.floor(IMAGE_SIZE/len(bgr_array)))
        for i in range(3):
            img[:,j : j + jump_value,i] = color_value[i]
        j = j + jump_value
        
    
    cv2.imshow('image',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    