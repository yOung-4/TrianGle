import arcade


class WorldView(arcade.View):
    def __init__(self):
        super().__init__()

        # set up the keyboard
        self.key_left_pressed = False
        self.key_right_pressed = False
        self.key_up_pressed = False

    def on_show_view(self):
        self.clear()
        arcade.set_background_color(arcade.color.BLACK)