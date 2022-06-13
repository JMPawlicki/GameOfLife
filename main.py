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

#=====================================Switchers=============================================

def walker_on():
    global turn_walker, normal, turn_boom, turn_bird, turn_x, turn_transofrmers
    turn_walker = ON
    normal = OFF
    turn_boom = OFF
    turn_bird =OFF
    turn_x = OFF
    turn_transofrmers = OFF
def normal_on():
    global turn_walker, normal, turn_boom, turn_bird, turn_x, turn_transofrmers
    turn_walker = OFF
    normal = ON
    turn_boom =OFF
    turn_bird = OFF
    turn_x = OFF
    turn_transofrmers = OFF
def boom_on():
    global turn_walker, normal, turn_boom, turn_bird, turn_x, turn_transofrmers
    turn_walker = OFF
    normal = OFF
    turn_boom =ON
    turn_bird = OFF
    turn_x = OFF
    turn_transofrmers = OFF
def bird_on():
    global turn_walker, normal, turn_boom, turn_bird, turn_x, turn_transofrmers
    turn_walker = OFF
    normal = OFF
    turn_boom = OFF
    turn_bird = ON
    turn_x = OFF
    turn_transofrmers = OFF
def x_on():
    global turn_walker, normal, turn_boom, turn_bird, turn_x, turn_transofrmers
    turn_walker = OFF
    normal = OFF
    turn_boom = OFF
    turn_bird = OFF
    turn_x = ON
    turn_transofrmers = OFF
def transformer_on():
    global turn_walker, normal, turn_boom, turn_bird, turn_x, turn_transofrmers
    turn_walker = OFF
    normal = OFF
    turn_boom = OFF
    turn_bird = OFF
    turn_x = OFF
    turn_transofrmers = ON

#===============================================Figures=====================================

def walker(pos):
    grid_pos = [pos[0] , pos[1] ]
    grid_pos[0] = grid_pos[0]//20
    grid_pos[1] = grid_pos[1]//20
    if game_window.grid[grid_pos[1]][grid_pos[0]].alive:
        game_window.grid[grid_pos[1]][grid_pos[0]].alive = False
        game_window.grid[grid_pos[1] - 1][grid_pos[0]].alive = False
        game_window.grid[grid_pos[1] - 2][grid_pos[0]].alive = False
        game_window.grid[grid_pos[1]][grid_pos[0] + 1].alive = False
        game_window.grid[grid_pos[1] - 1][grid_pos[0] + 2].alive = False
    else:
        game_window.grid[grid_pos[1]][grid_pos[0]].alive = True
        game_window.grid[grid_pos[1] - 1][grid_pos[0]].alive = True
        game_window.grid[grid_pos[1] - 2][grid_pos[0]].alive = True
        game_window.grid[grid_pos[1]][grid_pos[0] + 1].alive = True
        game_window.grid[grid_pos[1] - 1][grid_pos[0] + 2].alive = True

def boom(pos):
    grid_pos = [pos[0] , pos[1] ]
    grid_pos[0] = grid_pos[0]//20
    grid_pos[1] = grid_pos[1]//20
    if game_window.grid[grid_pos[1]][grid_pos[0]].alive:
        game_window.grid[grid_pos[1]][grid_pos[0]].alive = False
        game_window.grid[grid_pos[1] - 1][grid_pos[0]].alive = False
        game_window.grid[grid_pos[1] - 2][grid_pos[0]].alive = False
        game_window.grid[grid_pos[1]][grid_pos[0] + 1].alive = False
        game_window.grid[grid_pos[1] - 1][grid_pos[0] + 2].alive = False
        game_window.grid[grid_pos[1] - 2][grid_pos[0] + 2].alive = False
        game_window.grid[grid_pos[1]][grid_pos[0] + 2].alive = False
    else:
        game_window.grid[grid_pos[1]][grid_pos[0]].alive = True
        game_window.grid[grid_pos[1] - 1][grid_pos[0]].alive = True
        game_window.grid[grid_pos[1] - 2][grid_pos[0]].alive = True
        game_window.grid[grid_pos[1]][grid_pos[0] + 1].alive = True
        game_window.grid[grid_pos[1]][grid_pos[0] + 2].alive = True
        game_window.grid[grid_pos[1] - 1][grid_pos[0] + 2].alive = True
        game_window.grid[grid_pos[1] - 2][grid_pos[0] + 2].alive = True

