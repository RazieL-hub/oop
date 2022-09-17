class Vector:
    """
    Декораторы @classmethod и @staticmethod для определения методов классов и статических методов.
    Что это такое и как работают.

    """
    MIN_COORD = 0
    MAX_COORD = 100

    @classmethod
    def validate(cls, arg):
        return cls.MIN_COORD <= arg <= cls.MAX_COORD

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_coords(self):
        return self.x, self.y

    @staticmethod
    def norm2(x, y):
        return x * x + y * y


v = Vector(5, 6)
res = v.get_coords()
print(v.validate(5))
print(v.norm2(v.x, v.y))
print(Vector.norm2(v.x, v.y))
