import pygame
from random import randint
class Monety(pygame.sprite.Sprite):
    def __init__(self, type):
        super().__init__()

        if type == 'zloto':
            self.image = pygame.image.load('grafika/moneta33.png').convert_alpha()
            zmiana = 6
            punkty = 3

        elif type == "srebro":
            self.image = pygame.image.load('grafika/moneta22.png').convert_alpha()
            zmiana = 5
            punkty =2
        elif type == "braz":
            self.image = pygame.image.load('grafika/moneta11.png').convert_alpha()
            zmiana = 4
            punkty = 1


        self.rect = self.image.get_rect(midbottom= (randint(20,480), -randint(20,300)))
        self.zmiana = zmiana
        self.punkty = punkty
    def update(self):

        self.rect.y += self.zmiana
        self.move_up()
    def move_up(self):
        if self.rect.top >= 800:
            self.rect.y = -randint(20,400)
            self.rect.x = randint(0,500)
