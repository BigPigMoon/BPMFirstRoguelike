import libtcodpy as libtcod

from Rect import *
from Tile import *
from Constants import MIN_ROOM, MAX_ROOM, MAX_ROOM_HEIGHT, MAX_ROOM_WIDTH,\
                      MIN_ROOM_HEIGHT, MIN_ROOM_WIDTH, MAP_WIDTH, MAP_HEIGHT,\
                      color_dark_ground, color_dark_wall


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
    # TODO дописать скан для остальных направлений.

    if coords is not None:
        if direct == "UP" or direct == 1:
            y = coords[1]
            for x in coords[0]:
                for yd in range(1, depth):
                    # ???
                    if not map[x][y-yd].blocked:
                    #if map[x][y-yd].blocked == False:
                        return False
            
            return True

        elif direct == "RIGHT" or direct == 2:
            x = coords[0]
            for y in coords[1]:
                for xd in range(1, depth):
                    # ???
                    if not map[x+xd][y].blocked:
                    #if map[x][y-yd].blocked == False:
                        return False
            
            return True

        elif direct == "DOWN" or direct == 3:
            y = coords[1]
            for x in coords[0]:
                for yd in range(1, depth):
                    # ???
                    if not map[x][y+yd].blocked:
                    #if map[x][y-yd].blocked == False:
                        return False
            
            return True

        elif direct == "LEFT" or direct == 4:
            x = coords[0]
            for y in coords[1]:
                for xd in range(1, depth):
                    # ???
                    if not map[x-xd][y].blocked:
                    #if map[x][y-yd].blocked == False:
                        return False
            
            return True
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


def create_rooms():
    """Создает список комнат которые НЕ МОГУТ пересекаться друг с другом.
    
    return:
        rooms -- список комнат
    """
    x = 0
    rooms = [create_room()]
    while x < libtcod.random_get_int(0, MIN_ROOM, MAX_ROOM):
        new_room = create_room()

        failed = False
        for room in rooms:
            if new_room.intersect(room):
                failed = True

        if not failed:
            rooms.append(new_room)
            x += 1
    return rooms


def dig_rooms(map, rooms=None):
    """Выкапывает комнаты на основе списка комнат.

    args:
        map -- карта где надо копаться

    return:
        map -- измененная карта
    """
    if rooms is None:
        rooms = create_rooms()

    for room in rooms:
        for y in range(min(room.y1, room.y2), max(room.y1, room.y2)):
            for x in range(min(room.x1, room.x2), max(room.x1, room.x2)):
                dig_tile(map, x, y)

    return map


def make_map():
    """Создает играбельную карту.
    
    return:
        map -- измененная карта
    """
    map = [[Tile(blocked=True, explore=False, view=True, char='#', 
                 color=color_dark_wall)
                 for y in range(MAP_HEIGHT)] for x in range(MAP_WIDTH)]
    map = dig_rooms(map)
    #map = dig_tonnels(rooms, map)

    return map


def dig_h_tonel(map, x1, x2, y):
    """Выкапывает горизонтальный тонель в карте.
    
    args:
        map -- карта, матрица для тайлов
        x1 -- начало тонеля
        x2 -- конец тонеля
        y -- "глубина"
        """
    for x in range(min(x1, x2), max(x1, x2) + 1):
        dig_tile(map, x, y)


def dig_v_tonel(map, y1, y2, x):
    """Выкапывает вертикальный тонель в карте.
    
    args:
        map -- "Ну ты серьезно"
        y1 -- начало тонеля
        y2 -- конец тонеля
        x -- "глубина" тонеля
        """
    for y in range(min(y1, y2), max(y1, y2) + 1):
        dig_tile(map, x, y)


def dig_tonnels(rooms, map):
    """Прокапывает тонели в карте от комнаты к комнате,
        тонели г-образной формы.
        
    args:
        rooms -- список всех комнат
        map -- карта, матрица для тайлов

    return:
        map -- измененная карта
    """
    for i in range(-1, len(rooms)-1):
        prew_room = rooms[i]
        prew_x, prew_y = prew_room.center()

        new_room = rooms[i+1]
        new_x, new_y = new_room.center()

        if libtcod.random_get_int(0, 0, 1):
            dig_v_tonel(map, prew_y, new_y, new_x)
            dig_h_tonel(map, prew_x, new_x, prew_y)
        else:
            dig_v_tonel(map, prew_y, new_y, prew_x)
            dig_h_tonel(map, prew_x, new_x, new_y)

    return map

