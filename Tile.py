import libtcodpy as libtcod


class Tile:
    def __init__(self, *, blocked, explore, view, char=None, color=libtcod.black):
        self.blocked = blocked
        self.explore = explore
        self.view = view
        if char is None:
            char = ' '
        self.char = char
        self.color = color
