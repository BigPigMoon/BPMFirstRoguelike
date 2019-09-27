import libtcodpy as libtcod

from Player import *
from EventKey import *
from Constants import MAP_HEIGHT, MAP_WIDTH, SCREEN_HEIGHT, SCREEN_WIDTH


def render_map(map):
    """Отрисовывает карту

    args:
        map -- карта которую нужно отрисовать
    """
    for y in range(MAP_HEIGHT):
        for x in range(MAP_WIDTH):
            tile = map[x][y]
            wall_view = tile.view

            if wall_view:
                libtcod.console_put_char_ex(con, x+SCREEN_WIDTH-MAP_WIDTH, y,
                                            tile.char, libtcod.white,
                                            tile.color)
            elif wall_view:
                libtcod.console_put_char_ex(con, x+SCREEN_WIDTH-MAP_WIDTH, y,
                                            tile.char, libtcod.white,
                                            tile.color)


libtcod.console_set_custom_font('Font/font2.png',
                                libtcod.FONT_TYPE_GRAYSCALE |
                                libtcod.FONT_LAYOUT_TCOD)

libtcod.console_init_root(SCREEN_WIDTH, SCREEN_HEIGHT, "FirstRogue")
con = libtcod.console_new(SCREEN_WIDTH, SCREEN_HEIGHT)

player = Player(con, 50, 20, '@', libtcod.white)
player.set_map(map)

while not libtcod.console_is_window_closed():
    player.set_map(map)
    # draw
    render_map(map)
    player.draw()
    libtcod.console_blit(con, 0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, 0, 0, 0)

    libtcod.console_flush()
    # clear
    player.clear()

    # key event
    exit = handle_key(player)
    if exit is True:
        break