# TODO написать тест для скана
def test_scan_wall1():
    """
    ##############
    ###........###
    ###........###
    ###........###
    ###........###
    ##############
    ##############
    ###........###
    ###........###
    ###........###
    ###........###
    ##############
    """
    map = [[Tile(blocked=True, explore=False, view=True, char='#', 
                 color=color_dark_wall)
                 for y in range(12)] for x in range(14)]

    rooms = [Rect(3, 1, 8, 4), Rect(3, 7, 8, 4)]
    map = dig_rooms(map, rooms)
    wall = choise_wall(1, rooms[1])

    assert not scan_wall(1, wall, 5, map)

def test_scan_wall2():
    """
    ##############
    ###........###
    ###........###
    ###........###
    ###........###
    ##############
    ##############
    ###........###
    ###........###
    ###........###
    ###........###
    ##############
    """
    level = [[Tile(blocked=True, explore=False, view=True, char='#', color=color_dark_wall) for y in range(12)] for x in range(14)]
    
    rooms = [Rect(3, 1, 8, 4), Rect(3, 7, 8, 4)]
    level = dig_rooms(level, rooms)
    wall = choise_wall("DOWN", rooms[0])

    assert not scan_wall("DOWN", wall, 5, level)

def test_scan_wall3():
    """
    ##############
    ##############
    ##############
    ##############
    ##############
    ##############
    ##############
    ###........###
    ###........###
    ###........###
    ###........###
    ##############
    """
    map = [[Tile(blocked=True, explore=False, view=True, char='#', 
                 color=color_dark_wall)
                 for y in range(12)] for x in range(14)]

    rooms = [Rect(0, 0, 0, 0), Rect(3, 7, 8, 4)]
    map = dig_rooms(map, rooms)
    wall = choise_wall(1, rooms[1])

    assert scan_wall(1, wall, 5, map)

def test_scan_wall4():
    """
    ##############
    ###........###
    ###........###
    ###........###
    ###........###
    ##############
    ##############
    ##############
    ##############
    ##############
    ##############
    ##############
    """
    level = [[Tile(blocked=True, explore=False, view=True, char='#', color=color_dark_wall) for y in range(12)] for x in range(14)]
    
    rooms = [Rect(3, 1, 8, 4), Rect(0, 0, 0, 0)]
    level = dig_rooms(level, rooms)
    wall = choise_wall("DOWN", rooms[0])

    assert scan_wall("DOWN", wall, 5, level)

def test_scan_wall5():
    """
    ##############
    #.....###....#
    #.....###....#
    #.....###....#
    ##############
    """
    level = [[Tile(blocked=True, explore=False, view=True, char='#', color=color_dark_wall) for y in range(5)] for x in range(14)]
    
    rooms = [Rect(1, 1, 5, 3), Rect(9, 1, 4, 3)]
    level = dig_rooms(level, rooms)
    wall = choise_wall("RIGHT", rooms[0])

    assert not scan_wall("RIGHT", wall, 5, level)

def test_scan_wall6():
    """
    ##############
    #.....###....#
    #.....###....#
    #.....###....#
    ##############
    """
    level = [[Tile(blocked=True, explore=False, view=True, char='#', color=color_dark_wall) for y in range(5)] for x in range(14)]
    
    rooms = [Rect(1, 1, 5, 3), Rect(9, 1, 4, 3)]
    level = dig_rooms(level, rooms)
    wall = choise_wall("LEFT", rooms[1])

    assert not scan_wall("LEFT", wall, 5, level)

def test_scan_wall7():
    """
    ##############
    #.....########
    #.....########
    #.....########
    ##############
    """
    level = [[Tile(blocked=True, explore=False, view=True, char='#', color=color_dark_wall) for y in range(5)] for x in range(14)]
    
    rooms = [Rect(1, 1, 5, 3)]
    level = dig_rooms(level, rooms)
    wall = choise_wall("RIGHT", rooms[0])

    assert scan_wall("RIGHT", wall, 5, level)

def test_scan_wall8():
    """
    ##############
    #########....#
    #########....#
    #########....#
    ##############
    """
    level = [[Tile(blocked=True, explore=False, view=True, char='#', color=color_dark_wall) for y in range(5)] for x in range(14)]
    
    rooms = [Rect(9, 1, 5, 3)]
    level = dig_rooms(level, rooms)
    wall = choise_wall("LEFT", rooms[0])

    assert scan_wall("LEFT", wall, 5, level)
