from scene import *
from napisy import Napisy

class EndScene(Scene):
    def __init__(self, screen,scene_man):
        super().__init__(screen)

        self.scene_man = scene_man
        self.buttongame = Buttons((125,600),"grafika/przyciskgame.png","grafika/przyciskgamealt.png",self.screen)
        self.buttonmenu = Buttons((375, 600), "grafika/przyciskmenu.png", "grafika/przyciskmenualt.png", self.screen)
        self.napiswynik = Napisy(f"koniec gry uzyskany przez ciebie wynik to: 0", 50, (255, 255, 255),(50, 100))
        self.sky = pygame.image.load("grafika/sky.png")
        self.sky_rect = self.sky.get_rect(topleft=(0, 0))
        self.ground = pygame.image.load("grafika/ground.png")
        self.ground_rect = self.ground.get_rect(bottomleft=(0, 700))
        self.graczob = pygame.image.load("grafika/player3.png")
        self.graczob_rect = self.graczob.get_rect(midbottom=(250, 500))
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and self.buttongame.button_rect.collidepoint(pygame.mouse.get_pos()):
                self.scene_man.game_scene.new_game()
                self.scene_man.current_scene = self.scene_man.game_scene

            if event.type == pygame.MOUSEBUTTONDOWN and self.buttonmenu.button_rect.collidepoint(pygame.mouse.get_pos()):
                self.scene_man.game_scene.new_game()
                self.scene_man.current_scene = self.scene_man.menu_scene
    def update(self):
        # Aktualizacja stanu gry specyficz
        self.score = self.scene_man.game_scene.iloscmonet
        self.scene_man.game_scene.licznikmonet.clear()
        self.napiswynik = Napisy(f"koniec gry uzyskany przez ciebie wynik to:{self.score}",30,(0,0,255),(50,50))
        self.buttonmenu.podswietlenie()
        self.buttongame.podswietlenie()
    def render(self):

        self.screen.blit(self.ground,self.ground_rect)
        self.screen.blit(self.sky, self.sky_rect)
        self.screen.blit(self.graczob, self.graczob_rect)
        self.buttongame.display()
        self.buttonmenu.display()
        self.screen.blit(self.napiswynik.name,self.napiswynik.rect)


