
from game import Game
from scene_manager import SceneManager
def main():
    scene_manager = SceneManager()
    game = Game(scene_manager)
    game.run()

if __name__ == "__main__":
    main()