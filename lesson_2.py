class Point:
    """ Магический метод __new__. Пример паттерна Singleton | Объектно-ориентированное программирование"""

    def __new__(cls, *args, **kwargs):
        print("Вызов __new__ для " + str(cls))

    def __init__(self, x=0, y=0):
        print("Вызов метода __init__ для " + str(self))
        self.x = x
        self.y = y


pt = Point(1, 2)
print(pt)