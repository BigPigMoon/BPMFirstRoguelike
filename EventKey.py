import libtcodpy as libtcod


def handle_key(player):
    key = libtcod.console_wait_for_keypress(True)
    print(key.c)
    # exit
    if key.vk == libtcod.KEY_ESCAPE:
        return True

    # fullscreen
    if key.lalt and key.vk == libtcod.KEY_ENTER:
        libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen())

    if key.vk == libtcod.KEY_TAB:
        return 2

    # Player control
    if key.vk == libtcod.KEY_UP or key.c == 107:
        # UP
        player.move(0, -1)
    elif key.vk == libtcod.KEY_DOWN or key.c == 106:
        # DOWN
        player.move(0, 1)
    elif key.vk == libtcod.KEY_LEFT or key.c == 104:
        # LEFT
        player.move(-1, 0)
    elif key.vk == libtcod.KEY_RIGHT or key.c == 108:
        # RIGHT
        player.move(1, 0)
