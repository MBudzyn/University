
from scene import *
from player import Player
from monety import Monety
from random import choice
from napisy import Napisy
from bomby import Bomby
from grafika import Grafika
class GameScene(Scene):
    def __init__(self, screen,scene_man):
        super().__init__(screen)
        # Dodatkowa inicjalizacja specyficzna dla GameScene
        self.scene_man = scene_man
        self.sky = pygame.image.load("grafika/sky.png")
        self.sky_rect = self.sky.get_rect(topleft= (0,0))
        self.ground = pygame.image.load("grafika/ground.png")
        self.ground_rect = self.ground.get_rect(bottomleft=(0, 700))
        self.player = pygame.sprite.GroupSingle()
        self.player.add(Player())
        self.score = 0
        self.monety = pygame.sprite.Group()
        self.monety.add(Monety("braz"),Monety("zloto"),Monety("srebro"))
        self.punkty = Napisy(f"Your Score: {self.score}",60,(0,0,0),(25,100))
        self.licznikobrazen = Napisy(f"Your damage: {self.score} ", 60, (0, 0, 0), (25, 100))
        self.font = pygame.font.Font('Pixeltype.ttf', 50)
        self.bomby = pygame.sprite.Group()
        self.bomby.add(Bomby("biala"),Bomby("czerwona"))
        self.obrazenia = 0
        self.zycia = []
        self.licznikmonet = []
        self.iloscmonet = 0
        self.pozostalezycia = 9
        self.spawntimer = pygame.USEREVENT + 1
        pygame.time.set_timer(self.spawntimer, 500)
        self.table_filling()
    def table_filling(self):
        for i in range(9):
            self.zycia.append(Grafika((40+ i*50, 40),'grafika/zycie2.png'))
        for i in range(116):
            if i<29:
                self.licznikmonet.append(Grafika((40 + i * 15, 540), 'grafika/monetalicznik2.png'))
            elif i <58:
                self.licznikmonet.append(Grafika((40 + (i-29) * 15, 564), 'grafika/monetalicznik2.png'))
            elif i < 87:
                self.licznikmonet.append(Grafika((40 + (i - 58) * 15, 588), 'grafika/monetalicznik2.png'))
            elif i < 116:
                self.licznikmonet.append(Grafika((40 + (i - 87) * 15, 612), 'grafika/monetalicznik2.png'))
    def collision_spritemonety(self):
        blocks_hit_list = pygame.sprite.spritecollide(self.player.sprite, self.monety, True)
        for monety in blocks_hit_list:
            self.iloscmonet += monety.punkty
            self.monety.add(Monety(choice(["braz","srebro","zloto"])))
    def collision_spritebomby(self):
        blocks_hit_list = pygame.sprite.spritecollide(self.player.sprite, self.bomby, True)
        for bomby in blocks_hit_list:
            self.pozostalezycia -= bomby.obrazenia
    def game_end(self):
        if self.pozostalezycia <=0:
            return True
        else: return False
    def handle_events(self):


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == self.spawntimer:
                self.bomby.add(Bomby(choice(["biala", "czarna", "czerwona"])))
    def new_game(self):
        self.iloscmonet = 0
        self.table_filling()
    def update(self):
        self.player.update()
        self.monety.update()
        self.collision_spritemonety()
        self.bomby.update()
        self.collision_spritebomby()
        if self.game_end():
            self.pozostalezycia = 9
            self.bomby.empty()
            self.monety.empty()
            self.monety.add(Monety("braz"), Monety("zloto"), Monety("srebro"))
            self.scene_man.current_scene = self.scene_man.end_scene
    def render(self):


        self.screen.blit(self.sky,self.sky_rect)

        self.monety.draw(self.screen)
        self.bomby.draw(self.screen)
        self.screen.blit(self.ground, self.ground_rect)
        self.player.draw(self.screen)

        for i in range(self.pozostalezycia):
            self.screen.blit(self.zycia[i].image,self.zycia[i].rect)
        for i in range(self.iloscmonet):
            self.screen.blit(self.licznikmonet[i%116].image, self.licznikmonet[i%116].rect)