def bird(pos):
    grid_pos = [pos[0] , pos[1] ]
    grid_pos[0] = grid_pos[0]//20
    grid_pos[1] = grid_pos[1]//20
    if game_window.grid[grid_pos[1]][grid_pos[0]].alive:
        game_window.grid[grid_pos[1]][grid_pos[0]].alive = False
        game_window.grid[grid_pos[1] - 1][grid_pos[0] + 1].alive = False
        game_window.grid[grid_pos[1] - 1][grid_pos[0] + 2].alive = False
        game_window.grid[grid_pos[1] - 1][grid_pos[0] + 3].alive = False
        game_window.grid[grid_pos[1] - 1][grid_pos[0] + 4].alive = False
        game_window.grid[grid_pos[1] - 1][grid_pos[0] + 5].alive = False
        game_window.grid[grid_pos[1] - 1][grid_pos[0] + 6].alive = False
        game_window.grid[grid_pos[1]][grid_pos[0] + 6].alive = False
        game_window.grid[grid_pos[1] + 1][grid_pos[0] + 6].alive = False
        game_window.grid[grid_pos[1] + 2][grid_pos[0] + 5].alive = False
        game_window.grid[grid_pos[1] + 3][grid_pos[0] + 3].alive = False
        game_window.grid[grid_pos[1] + 3][grid_pos[0] + 3].alive = False
        game_window.grid[grid_pos[1] + 3][grid_pos[0] + 2].alive = False
        game_window.grid[grid_pos[1] + 2][grid_pos[0]].alive = False
    else:
        game_window.grid[grid_pos[1]][grid_pos[0]].alive = True
        game_window.grid[grid_pos[1] - 1][grid_pos[0] + 1].alive = True
        game_window.grid[grid_pos[1] - 1][grid_pos[0] + 2].alive = True
        game_window.grid[grid_pos[1] - 1][grid_pos[0] + 3].alive = True
        game_window.grid[grid_pos[1] - 1][grid_pos[0] + 4].alive = True
        game_window.grid[grid_pos[1] - 1][grid_pos[0] + 5].alive = True
        game_window.grid[grid_pos[1] - 1][grid_pos[0] + 6].alive = True
        game_window.grid[grid_pos[1]][grid_pos[0] + 6].alive = True
        game_window.grid[grid_pos[1] + 1][grid_pos[0] + 6].alive = True
        game_window.grid[grid_pos[1] + 2][grid_pos[0] + 5].alive = True
        game_window.grid[grid_pos[1] + 3][grid_pos[0] + 3].alive = True
        game_window.grid[grid_pos[1] + 3][grid_pos[0] + 3].alive = True
        game_window.grid[grid_pos[1] + 3][grid_pos[0] + 2].alive = True
        game_window.grid[grid_pos[1] + 2][grid_pos[0]].alive = True

def x(pos):
    grid_pos = [pos[0] , pos[1] ]
    grid_pos[0] = grid_pos[0]//20
    grid_pos[1] = grid_pos[1]//20
    if game_window.grid[grid_pos[1]][grid_pos[0]].alive:
        game_window.grid[grid_pos[1]][grid_pos[0]].alive = False
        game_window.grid[grid_pos[1]][grid_pos[0] - 1].alive = False
        game_window.grid[grid_pos[1] + 2][grid_pos[0]].alive = False
        game_window.grid[grid_pos[1]][grid_pos[0] + 3].alive = False
        game_window.grid[grid_pos[1]][grid_pos[0] + 4].alive = False
        game_window.grid[grid_pos[1]][grid_pos[0] + 5].alive = False
        game_window.grid[grid_pos[1] + 1][grid_pos[0] + 2].alive = False
    else:
        game_window.grid[grid_pos[1]][grid_pos[0]].alive = True
        game_window.grid[grid_pos[1]][grid_pos[0] - 1].alive = True
        game_window.grid[grid_pos[1] + 2][grid_pos[0]].alive = True
        game_window.grid[grid_pos[1]][grid_pos[0] + 3].alive = True
        game_window.grid[grid_pos[1]][grid_pos[0] + 4].alive = True
        game_window.grid[grid_pos[1]][grid_pos[0] + 5].alive = True
        game_window.grid[grid_pos[1] + 1][grid_pos[0] + 2].alive = True
