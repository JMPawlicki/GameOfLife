import random
import os
import pygame
import random

class Cell:
    def __init__(self, surface, grid_x, grid_y, grafika, grafiki_list):
        self.alive = False
        self.surface = surface
        self.grid_x = grid_x
        self.grid_y = grid_y
        self.image = pygame.Surface((20,20))
        self.rect = self.image.get_rect()
        self.neighbours = []
        self.alive_neighbours = 0
        self.grafika = grafika
        self.grafiki_list = grafiki_list


    def update(self):
        self.rect.topleft = (self.grid_x * 20, self.grid_y * 20)

    def draw(self):
        if self.alive:
            self.image.blit(random.choice(self.grafiki_list), (0,0))
        else:
            self.image.fill((70, 70, 70))
            pygame.draw.rect(self.image, (50, 50, 50), (0, 0, 19, 19))
        self.surface.blit(self.image, (self.grid_x * 20, self.grid_y * 20))


    def get_neigbours(self, grid):
        neighbour_list = [[1, 1], [-1, -1], [-1, 1], [1, -1], [0, -1], [0, 1], [1, 0], [-1, 0]]
        for neighbour in neighbour_list:
            neighbour[0] += self.grid_x
            neighbour[1] += self.grid_y
        for neighbour in neighbour_list:
            if neighbour[0] < 0:
                neighbour[0] += 60
            if neighbour[1] < 0:
                neighbour[1] += 60
            if neighbour[0] > 59:
                neighbour[0] -= 60
            if neighbour[1] > 59:
                neighbour[1] -= 60
        for neighbour in neighbour_list:
            try:
                self.neighbours.append(grid[neighbour[1]][neighbour[0]])
            except:
                print(neighbour)

    def live_neighbours(self):
        count = 0
        for neighbour in self.neighbours:
            if neighbour.alive:
                count += 1

        self.alive_neighbours = count







