import pygame
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('grafika/player2.png').convert_alpha()

        self.zmiana = 7
        self.rect = self.image.get_rect(midbottom=(250, 500))
    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT] and self.rect.right < 500:
            self.rect.x += self.zmiana
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.zmiana

    def update(self):
        self.player_input()

