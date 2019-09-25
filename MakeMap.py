import libtcodpy as libtcod
from Rect import *
from Tile import *
from Constants import MIN_ROOM, MAX_ROOM, MAX_ROOM_HEIGHT, MAX_ROOM_WIDTH,\
                      MIN_ROOM_HEIGHT, MIN_ROOM_WIDTH, MAP_WIDTH, MAP_HEIGHT,\
                      color_dark_ground, color_dark_wall


def dig_tile(map, x, y):
    map[x][y].blocked = False
    map[x][y].char = '.'
    map[x][y].color = color_dark_ground


def create_room():
    """Создает комнату с рандомными размерами"""
    rnd = 0
    w = libtcod.random_get_int(rnd, MIN_ROOM_WIDTH, MAX_ROOM_WIDTH)
    h = libtcod.random_get_int(rnd, MIN_ROOM_HEIGHT, MAX_ROOM_HEIGHT)
    x = libtcod.random_get_int(rnd, 1, MAP_WIDTH - w - 1)
    y = libtcod.random_get_int(rnd, 1, MAP_HEIGHT - h - 1)

    room = Rect(x, y, w, h)
    return room


def create_rooms():
    """Создает список комнат которые НЕ МОГУТ пересекаться друг с другом"""
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


def dig_rooms(rooms, map):
    """Выкапывает комнаты на основе списка комнат

    args:
        rooms -- список комнат
        map -- карта где надо копаться
    """
    for room in rooms:
        for y in range(min(room.y1, room.y2), max(room.y1, room.y2)):
            for x in range(min(room.x1, room.x2), max(room.x1, room.x2)):
                dig_tile(map, x, y)

    return map


def make_map():
    """Создает играбельную карту"""
    map = [[Tile(blocked=True, explore=False, view=True, char='#', color=color_dark_wall)
            for y in range(MAP_HEIGHT)] for x in range(MAP_WIDTH)]
    rooms = create_rooms()
    map = dig_rooms(rooms, map)
    #map = dig_tonnel(rooms, map)

    return map


def dig_h_tonel(map, x1, x2, y):
    for x in range(min(x1, x2), max(x1, x2) + 1):
        dig_tile(map, x, y)


def dig_v_tonel(map, y1, y2, x):
    for y in range(min(y1, y2), max(y1, y2) + 1):
        dig_tile(map, x, y)


def dig_tonnel(rooms, map):
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