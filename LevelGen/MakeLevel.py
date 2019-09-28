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

    return level
