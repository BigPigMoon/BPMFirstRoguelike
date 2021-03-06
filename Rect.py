import libtcodpy as libtcod


class Rect:
    def __init__(self, x, y, w, h, type=None):
        self.x1 = x
        self.y1 = y
        self.x2 = w + x
        self.y2 = h + y
        self.type = type

    def intersect(self, other):
        """Проверка исключений."""
        return (self.x1 <= other.x2 and self.x2 >= other.x1 and
                self.y1 <= other.y2 and self.y2 >= other.y1)

    def center(self):
        """Определение центров прямоугольника(комнаты)."""
        center_x = (self.x1 + self.x2) // 2
        center_y = (self.y1 + self.y2) // 2

        return (center_x, center_y)
