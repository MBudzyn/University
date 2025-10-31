import pygame.mouse

import globalne
from scene import *
from buttons import Buttons
from bomby import Bomby

class GameSettings(Scene):
    def __init__(self, screen,scene_man):
        super().__init__(screen)

        self.scene_man = scene_man
        self.tlo = pygame.image.load("grafika/ekranopcje3.png")
        self.tlo_rect = self.tlo.get_rect(topleft = (0,0))
        self.buttoneasy = Buttons((110,110),"grafika/easyb3.png","grafika/easybalt3.png",self.screen)
        self.buttonmedium= Buttons((385, 115), "grafika/mediumb3.png", "grafika/mediumbalt3.png", self.screen)
        self.buttonhard = Buttons((330, 360), "grafika/hardb3.png", "grafika/hardbalt3.png", self.screen)
        self.nacisniety = "easy"
        self.buttoneasy.changetoalt()
        self.buttonbackmenu = Buttons((110, 440), "grafika/przyciskmenu2.png", "grafika/przyciskmenualt2.png", self.screen)
        self.buttonbackgame = Buttons((290, 580), "grafika/przyciskgame2.png", "grafika/przyciskgamealt2.png", self.screen)
    def handle_events(self):
        # Obsługa zdarzeń specyficzna dla GameScene
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.mousebuttonlevelcontrol()
            if event.type == pygame.MOUSEBUTTONDOWN and self.buttonbackmenu.button_rect.collidepoint(pygame.mouse.get_pos()):
                self.scene_man.current_scene = self.scene_man.menu_scene
            if event.type == pygame.MOUSEBUTTONDOWN and self.buttonbackgame.button_rect.collidepoint(pygame.mouse.get_pos()):
                self.scene_man.current_scene = self.scene_man.game_scene
    def zmientrudnosc(self,trudnoscstr):

        if trudnoscstr == "hard":
            globalne.zmianabombabiala = 6
            globalne.zmianabombaczarna = 8
            globalne.zmianabombaczerwona = 10
            self.scene_man.game_scene.bomby.empty()
            self.scene_man.game_scene.bomby.add(Bomby("biala"), Bomby("czerwona"))
        if trudnoscstr == "medium":
            globalne.zmianabombabiala = 5
            globalne.zmianabombaczarna = 6
            globalne.zmianabombaczerwona = 8

            self.scene_man.game_scene.bomby.empty()
            self.scene_man.game_scene.bomby.add(Bomby("biala"), Bomby("czerwona"))
        if trudnoscstr == "easy":

            globalne.zmianabombabiala = 4
            globalne.zmianabombaczarna = 5
            globalne.zmianabombaczerwona = 6
            self.scene_man.game_scene.bomby.empty()
            self.scene_man.game_scene.bomby.add(Bomby("biala"), Bomby("czerwona"))
    def mousebuttonlevelcontrol(self):

        if self.buttonhard.button_rect.collidepoint(pygame.mouse.get_pos()):
            self.zmientrudnosc("hard")
            self.buttonhard.changetoalt()
            self.buttoneasy.chagnetonormal()
            self.buttonmedium.chagnetonormal()

        if self.buttonmedium.button_rect.collidepoint(pygame.mouse.get_pos()):
            self.zmientrudnosc("medium")
            self.buttonmedium.changetoalt()
            self.buttoneasy.chagnetonormal()
            self.buttonhard.chagnetonormal()

        if self.buttoneasy.button_rect.collidepoint(pygame.mouse.get_pos()):
            self.zmientrudnosc("easy")
            self.buttoneasy.changetoalt()
            self.buttonhard.chagnetonormal()
            self.buttonmedium.chagnetonormal()
    def update(self):
        self.buttonbackgame.podswietlenie()
        self.buttonbackmenu.podswietlenie()
    def render(self):
        self.screen.blit(self.tlo,self.tlo_rect)
        self.screen.blit(self.buttoneasy.button, self.buttoneasy.button_rect)
        self.screen.blit(self.buttonmedium.button, self.buttonmedium.button_rect)
        self.screen.blit(self.buttonhard.button, self.buttonhard.button_rect)
        self.screen.blit(self.buttonbackmenu.button, self.buttonbackmenu.button_rect)
        self.screen.blit(self.buttonbackgame.button, self.buttonbackgame.button_rect)
