#chuj
# Kocham piwko
# klasa obsługująca przzycisk

import pygame
vec =pygame.math.Vector2

class Button:
    # inicjalizacja zmiennych
    def __init__(self, surface, x, y, width, height, state = '', function = 0, color = (255, 255, 255), hover_color = (255, 255, 255),
                 border = True, border_width = 2, border_color = (0, 0, 0), text = '', font_name = 'arial', text_size = 20,
                 text_color = (0, 0, 0), bold_text = False):
        self.x = x
        self.y = y
        self.pos = vec(x, y)
        self.width = width
        self.height = height
        self.surface = surface
        self.image = pygame.Surface((width, height))
        self.rect = self.image.get_rect()
        self.rect.topleft = self.pos
        self.state = state
        self.function = function
        self.color = color
        self.hover_color = hover_color
        self.border = border
        self.border_width = border_width
        self.border_color = border_color
        self.text = text
        self.font_name = font_name
        self.text_size = text_size
        self.text_color = text_color
        self.bold_text = bold_text
        self.hovered = False
        self.showing = True
# ---------------------------------------------------------------------------------------------------------------------
    #funckja wywołująca teskt na przyciku
    def show_text(self):
        font = pygame.font.SysFont(self.font_name, self.text_size, bold = self.bold_text)
        text = font.render(self.text, False, self.text_color)
        size = text.get_size()
        x, y = self.width//2-(size[0]//2), self.height//2-(size[1]//2)
        pos = vec(x,y)
        self.image.blit(text, pos)
# ---------------------------------------------------------------------------------------------------------------------
    #funckja odpowiadająca za zmiany wyglądu przycisku
    def update(self, pos, game_state = ''):
        if self.mouse_hovering(pos):
            self.hovered = True
        else:
            self.hovered = False
        if self.state == '' or game_state == '':
            self.showing = True
        else:
            if self.state == game_state:
                self.showing = True
            else:
                self.showing = False
# ---------------------------------------------------------------------------------------------------------------------
