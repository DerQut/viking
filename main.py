import pygame
from pygame.locals import *
import time
import random
import os
import ctypes
import subprocess
import webbrowser

#rows, cols = (480, 480)
#all_points = [[0 for i in range(cols)] for j in range(rows)]

class Button:
    all = []

    def __init__(self, id: int, text: str, font_size: int, x_cord: int, y_cord: int, loads_from: str, is_visible=False):

        # assert
        assert id > 0, f"ID {id} is lower than 1!"
        assert font_size > 0, f"Font size {font_size} is lower than 1!"
        assert len(text) > 0, f"Text can't be empty!"

        # assign mandatory
        self.id = id
        self.text = text
        self.font_size = font_size
        self.x_cord = x_cord
        self.y_cord = y_cord
        self.loads_from = loads_from

        # assign optional
        self.is_visible = is_visible

        Button.all.append(self)

class Menu_section:
    all = []

    def __init__(self):