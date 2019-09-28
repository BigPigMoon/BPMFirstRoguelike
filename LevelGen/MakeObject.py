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
    room = Rect.Rect(x, y, w, h)
    return room


# TODO написать генератор тунелей во все стороны
def create_tonel(x, y, direct):
    """Создает горизонтальный или вертикальный тонель
       с рандомной шириной или высотой, с заданными координатами.
       
    args:
        direct -- направление h|0 - горизонтальный, v|1 - вертикальный
        
    return:
        Rect
    """
    rnd = 0
    if direct == 0 or direct == "h":
        h = 1
        w = libtcod.random_get_int(
                rnd, const.MIN_TONEL_WIDTH, const.MAX_TONEL_WIDTH
            )
    elif direct == 1 or direct == "v":
        h = libtcod.random_get_int(
                rnd, const.MIN_TONEL_HEIGHT, const.MAX_TONEL_HEIGHT
            )
        w = 1
    tonnel = Rect.Rect(x, y, w, h)

    return tonnel


# TODO написать генератор окружностей
def create_circle():
    pass


# TODO написать генератор абстрактной хуйни
def create_abstratc():
    pass
