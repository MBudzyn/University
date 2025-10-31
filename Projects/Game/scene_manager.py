import pygame
from game_scene import GameScene
from menu_scene import MenuScene
from game_settings import GameSettings
from end_scene import EndScene
from globalne import *


class SceneManager:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.clock = pygame.time.Clock()

        self.game_scene = GameScene(self.screen,self)
        self.menu_scene = MenuScene(self.screen,self)
        self.game_settings = GameSettings(self.screen, self)
        self.end_scene = EndScene(self.screen,self)
        self.current_scene = self.menu_scene
    def handle_events(self):
        self.current_scene.handle_events()
    def update(self):
        self.current_scene.update()
    def render(self):
        self.current_scene.render()

        pygame.display.flip()
        self.clock.tick(60)