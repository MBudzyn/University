import pygame
from random import randint,choice
import globalne
from globalne import *
class Bomby(pygame.sprite.Sprite):
    def __init__(self, type):
        super().__init__()

        if type == 'biala':
            self.image = pygame.image.load('grafika/bombabiala.png').convert_alpha()
            zmiana = globalne.zmianabombabiala
            obrazenia = 3

        elif type == "czarna":
            self.image = pygame.image.load('grafika/bombaczarna.png').convert_alpha()
            zmiana = globalne.zmianabombaczarna
            obrazenia =2
        elif type == "czerwona":
            self.image = pygame.image.load('grafika/bombaczerwona.png').convert_alpha()
            zmiana = globalne.zmianabombaczerwona
            obrazenia = 1


        self.rect = self.image.get_rect(midbottom= (randint(20,480), -randint(20,300)))
        self.zmiana = zmiana
        self.obrazenia = obrazenia
    def update(self):

        self.rect.y += self.zmiana
        if self.rect.y > 600:
            del self




