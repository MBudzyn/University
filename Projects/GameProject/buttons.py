
import pygame
class Buttons:
    def __init__(self, wspdanesrodka, grafika, grafikaalt, screen):

        self.screen = screen
        self.wspdanesrodka = wspdanesrodka
        self.grafika = pygame.image.load(grafika)
        self.grafikaalt = pygame.image.load(grafikaalt)
        self.button = self.grafika
        self.button_rect = self.button.get_rect(center = self.wspdanesrodka)

    def display(self):
        self.screen.blit(self.button,self.button_rect)
    def podswietlenie(self):
        if self.button_rect.collidepoint(pygame.mouse.get_pos()):
            self.changetoalt()
        else: self.chagnetonormal()
    def changetoalt(self):
        self.button = self.grafikaalt
    def chagnetonormal(self):
        self.button = self.grafika