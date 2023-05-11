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

    def __init__(self, id: int, text: str, font, top_left_cords, loads_from: str, is_visible=False):

        # assert
        assert id > 0, f"ID {id} is lower than 1!"
        assert len(text) > 0, f"Text can't be empty!"

        # assign mandatory
        self.id = id
        self.text = text
        self.font = font
        self.top_left_cords = top_left_cords
        self.loads_from = loads_from

        # assign optional
        self.is_visible = is_visible

        # pygame magic
        self.pygame_object = self.font.render(self.text, False, (0, 0, 0))

        self.x_size = self.pygame_object.get_width()
        self.y_size = self.pygame_object.get_height()

        self.bottom_right_cords = (self.top_left_cords[0] + self.x_size, self.top_left_cords[1] + self.y_size)


        Button.all.append(self)

    def __repr__(self):
        return f"Button({self.id}, '{self.text}', {self.font}, {self.top_left_cords}, {self.bottom_right_cords}, '{self.loads_from}', {self.is_visible}"


class Menu_section:
    all = []