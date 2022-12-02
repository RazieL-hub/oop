class Clock:
    """
    Магические методы __add__, __sub__, __mul__, __truediv__
    """
    __DAY = 86400

    def __init__(self, seconds: int):
        if not isinstance(seconds, int):
            raise TypeError("qwerty")
        self.seconds = seconds % self.__DAY

    def get_time(self):
        s = self.seconds % 60
        m = (self.seconds // 60) % 60
        h = (self.seconds // 3600) % 24
        return f"{self.__get_formatted(h)}:{self.__get_formatted(m)}:{self.__get_formatted(s)}"

    @classmethod
    def __get_formatted(cls, x):
        return str(x).rjust(2, "0")

    def __add__(self, other):
        if not isinstance(other, (int, Clock)):
            raise ArithmeticError("INTEGER PLEASE OR CLOCK")
        if isinstance(other, int):
            return Clock(self.seconds + other)
        else:
            return Clock(self.seconds + other.seconds)

    def __radd__(self, other):
        if not isinstance(other, int):
            raise ArithmeticError("INTEGER PLEASE OR CLOCK")
        return self + other

    def __iadd__(self, other):
        print("__iadd")
        if not isinstance(other, (int, Clock)):
            raise ArithmeticError("INTEGER PLEASE OR CLOCK")

        self.seconds += other
        return self

c1 = Clock(1000)
c1 += 100
print(c1.get_time())