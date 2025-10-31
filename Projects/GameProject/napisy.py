import pygame
class Napisy:
    def __init__(self, nazwa, rozmiar, RGB, wspmf):

        font = pygame.font.Font('Pixeltype.ttf', rozmiar)
        self.nazwa = nazwa
        self.name = font.render(self.nazwa, False, RGB)
        self.rect = self.name.get_rect(midleft=wspmf)

