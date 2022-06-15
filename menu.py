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

        """    
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
        """
        # =========================Menu Grafiki=====================================================#

        self.pauza = pygame.transform.scale(pygame.image.load(os.path.join("Grafika", "gol_menu.png")),
                                            (self.WIDTH, self.HEIGHT))
        self.tlo_how_to_play = pygame.transform.scale(pygame.image.load(os.path.join("Grafika", "gol_help.png")),
                                                      (self.WIDTH, self.HEIGHT))
        self.ekran_wlaczania_gry = pygame.transform.scale(
            pygame.image.load(os.path.join("Grafika", "ekran_wlaczania.png")),
            (self.WIDTH, self.HEIGHT))
        self.wybor_lvla = pygame.transform.scale(
            pygame.image.load(os.path.join("Grafika", "gol_play.png")),
            (self.WIDTH, self.HEIGHT))
        self.przycisk_play_obrazek = pygame.transform.scale(
            pygame.image.load(os.path.join("Grafika", "gol_menu_play.png")),
            (self.WIDTH, self.HEIGHT))
        self.przycisk_help_obrazek = pygame.transform.scale(
            pygame.image.load(os.path.join("Grafika", "gol_menu_help.png")),
            (self.WIDTH, self.HEIGHT))
        self.przycisk_quit_obrazek = pygame.transform.scale(
            pygame.image.load(os.path.join("Grafika", "gol_menu_quit.png")),
            (self.WIDTH, self.HEIGHT))

        self.przycisk_start = pygame.Rect(360, 450, 420, 80)
        self.przycisk_how_to_play = pygame.Rect(360, 540, 420, 80)
        self.przycisk_quit = pygame.Rect(360, 630, 420, 80)
        self.przycisk_w_wyborze_lvla_lewy = pygame.Rect(260, 330, 440, 400)

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


            # Start in menu
            if self.przycisk_start.collidepoint(mx, my):
                self.WIN.blit(self.przycisk_play_obrazek, (0, 0))
                if click:
                    effect = pygame.mixer.Sound('click_sound.wav')
                    effect.play()
                    return

            # Quit from menu
            if self.przycisk_quit.collidepoint(mx, my):
                self.WIN.blit(self.przycisk_quit_obrazek, (0, 0))
                if click:
                    pygame.quit()

            # How to play
            if self.przycisk_how_to_play.collidepoint(mx, my):
                self.WIN.blit(self.przycisk_help_obrazek, (0, 0))
                if click:
                    self.how_to_play()

            #self.WIN.blit(self.nazwa_gry, (500, 35))

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

    def how_to_play(self):
        jestes_w_how_to_play = True

        while jestes_w_how_to_play:
            self.WIN.blit(self.tlo_how_to_play, (0, 0))
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    jestes_w_how_to_play = False
                    pygame.quit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    return

    def wybor_levela(self):
        if self.czy_nie_byles_jeszcze_w_menu:
            self.czy_nie_byles_jeszcze_w_menu = False
            self.menu()
        click = False
        nie_wiem_co_pisze = True
        while nie_wiem_co_pisze:
            # Stara część kodu (może się przydać jeszcze kiedyś)
            """
            self.square_game_thumbnail = pygame.transform.scale(
                pygame.image.load(os.path.join("Grafika", "square_game.png")),
                (500 + self.pierwszy, 200 + self.pierwszy))
            self.hex_game_thumbnail = pygame.transform.scale(
                pygame.image.load(os.path.join("Grafika", "square_game.png")),
                (500 + self.drugi, 200 + self.drugi))
            """
            self.opoznienie.tick(self.FPS)
            self.WIN.blit(self.wybor_lvla, (0, 0))
            mx, my = pygame.mouse.get_pos()
            square_map = pygame.Rect(100 - self.pierwszy // 2, 200 - self.pierwszy // 2, 500 + self.pierwszy,
                                     200 + self.pierwszy)
            hexagon_map = pygame.Rect(800 - self.drugi // 2, 200 - self.drugi // 2, 500 + self.drugi,
                                      200 + self.drugi)
            # self.WIN.blit(self.square_game_thumbnail, (100 - self.pierwszy // 2, 200 - self.pierwszy // 2))
            # self.WIN.blit(self.hex_game_thumbnail, (800 - self.drugi // 2, 200 - self.drugi // 2))
            # self.WIN.blit(self.square_level_name, (100, 100))
            # self.WIN.blit(self.hex_level_name, (800, 100))
            pygame.draw.rect(self.WIN, (0, 0, 0), self.przycisk_w_wyborze_lvla_lewy, 5)

            if self.przycisk_w_wyborze_lvla_lewy.collidepoint(mx, my):
                if self.pierwszy > 10:
                    self.pierwszy = 8
                if self.pierwszy < -12:
                    self.pierwszy = -10
                if -12 <= self.pierwszy <= 10:
                    if self.pierwszy_ostatni < self.pierwszy:
                        self.pierwszy += 2
                        self.pierwszy_ostatni = self.pierwszy - 1
                    if self.pierwszy_ostatni > self.pierwszy:
                        self.pierwszy -= 2
                        self.pierwszy_ostatni = self.pierwszy + 1
                if click:
                    pygame.mixer.music.pause()
                    effect = pygame.mixer.Sound('click_sound.wav')
                    effect.play()
                    # Przejście do mapy kwadratowej.
                    nie_wiem_co_pisze = False
                    return
            else:
                self.pierwszy = 0
                self.pierwszy_ostatni = -2

            if hexagon_map.collidepoint(mx, my):
                if self.drugi > 10:
                    self.drugi = 8
                if self.drugi < -12:
                    self.drugi = -10
                if -12 <= self.drugi <= 10:
                    if self.drugi_ostatni < self.drugi:
                        self.drugi += 2
                        self.drugi_ostatni = self.drugi - 1
                    if self.drugi_ostatni > self.drugi:
                        self.drugi -= 2
                        self.drugi_ostatni = self.drugi + 1

                if click:
                    pygame.mixer.music.pause()
                    effect = pygame.mixer.Sound('click_sound.wav')
                    effect.play()
                    # Tu bedzie przejście do mapy Ul.
                    return
            else:
                self.drugi = 0
                self.drugi_ostatni = -2

            click = False

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    self.menu()
                if event.type == pygame.QUIT:
                    nie_wiem_co_pisze = False
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True

            pygame.display.update()
