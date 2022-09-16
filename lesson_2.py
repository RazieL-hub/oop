class Point:
    """
    1. Магический метод __new__. Пример паттерна Singleton | Объектно-ориентированное программирование
    2. cls - ссылается на сам класс, self - ссылается на экземляр класса
    """

    def __new__(cls, *args, **kwargs):
        print("BEGIN __NEW__")
        print("Вызов __new__ для " + str(cls))
        print("END __NEW__")
        return super().__new__(cls)

    def __init__(self, x=0, y=0):
        print("BEGIN __INIT__")
        print("Вызов метода __init__ для " + str(self))
        self.x = x
        self.y = y
        print("END __INIT__")


pt = Point(1, 2)
# Тут будет сейчас None, потому что в методе __new__ не вызвали super().__new__(cls)
# Как только добавляется return super().__new__(cls), то уже тогда происходит создание экземпляра класса
