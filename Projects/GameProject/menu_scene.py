from scene import *

class MenuScene(Scene):
    def __init__(self, screen,scene_man):
        super().__init__(screen)
        # Dodatkowa inicjalizacja specyficzna dla MenuScene
        self.sky = pygame.image.load("grafika/sky.png")
        self.sky_rect = self.sky.get_rect(topleft=(0, 0))
        self.ground = pygame.image.load("grafika/ground.png")
        self.ground_rect = self.ground.get_rect(bottomleft=(0, 700))
        self.scene_man = scene_man
        self.button1 = Buttons((125, 600), "grafika/przyciskgame.png", "grafika/przyciskgamealt.png", self.screen)
        self.button2 = Buttons((375, 600), "grafika/przyciskoptions.png", "grafika/przyciskoptionsalt.png", self.screen)
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and self.button1.button_rect.collidepoint(pygame.mouse.get_pos()):
                self.scene_man.current_scene = self.scene_man.game_scene
            if event.type == pygame.MOUSEBUTTONDOWN and self.button2.button_rect.collidepoint(pygame.mouse.get_pos()):
                self.scene_man.current_scene = self.scene_man.game_settings
    def update(self):
        self.button2.podswietlenie()
        self.button1.podswietlenie()
    def render(self):
        self.screen.blit(self.ground,self.ground_rect)
        self.screen.blit(self.sky, self.sky_rect)
        self.button1.display()
        self.button2.display()
