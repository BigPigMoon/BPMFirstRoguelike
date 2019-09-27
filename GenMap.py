import libtcodpy as libtcod

from Rect import *
from Tile import *
from Constants import MIN_ROOM, MAX_ROOM, MAX_ROOM_HEIGHT, MAX_ROOM_WIDTH,\
                      MIN_ROOM_HEIGHT, MIN_ROOM_WIDTH, MAP_WIDTH, MAP_HEIGHT,\
                      color_dark_ground, color_dark_wall


def scan_up(coords, depth, map):
    y = coords[1]
    for x in coords[0]:
        for yd in range(1, depth):
            if not map[x][y-yd].blocked:
                return False        
    return True

def scan_down(coords, depth, map):
    y = coords[1]
    for x in coords[0]:
        for yd in range(1, depth):
            if not map[x][y+yd].blocked:
                return False
    return True


def scan_left(coords, depth, map):
    x = coords[0]
    for y in coords[1]:
        for xd in range(1, depth):
            if not map[x-xd][y].blocked:
                return False
    return True


def scan_right(coords, depth, map):
    x = coords[0]
    for y in coords[1]:
        for xd in range(1, depth):
            if not map[x+xd][y].blocked:
                return False        
    return True


def choise_wall(direct, room):
    """Выбирает комнату в зависимости от направления.

    args:
        direct -- направление выбора стены
        room -- комната в которой набо выбирать

    return:
        wall -- список со списком координат и одной координатой.
        Если не задать направления вернет None.
        
    схема направления
          1
          |
       4--.--2
          |
          3
    """
    x1 = room.x1
    x2 = room.x2
    y1 = room.y1
    y2 = room.y2
    
    if direct == "UP" or direct == 1:
        wall = [[x for x in range(min(x1, x2), max(x1, x2))], y1]
    elif direct == "DOWN" or direct == 3:
        wall = [[x for x in range(min(x1, x2), max(x1, x2))], y2]
    elif direct == "LEFT" or direct == 4:
        wall = [x1, [y for y in range(min(y1, y2), max(y1, y2))]]
    elif direct == "RIGHT" or direct == 2:
        wall = [x2, [y for y in range(min(y1, y2), max(y1, y2))]]
    else:
        print("oops, change true direction")
        return

    return wall


def scan_wall(direct, coords, depth, map):
    """Сканирует стену в глубину для новой комнаты, тунеля и пр.
    
    args:
        deriect -- направление для сканирования
        coords -- список координат для сканирования
        depth -- глубина сканирования
        map -- карта для сканирования

    return:
        clear -- чисто или нет(true or false)
    """
    if coords is not None:
        if direct == "UP" or direct == 1:
            scan_up(coords, depth, map)
        elif direct == "RIGHT" or direct == 2:
            scan_right(coords, depth, map)
        elif direct == "DOWN" or direct == 3:
            scan_down(coords, depth, map)
        elif direct == "LEFT" or direct == 4:
            scan_left(coords, depth, map)
    else:
        print("oops, your coordinates is None.")
        return


def dig_tile(map, x, y):
    """Расскапывает тайл.
    
    args:
        map -- карта, матрица для тайлов
        x -- координата тайла по x
        y -- координата тайла по y
    """
    map[x][y].blocked = False
    map[x][y].char = '.'
    map[x][y].color = color_dark_ground


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
def create_tonel()
#TODO написать генератор окружностей
#TODO написать генератор абстрактной хуйни