import random

import pygame,sys
from window import *
from button import *
from menu import Gra


pygame.init()
menu = Gra()
black = (0, 0, 0)
white = (255, 255, 255)
grey = (128, 128, 128)
width = 1500
height = 800
size = (width, height)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Game of Life")
clock = pygame.time.Clock()
game_window = Game_window(screen, 0, 0)
fps = 10
fps_in_game = 10
ON= True
OFF = False
turn_walker = OFF
turn_boom = OFF
turn_bird = OFF
turn_x = OFF
turn_transofrmers = OFF
normal = ON
run = True