def transforemers(pos):
    grid_pos = [pos[0], pos[1]]
    grid_pos[0] = grid_pos[0] // 20
    grid_pos[1] = grid_pos[1] // 20
    if game_window.grid[grid_pos[1]][grid_pos[0]].alive:
        game_window.grid[grid_pos[1]][grid_pos[0]].alive = False
        game_window.grid[grid_pos[1] - 3][grid_pos[0]].alive = False
        game_window.grid[grid_pos[1] - 3][grid_pos[0] - 1].alive = False
        game_window.grid[grid_pos[1] - 3][grid_pos[0] + 1].alive = False
        game_window.grid[grid_pos[1] - 2][grid_pos[0] - 1].alive = False
        game_window.grid[grid_pos[1] - 2][grid_pos[0] + 1].alive = False
        game_window.grid[grid_pos[1] - 1][grid_pos[0] - 1].alive = False
        game_window.grid[grid_pos[1] - 1][grid_pos[0] + 1].alive = False
        game_window.grid[grid_pos[1] + 1][grid_pos[0] + 1].alive = False
        game_window.grid[grid_pos[1] + 1][grid_pos[0] - 1].alive = False
        game_window.grid[grid_pos[1] + 2][grid_pos[0] + 2].alive = False
        game_window.grid[grid_pos[1] + 2][grid_pos[0] - 2].alive = False
        game_window.grid[grid_pos[1] + 3][grid_pos[0] + 3].alive = False
        game_window.grid[grid_pos[1] + 1][grid_pos[0] - 3].alive = False
        game_window.grid[grid_pos[1] + 1][grid_pos[0]].alive = False
        game_window.grid[grid_pos[1] + 2][grid_pos[0]].alive = False
        game_window.grid[grid_pos[1] + 3][grid_pos[0]].alive = False
        game_window.grid[grid_pos[1] + 4][grid_pos[0] - 1].alive = False
        game_window.grid[grid_pos[1] + 4][grid_pos[0] + 1].alive = False
        game_window.grid[grid_pos[1] + 5][grid_pos[0] - 1].alive = False
        game_window.grid[grid_pos[1] + 5][grid_pos[0] + 1].alive = False
    else:
        game_window.grid[grid_pos[1]][grid_pos[0]].alive = True
        game_window.grid[grid_pos[1] - 3][grid_pos[0]].alive = True
        game_window.grid[grid_pos[1] - 3][grid_pos[0] - 1].alive = True
        game_window.grid[grid_pos[1] - 3][grid_pos[0] + 1].alive = True
        game_window.grid[grid_pos[1] - 2][grid_pos[0] - 1].alive = True
        game_window.grid[grid_pos[1] - 2][grid_pos[0] + 1].alive = True
        game_window.grid[grid_pos[1] - 1][grid_pos[0] - 1].alive = True
        game_window.grid[grid_pos[1] - 1][grid_pos[0] + 1].alive = True
        game_window.grid[grid_pos[1] + 1][grid_pos[0] + 1].alive = True
        game_window.grid[grid_pos[1] + 1][grid_pos[0] - 1].alive = True
        game_window.grid[grid_pos[1] + 2][grid_pos[0] + 2].alive = True
        game_window.grid[grid_pos[1] + 2][grid_pos[0] - 2].alive = True
        game_window.grid[grid_pos[1] + 3][grid_pos[0] + 3].alive = True
        game_window.grid[grid_pos[1] + 1][grid_pos[0] - 3].alive = True
        game_window.grid[grid_pos[1] + 1][grid_pos[0]].alive = True
        game_window.grid[grid_pos[1] + 2][grid_pos[0]].alive = True
        game_window.grid[grid_pos[1] + 3][grid_pos[0]].alive = True
        game_window.grid[grid_pos[1] + 4][grid_pos[0] - 1].alive = True
        game_window.grid[grid_pos[1] + 4][grid_pos[0] + 1].alive = True
        game_window.grid[grid_pos[1] + 5][grid_pos[0] - 1].alive = True
        game_window.grid[grid_pos[1] + 5][grid_pos[0] + 1].alive = True

