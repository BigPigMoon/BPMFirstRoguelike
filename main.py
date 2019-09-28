import libtcodpy as libtcod

import Player
import EventKey as event
import Constants as const
import LevelGen.MakeLevel as levelgen


def render_level(level):
    """Отрисовывает карту

    args:
        level -- карта которую нужно отрисовать
    """
    for y in range(const.MAP_HEIGHT):
        for x in range(const.MAP_WIDTH):
            tile = level[x][y]
            wall_view = tile.view

            if wall_view:
                libtcod.console_put_char_ex(
                    con, x + const.SCREEN_WIDTH - const.MAP_WIDTH, y,
                    tile.char, libtcod.white, tile.color
                )
            elif wall_view:
                libtcod.console_put_char_ex(
                    con, x + const.SCREEN_WIDTH - const.MAP_WIDTH, y,
                    tile.char, libtcod.white, tile.color
                )


libtcod.console_set_custom_font(
            'Font/font2.png',
            libtcod.FONT_TYPE_GRAYSCALE |
            libtcod.FONT_LAYOUT_TCOD
        )

libtcod.console_init_root(const.SCREEN_WIDTH, const.SCREEN_HEIGHT, "FirstRogue")
con = libtcod.console_new(const.SCREEN_WIDTH, const.SCREEN_HEIGHT)

level = levelgen.main_gen_level_algorithm()
player = Player.Player(con, 59, 25, '@', libtcod.white)

while not libtcod.console_is_window_closed():
    level = levelgen.main_gen_level_algorithm()
    player.set_map(level)
    # draw
    render_level(level)
    player.draw()
    libtcod.console_blit(con, 0, 0, const.SCREEN_WIDTH, const.SCREEN_HEIGHT, 0, 0, 0)

    libtcod.console_flush()
    # clear
    player.clear()

    # key event
    exit = event.handle_key(player)
    if exit is True:
        break
