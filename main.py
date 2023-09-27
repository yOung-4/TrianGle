import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "TrianGle"


class game(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.AMAZON)
        # set up the scene
        self.scene = None
        # set up the physics engine
        self.physics_engine = None
        # set up the camera
        self.camera = None


def main():
    game()
    arcade.run()


if __name__ == "__main__":
    main()