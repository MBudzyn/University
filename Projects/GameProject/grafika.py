import pygame

class Grafika:
    def __init__(self, wsps,grafika):
        self.image = pygame.image.load(grafika).convert_alpha()
        self.rect = self.image.get_rect(center=wsps)
