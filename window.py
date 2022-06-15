import copy
import os
import pygame
from cell import *
vec = pygame.math.Vector2
import copy

class Game_window:
    def __init__(self, screen, x, y):
        self.pos = vec(x,y)
        self.screen = screen
        self.width, self.height = 1200, 1000
        self.image = pygame.Surface((self.width, self.height))
        self.rect = self.image.get_rect()
        self.rows =60
        self.cols = 60
        self.grafika = pygame.transform.scale(pygame.image.load(os.path.join("GoL", "cell_alive_01.png")),(19,19))
        self.grafika1 = pygame.transform.scale(pygame.image.load(os.path.join("GoL", "cell_alive_02.png")), (19, 19))
        self.grafika2 = pygame.transform.scale(pygame.image.load(os.path.join("GoL", "cell_alive_03.png")), (19, 19))
        self.grafika3 = pygame.transform.scale(pygame.image.load(os.path.join("GoL", "cell_alive_04.png")), (19, 19))
        self.grafika4 = pygame.transform.scale(pygame.image.load(os.path.join("GoL", "cell_dead_1.png")), (19, 19))
        self.grafiki_list =[self.grafika, self.grafika1, self.grafika2, self.grafika3]
        self.grid = [[Cell(self.image, x, y, self.grafika, self.grafiki_list) for x in range(self.cols + 6)] for y in range(self.rows + 6)]
        for row in self.grid:
            for cell in row:
                cell.get_neigbours(self.grid)

    def update(self):
        self.rect.topleft = self.pos
        for row in  self.grid:
            for cell in row:
                cell.update()

    def draw(self):
        self.image.fill((102, 102, 102))
        for row in  self.grid:
            for cell in row:
                cell.draw()
        self.screen.blit(self.image, (self.pos.x, self.pos.y))

    def reset_grid(self):
        self.grid = [[Cell(self.image, x, y,self.grafika, self.grafiki_list) for x in range(self.cols)] for y in range(self.rows)]
        for row in self.grid:
            for cell in row:
                cell.get_neigbours(self.grid)

    def evaluate(self):
        new_grid = copy.copy(self.grid)

        for row in self.grid:
            for cell in row:
                cell.live_neighbours()

        for yidx, row in enumerate(self.grid):
            for xidx, cell in enumerate(row):
                if cell.alive:
                    if cell.alive_neighbours == 2:
                        new_grid[yidx][xidx].alive = True
                    if cell.alive_neighbours < 2:
                        new_grid[yidx][xidx].alive = False
                    if cell.alive_neighbours > 3:
                        new_grid[yidx][xidx].alive = False
                else:
                    if cell.alive_neighbours == 3:
                        new_grid[yidx][xidx].alive = True

        self.grid = new_grid



