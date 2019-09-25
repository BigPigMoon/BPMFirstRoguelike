import libtcodpy as libtcod


class Player:
    def __init__(self, con, x, y, char, color):
        self.x = x
        self.y = y
        self.char = char
        self.color = color
        self.con = con

    def draw(self):
        libtcod.console_set_default_foreground(self.con, self.color)
        libtcod.console_put_char(self.con, self.x, self.y,
                                 self.char, libtcod.BKGND_NONE)

    def clear(self):
        libtcod.console_put_char(self.con, self.x, self.y, ' ',
                                 libtcod.BKGND_NONE)

    def move(self, dx, dy):
        if not self.map[self.x - 30 + dx][self.y + dy].blocked:
            self.x += dx
            self.y += dy

    def set_map(self, map):
        self.map = map
