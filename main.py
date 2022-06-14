
import random

import pygame,sys
from window import *
from button import *
from Menu import Gra

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
fps = 60
fps_in_game = 60
ON= True
OFF = False
turn_walker = OFF
turn_boom = OFF
turn_bird = OFF
turn_x = OFF
turn_transofrmers = OFF
normal = ON
run = True
clock_ticks = 15
#---------------------------------------------------------Game speed---------------------------------------------------------------
def plus():
    global clock_ticks
    if clock_ticks > 0 and clock_ticks < 60:
        clock_ticks += 5
    else:
        clock_ticks = 60

def minus():
    global clock_ticks
    if clock_ticks > 10:
        clock_ticks -= 5
    else:
        clock_ticks = 10



#----------------------------------------------------------Switchers---------------------------------------------------------------
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

#----------------------------------------------------------Figures---------------------------------------------------------------

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
#---------------------------------------------------------------------------------------------------------------------------

def get_events():
    global run
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            menu.wybor_levela()
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
    screen.fill((89, 86, 84))
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
    buttons.append(Button(screen, width - 300, 0, 300, 65,  color=(166, 28, 20), hover_color=(166, 28, 20),
                          function=run_game, state='setting'))
    buttons.append(Button(screen, width -300, 0, 300, 50, text = 'RUN', color=(235, 64, 52), hover_color=(135, 21, 14),
                          function = run_game, state= 'setting'))
    buttons.append(
        Button(screen, width - 300, 0, 300, 65, color=(161, 14, 5), hover_color=(161, 14, 5),
               function=pause_game, state='running'))
    buttons.append(Button(screen, width -300, 0, 300, 50, text = 'PAUSE', color=(240, 38, 26), hover_color=(161, 14, 5),
                          function= pause_game, state = 'running'))
    buttons.append(
        Button(screen, width - 300, 170, 300, 70, color=(161, 14, 5), hover_color=(161, 14, 5),
               function=reset_game, state='paused', ))
    buttons.append(Button(screen, width -300, 170, 300, 50, text = 'RESET', color=(252, 8, 8), hover_color=(161, 14, 5),
                          function= reset_game, state= 'paused'))
    buttons.append(
        Button(screen, width - 300, 100, 300, 70, color=(28, 92, 4), hover_color=(28, 92, 4),
               function=run_game, state='paused'))
    buttons.append(Button(screen, width - 300, 100, 300, 50, text='RESUME', color=(28,111,51), hover_color=(28, 92, 4),
               function=run_game, state='paused', font_name = 'MinecraftRegular-Bmg3.otf'))
    buttons.append(
        Button(screen, width - 300, 435, 300, 65, color=(135, 71, 30), hover_color=(135, 71, 30)))
    buttons.append(
        Button(screen, width - 300, 435, 300, 50, text='Walker', color=(240, 94, 10), hover_color=(117, 58, 20),
               function = walker_on, font_name = 'MinecraftRegular-Bmg3.otf' ))
    buttons.append(
        Button(screen, width - 300, 370, 300, 65, color=(135, 71, 30), hover_color=(135, 71, 30)))
    buttons.append(
        Button(screen, width - 300, 370, 300, 50, text='Default', color=(240, 94, 10), hover_color=(117, 58, 20),
               function= normal_on))
    buttons.append(
        Button(screen, width - 300, 500, 300, 65, color=(135, 71, 30), hover_color=(135, 71, 30)))
    buttons.append(
        Button(screen, width - 300, 500, 300, 50, text='Boom', color=(240, 94, 10), hover_color=(117, 58, 20),
               function=boom_on))
    buttons.append(
        Button(screen, width - 300, 565, 300, 65, color=(135, 71, 30), hover_color=(135, 71, 30)))
    buttons.append(
        Button(screen, width - 300, 565, 300, 50, text='Bird', color=(240, 94, 10), hover_color=(117, 58, 20),
               function= bird_on))
    buttons.append(
        Button(screen, width - 300, 630, 300, 65, color=(135, 71, 30), hover_color=(135, 71, 30)))
    buttons.append(
        Button(screen, width - 300, 630, 300, 50, text='Figure X', color=(240, 94, 10), hover_color=(117, 58, 20),
               function= x_on))
    buttons.append(
        Button(screen, width - 300, 695, 300, 70, color=(135, 71, 30), hover_color=(135, 71, 30)))
    buttons.append(
        Button(screen, width - 300, 695, 300, 50, text='Transformers', color=(240, 94, 10), hover_color=(117, 58, 20),
               function=transformer_on))

    buttons.append(Button(screen, width - 290, 200, 50, 65, color=(161, 14, 5), hover_color=(161, 14, 5),
                          state='running'))
    buttons.append(Button(screen, width - 290, 200, 50, 50, text='-', color=(240, 38, 26), hover_color=(161, 14, 5),
                           state='running', function= minus))
    buttons.append(Button(screen, width - 60, 200, 50, 65, color=(161, 14, 5), hover_color=(161, 14, 5),
                          state='running'))
    buttons.append(Button(screen, width - 60, 200, 50, 50, text='+', color=(240, 38, 26), hover_color=(161, 14, 5),
                           state='running', function= plus))
    return buttons

