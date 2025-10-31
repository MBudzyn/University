
class Game:
    def __init__(self, scene_manager):
        self.scene_manager = scene_manager

    def run(self):
        while True:
            self.scene_manager.handle_events()
            self.scene_manager.update()
            self.scene_manager.render()

newgame = Game(SceneManager())
newgame.run()