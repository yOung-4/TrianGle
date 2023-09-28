import arcade
from views.world_view import WorldView
from plugins.get_config import config


class MenuViews(arcade.View):
    def on_show_view(self):
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        self.clear()
        arcade.draw_text(
            "TrianGle",
            config["display"]["screen_width"] / 2,
            config["display"]["screen_height"] / 2,
            arcade.color.WHITE,
            font_size=80,
            anchor_x="center",
        )

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        world_view = WorldView()
        self.window.show_view(world_view)