#---------------------------------------------------------Running------------------------------------------------------------
def running_get_events():
    global run
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            menu.wybor_levela()
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
        if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
            Cell.walker = True
def running_upadte():
    game_window.update()
    for button in buttons:
        button.update(mouse_pos, game_state= state)
    if frame_count%(fps_in_game//10) == 0:
        game_window.evaluate()


def running_draw():
    screen.fill((89, 86, 84))
    for button in buttons:
        button.draw()
    game_window.draw()
    pygame.draw.line(screen, black, (1201, 0), (1201, 800), 3 )
    pygame.draw.line(screen, black, (1201, 300), (width, 300), 3)


#---------------------------------------------------------Paused------------------------------------------------------------
def paused_get_events():
    global run
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            menu.wybor_levela()
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
        if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
            Cell.walker = True
def paused_upadte():
    game_window.update()
    for button in buttons:
        button.update(mouse_pos, game_state= state)


def paused_draw():
    screen.fill((89, 86, 84))
    for button in buttons:
        button.draw()
    game_window.draw()
    pygame.draw.line(screen, black, (1201, 0), (1201, 800), 3 )
    pygame.draw.line(screen, black, (1201, 300), (width, 300), 3)
#---------------------------------------------------------------------------------------------------------------------------

def run_game():
    global state
    state = 'running'
def pause_game():
    global state
    state = 'paused'
def reset_game():
    global state
    game_window.reset_grid()
    state = 'setting'



buttons = make_buttons()
state = 'setting'
frame_count = 0
font = pygame.font.SysFont('GalacticaGrid.ttf', 50)
font1 = pygame.font.SysFont('GalacticaGrid.ttf', 30)
text = font.render("Ready samples", False, black)
text1 = font1.render("Game speed [FPS]", False, black)
text2 = font.render(f'{clock_ticks}', False, black)
text3 = font.render("MAX", False, black)
text4 = font.render("MIN", False, black)
clock = pygame.time.Clock()
menu.wybor_levela()
while run:
    mouse_pos = pygame.mouse.get_pos()
    if state == 'setting':
        get_events()
        upadte()
        draw()
    if state == 'running':
        text2 = font.render(f'{clock_ticks}', False, black)
        running_get_events()
        running_upadte()
        running_draw()
        clock.tick(clock_ticks)
        if clock_ticks == 60:
            screen.blit(text3,(1305, 240) )
        if clock_ticks == 10:
            screen.blit(text4,(1310, 240) )
        screen.blit(text1, (1265, 150))
        screen.blit(text2, (1325, 210))
    if state == 'paused':
        paused_get_events()
        paused_upadte()
        paused_draw()
    screen.blit(text, (1220, 310))
    pygame.display.update()
pygame.quit()