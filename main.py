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

pygame.font.init()

norse_font_30 = pygame.font.SysFont("Norse", 30)

class Button:
    all = []

    def __init__(self, id: int, text: str, font, x_cord: int, y_cord: int, loads_from: str, is_visible=False):

        # assert
        assert id > 0, f"ID {id} is lower than 1!"
        assert len(text) > 0, f"Text can't be empty!"

        # assign mandatory
        self.id = id
        self.text = text
        self.font = font
        self.x_cord = x_cord
        self.y_cord = y_cord
        self.loads_from = loads_from

        # assign optional
        self.is_visible = is_visible

        # pygame magic
        self.pygame_object = self.font.render(self.text, False, (0, 0, 0))

        self.x_size = self.pygame_object.get_width()
        self.y_size = self.pygame_object.get_height()


        Button.all.append(self)

    def __repr__(self):
        return f"Button({self.id}, '{self.text}', {self.font}, {self.x_cord}, {self.y_cord}, '{self.loads_from}', {self.is_visible}, {self.x_size}, {self.y_size}"


class Menu_section:
    all = []


button_new_game = Button(1, "New game", norse_font_30, 0, 0, "right", True)


if __name__ == "__main__":
    for button in Button.all:
        print(button)