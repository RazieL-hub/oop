"""
Магические методы __setattr__, __getattribute__, __getattr__ и __delattr__ | ООП Python
"""


class Point:
    MAX_COORD = 100
    MIN_COORD = 0

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def set_coords(self, x: int, y: int):
        if self.MIN_COORD <= x <= self.MAX_COORD:
            self.x = x
            self.y = y

    def __getattribute__(self, item):
        """
        Управление обращением к атрибутам.
        Автоматически вызывается при получении свойства класса с именем item.
        """
        if item == "x":
            raise ValueError("доступ запрещён")
        return object.__getattribute__(self, item)

    def __setattr__(self, key, value):
        """
        Автоматически вызывается при изменении свойства key класса
        """
        if key == 'z':
            raise AttributeError("Недопустимое имя атрибута")
        object.__setattr__(self, key, value)
        self.__dict__[key] = value

    def __getattr__(self, item):
        """
        Автоматически вызывается при получении несуществующего свойства item класса
        """
        print("__getattr__: " + item)
        return False

    def __delattr__(self, item):
        """
        Автоматечески вызывается при удалении свойства item.
        (не важно: существует оно или нет)
        """
        print("__delattr__: " + item)
        object.__delattr__(self, item)


pt1 = Point(1, 2)
# pt1.set_bound(-100)
print(pt1.__dict__)
print(pt1.y)
a = pt1.y
print(a)
# pt2 = Point(10, 20)
pt1.yy = 5
print(pt1.__dict__)
