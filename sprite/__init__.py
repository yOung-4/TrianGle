import arcade


def load_texture_pair(filename):
    return [
        arcade.load_texture(filename),
        arcade.load_texture(filename, flipped_horizontally=True),
    ]


class Entity(arcade.Sprite):
    def __init__(self, file_name, folder_name):
        super().__init__()
        self.texture = load_texture_pair(f"./assets/{folder_name}/{file_name}.png")
