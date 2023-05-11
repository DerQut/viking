import pygame
from pygame.locals import *
import time
import random
import os
import ctypes
import subprocess
import webbrowser

import classes

#rows, cols = (480, 480)
#all_points = [[0 for i in range(cols)] for j in range(rows)]

pygame.font.init()

norse_font_30 = pygame.font.SysFont("Norse", 30)




button_new_game = classes.Button(1, "New game", norse_font_30, (200, 300), "right", True)


if __name__ == "__main__":
    for button in classes.Button.all:
        print(button)