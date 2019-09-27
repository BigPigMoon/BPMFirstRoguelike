import libtcodpy as libtcod

from Rect import *
from Constants import MIN_ROOM, MAX_ROOM, MAX_ROOM_HEIGHT, MAX_ROOM_WIDTH,\
                      MIN_ROOM_HEIGHT, MIN_ROOM_WIDTH, MAP_WIDTH, MAP_HEIGHT

def create_room():
    """Создает комнату с рандомными размерами."""
    rnd = 0
    w = libtcod.random_get_int(rnd, MIN_ROOM_WIDTH, MAX_ROOM_WIDTH)
    h = libtcod.random_get_int(rnd, MIN_ROOM_HEIGHT, MAX_ROOM_HEIGHT)
    x = libtcod.random_get_int(rnd, 1, MAP_WIDTH - w - 1)
    y = libtcod.random_get_int(rnd, 1, MAP_HEIGHT - h - 1)

    room = Rect(x, y, w, h)
    return room


#TODO написать генератор тунелей во все стороны
def create_tonel():
    pass
#TODO написать генератор окружностей
#TODO написать генератор абстрактной хуйни