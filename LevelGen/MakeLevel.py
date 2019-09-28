import libtcodpy as libtcod

import LevelGen.MakeObject as make
import LevelGen.ScanWall as scan
import Color as color
import Constants as const
import Tile as tile


def dig_tile(level, x, y):
    """Расскапывает тайл.
    
    args:
        level -- карта, матрица для тайлов
        x -- координата тайла по x
        y -- координата тайла по y
    """
    level[x][y].blocked = False
    level[x][y].char = '.'
    level[x][y].color = color.dark_ground


def dig_rect(level, rect):
    for y in range(min(rect.y1, rect.y2), max(rect.y1, rect.y2)):
        for x in range(min(rect.x1, rect.x2), max(rect.x1, rect.x2)):
            dig_tile(level, x, y)

#TODO главный алгоритм генерации уровня
def main_gen_level_algorithm():
    rnd = 0
    level = [
            [tile.Tile(blocked=True, explore=True,
                       view=True, char='#', color=color.dark_wall)
            for i in range(const.MAP_WIDTH)] 
                for j in range(const.MAP_HEIGHT)
        ]

    obj = make.create_room(
        const.MAP_WIDTH // 2 - const.MAX_ROOM_WIDTH,
        const.MAP_HEIGHT // 2 - const.MAX_ROOM_HEIGHT
    )

    objs = [obj]

    while len(objs) < 20:
        random_obj = objs[libtcod.random_get_int(rnd, 0, len(objs) - 1)]
        print(objs)

        direct = libtcod.random_get_int(rnd, 1, 4)
        wall = scan.choise_wall(direct, random_obj)
        if type(wall[0]) == list:
            if not scan.scan_wall(direct, wall, const.DEPTH_SCAN, level):
                print("yes")
                x = libtcod.random_get_int(
                    rnd, min(wall[0][0], wall[0][-1]),
                         max(wall[0][0], wall[0][-1])
                )
                y = wall[1]
                if libtcod.random_get_int(rnd, 0, 1):
                    new_obj = make.create_tonel(x, y, direct)
                else:
                    new_obj = make.create_room(x, y)

                objs.append(new_obj)

        elif type(wall[1]) == list:
            if not scan.scan_wall(direct, wall, const.DEPTH_SCAN, level):
                print("yes")
                x = wall[0]
                y = libtcod.random_get_int(
                    rnd, min(wall[1][0], wall[1][-1]),
                         max(wall[1][0], wall[1][-1])
                )
                if libtcod.random_get_int(rnd, 0, 1):
                    new_obj = make.create_tonel(x, y, direct)
                else:
                    new_obj = make.create_room(x, y)

                objs.append(new_obj)

    for obj in objs:
        dig_rect(level, obj)

    return level
