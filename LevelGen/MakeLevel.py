import libtcodpy as libtcod

import MakeObject as make
import ScanWall as scan
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

# TODO Копатель прямоугольника
def dig_rect(level, rect):
    pass

#TODO главный алгоритм генерации уровня
def main_gen_level_algorithm():
    rnd = 0
    level = [
            [tile.Tile(blocked=True, explore=True, view=True, char='#')
            for i in range(const.MAP_WIDTH)] 
                for j in range(const.MAP_HEIGHT)
        ]

    first_room = make.create_room(const.MAP_WIDTH // 2, const.MAP_HEIGHT // 2)
    wall = scan.choise_wall(2, first_room)
    x = wall[0]
    y = libtcod.random_get_int(
            rnd, min(wall[1][0], wall[1][-1]), max(wall[1][0], wall[1][-1])
        )

    tonnel = make.create_tonel(x, y, 0)
    dig_rect(level, first_room)
    dig_rect(level, tonnel)

    return level