#=======================================================================================

def get_events():
    global run
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            sys.exit(0)
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if mouse_on_grid(mouse_pos):
                if normal:
                    click_cell(mouse_pos)
                elif turn_walker:
                    walker(mouse_pos)
                elif turn_boom:
                    boom(mouse_pos)
                elif turn_bird:
                    bird(mouse_pos)
                elif turn_x:
                    x(mouse_pos)
                elif turn_transofrmers:
                    transforemers(mouse_pos)
            else:
                for button in buttons:
                    button.click()

def upadte():
    game_window.update()
    for button in buttons:
        button.update(mouse_pos, game_state= state)


def draw():
    screen.fill(grey)
    for button in buttons:
        button.draw()
    game_window.draw()
    pygame.draw.line(screen, black, (1201, 0), (1201, 800), 3 )
    pygame.draw.line(screen, black, (1201, 300), (width, 300), 3)

def mouse_on_grid(pos):
    if pos[0] > 0 and pos[0] < width - 300 :
        if pos[1] > 0  and pos[1] < height :
            return True
    return False

def click_cell(pos):
    grid_pos = [pos[0], pos[1]]
    grid_pos[0] = grid_pos[0]//20
    grid_pos[1] = grid_pos[1]//20
    if game_window.grid[grid_pos[1]][grid_pos[0]].alive:
        game_window.grid[grid_pos[1]][grid_pos[0]].alive = False
    else:
        game_window.grid[grid_pos[1]][grid_pos[0]].alive = True

def make_buttons():
    buttons = []
    buttons.append(Button(screen, width -300, 0, 300, 50, text = 'RUN', color=(28,111,51), hover_color=(48, 131, 81),
                          function = run_game, state= 'setting'))
    buttons.append(Button(screen, width -300, 0, 300, 50, text = 'PAUSE', color=(18,104,135), hover_color=(51,168,212),
                          function= pause_game, state = 'running'))
    buttons.append(Button(screen, width -300, 150, 300, 50, text = 'RESET', color=(117,40,14), hover_color=(217, 54, 54),
                          function= reset_game, state= 'paused'))
    buttons.append(Button(screen, width - 300, 100, 300, 50, text='RESUME', color=(28,111,51), hover_color=(48, 131, 81),
               function=run_game, state='paused'))
    buttons.append(
        Button(screen, width - 300, 550, 300, 50, text='Walker', color=(28, 111, 51), hover_color=(48, 131, 81),
               function = walker_on ))
    buttons.append(
        Button(screen, width - 300, 500, 300, 50, text='Default', color=(28, 111, 51), hover_color=(48, 131, 81),
               function= normal_on))
    buttons.append(
        Button(screen, width - 300, 600, 300, 50, text='Boom', color=(28, 111, 51), hover_color=(48, 131, 81),
               function=boom_on))
    buttons.append(
        Button(screen, width - 300, 650, 300, 50, text='Bird', color=(28, 111, 51), hover_color=(48, 131, 81),
               function= bird_on))
    buttons.append(
        Button(screen, width - 300, 700, 300, 50, text='Figure X', color=(28, 111, 51), hover_color=(48, 131, 81),
               function= x_on))
    buttons.append(
        Button(screen, width - 300, 750, 300, 50, text='Transformers', color=(28, 111, 51), hover_color=(48, 131, 81),
               function=transformer_on))
    return buttons
