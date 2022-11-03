class Point:
    """
    lesson 4-6
    Режимы доступа public, private, protected, setter, getter
    """

    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y

    @classmethod
    def __check_value(cls, x):
        return type(x) in (int, float)

    def set_coord(self, x, y):
        if self.__check_value(x) and self.__check_value(y):
            self._x = x
            self._y = y
        else:
            raise ValueError("Координаты должны быть числами")

    def get_coords(self):
        return self._x, self._y


pt = Point(1, 2)
q = pt.get_coords()

