
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
