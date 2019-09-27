import libtcodpy as libtcod

from Constants import MIN_ROOM, MAX_ROOM, MAX_ROOM_HEIGHT, MAX_ROOM_WIDTH,\
                      MIN_ROOM_HEIGHT, MIN_ROOM_WIDTH, MAP_WIDTH, MAP_HEIGHT,\
                      color_dark_ground, color_dark_wall


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
#TODO главный алгоритм генерации уровня