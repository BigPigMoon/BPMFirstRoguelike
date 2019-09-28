import libtcodpy as libtcod

import Rect
import Constants as const


def create_room(x, y):
    """Создает комнату с рандомными размерами.

    return:
        Rect
    """
    rnd = 0
    w = libtcod.random_get_int(
            rnd, const.MIN_ROOM_WIDTH, const.MAX_ROOM_WIDTH
        )
    h = libtcod.random_get_int(
            rnd, const.MIN_ROOM_HEIGHT, const.MAX_ROOM_HEIGHT
        )
    room = Rect.Rect(x, y, w, h, "room")
    return room


# TODO написать генератор в лево и в верх
def create_tonel(x, y, direct):
    """Создает горизонтальный или вертикальный тонель
       с рандомной шириной или высотой, с заданными координатами.

    args:
        direct -- направление h|0 - горизонтальный, v|1 - вертикальный

    return:
        Rect
    """
    rnd = 0

    if direct == 1:
        # UP
        h = libtcod.random_get_int(
                rnd, const.MIN_TONEL_HEIGHT, const.MAX_TONEL_HEIGHT
        )
        w = 1
        y, h = h, y
    elif direct == 2:
        # RIGHT
        h = 1
        w = libtcod.random_get_int(
                rnd, const.MIN_TONEL_WIDTH, const.MAX_TONEL_WIDTH
        )
    elif direct == 3:
        # DOWN
        h = libtcod.random_get_int(
                rnd, const.MIN_TONEL_HEIGHT, const.MAX_TONEL_HEIGHT
        )
        w = 1
    elif direct == 4:
        # LEFT
        h = 1
        w = libtcod.random_get_int(
                rnd, const.MIN_TONEL_WIDTH, const.MAX_TONEL_WIDTH
        )
        w, x = x, w

    tonnel = Rect.Rect(x, y, w, h, "tonnel")

    return tonnel


# TODO написать генератор окружностей
def create_circle():
    pass


# TODO написать генератор абстрактной хуйни
def create_abstratc():
    pass
