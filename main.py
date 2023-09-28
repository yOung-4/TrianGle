import arcade
from plugins.get_config import config
from views.menu_view import MenuViews


def main():
    windows = arcade.Window(config["display"]["screen_width"], config["display"]["screen_height"], config["display"]["screen_title"])
    menu_view = MenuViews()
    windows.show_view(menu_view)


if __name__ == "__main__":
    main()
    arcade.run()
