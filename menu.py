import pygame
import os
import time
from random import randint

class Gra(object):
    def __init__(self):
        pygame.init()

#=======================Parametry=======================================================#

        self.WIDTH, self.HEIGHT = 1500, 800
        self.WIN = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.FPS = 20
        self.run = True
        self.opoznienie = pygame.time.Clock()
        self.uruchamiasz_po_raz_pierwszy = True
        self.czy_nie_byles_jeszcze_w_menu = True

#=======================Animacja przycisków=============================================#

        self.pierwszy = 0
        self.pierwszy_ostatni = -2
        self.drugi = 0
        self.drugi_ostatni = -2

        pygame.font.init()
        self.NAZWA_GRY = pygame.font.Font("GalacticaGrid.ttf", 80, )
        self.mniejsza_czcionka = pygame.font.Font("GalacticaGrid.ttf", 15, )

#=========================Wygląd pauzy=====================================================#

        self.nazwa_gry = self.NAZWA_GRY.render('GAME OF LIFE', True, (0, 0, 0))
        self.square_level_name = self.NAZWA_GRY.render('SQUARE LEVEL', True, (0, 0, 0))
        self.hex_level_name = self.NAZWA_GRY.render('HEXAGON LEVEL', True, (0, 0, 0))
        self.tekst_w_how_to_play1 = self.mniejsza_czcionka.render("How to play?", True, (0, 0, 0))
        self.tekst_w_how_to_play2 = self.mniejsza_czcionka.render(
            "You're a scientist who has discovered a new spice of cells.", True, (0, 0, 0))
        self.tekst_w_how_to_play3 = self.mniejsza_czcionka.render(
            "After a long time, that you have spent on researches, finally you began to", True, (0, 0, 0))
        self.tekst_w_how_to_play4 = self.mniejsza_czcionka.render("see some dependences. Here they are:", True,
                                                                  (0, 0, 0))
        self.tekst_w_how_to_play5 = self.mniejsza_czcionka.render(
            "-the cells that have less than two or more than three neighbours die (appropriately from loneliness and overpopulation)",
            True, (0, 0, 0))
        self.tekst_w_how_to_play6 = self.mniejsza_czcionka.render(
            "-The cells that have 3 or 2 neighborus live happy life", True, (0, 0, 0))
        self.tekst_w_how_to_play7 = self.mniejsza_czcionka.render(
            "How can you use this informations? Maybe there are stable structures of cells, maybe the cells could create a relevant good",
            True, (0, 0, 0))
        self.tekst_w_how_to_play8 = self.mniejsza_czcionka.render(
            "working society? That's your duty to find it out. Based on this rules we can call this project", True,
            (0, 0, 0))
        self.tekst_w_how_to_play9 = self.mniejsza_czcionka.render('"Game of Life"', True, (0, 0, 0))

        # =========================Menu Grafiki=====================================================#

        self.pauza = pygame.transform.scale(pygame.image.load(os.path.join("Grafika", "lepsze_menu.png")),
                                            (self.WIDTH, self.HEIGHT))
        self.tlo_how_to_play = pygame.transform.scale(pygame.image.load(os.path.join("Grafika", "how_to_play_2.png")),
                                                      (self.WIDTH, self.HEIGHT))
        self.ekran_wlaczania_gry = pygame.transform.scale(
            pygame.image.load(os.path.join("Grafika", "ekran_wlaczania.png")),
            (self.WIDTH, self.HEIGHT))
        self.wybor_lvla = pygame.transform.scale(
            pygame.image.load(os.path.join("Grafika", "wybor_lvla.png")),
            (self.WIDTH, self.HEIGHT))
        self.przycisk_start = pygame.Rect(585, 420, 290, 95)
        self.przycisk_how_to_play = pygame.Rect(580, 510, 300, 100)
        self.przycisk_quit = pygame.Rect(580, 610, 310, 100)
        self.przycisk_w_wyborze_lvla_lewy = pygame.Rect(200, 100, 400, 300)

        def wlaczanie_gry_intro(self):
            self.WIN.blit(self.ekran_wlaczania_gry, (0, 0))
            pygame.display.update()
            time.sleep(5.2)

        def menu(self):

            x = randint(0, 3)

            playlist = list()
            playlist.append("Title_music.ogg")
            playlist.append("Title_music2.ogg")
            playlist.append("Title_music3.ogg")
            playlist.append("Title_music4.ogg")
            pygame.mixer.music.load(playlist.pop(x))
            pygame.mixer.music.set_endevent(pygame.USEREVENT)
            pygame.mixer.music.play(-1)

            if self.uruchamiasz_po_raz_pierwszy:
                self.wlaczanie_gry_intro()
                self.uruchamiasz_po_raz_pierwszy = False

            click = False
            while self.run:
                self.opoznienie.tick(self.FPS)
                mx, my = pygame.mouse.get_pos()
                self.WIN.blit(self.pauza, (0, 0))

                # Najnowsza zmiana.
                pygame.draw.rect(self.WIN, (0, 0, 0), self.przycisk_start, 5)
                pygame.draw.rect(self.WIN, (0, 0, 0), self.przycisk_how_to_play, 5)
                pygame.draw.rect(self.WIN, (0, 0, 0), self.przycisk_quit, 5)

                # Start in menu
                if self.przycisk_start.collidepoint(mx, my):
                    if click:
                        effect = pygame.mixer.Sound('click_sound.wav')
                        effect.play()
                        return

                # Quit from menu
                if self.przycisk_quit.collidepoint(mx, my):
                    if click:
                        pygame.quit()

                # How to play
                if self.przycisk_how_to_play.collidepoint(mx, my):
                    if click:
                        self.how_to_play()

                self.WIN.blit(self.nazwa_gry, (500, 35))

                click = False

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.run = False
                        pygame.quit()

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1:
                            click = True

                    if event.type == pygame.USEREVENT:
                        if len(playlist) > 0:
                            pygame.mixer.music.queue(playlist.pop(x))

                pygame.display.update()