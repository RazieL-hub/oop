"""
Дескрипторы (data descriptor и non-data descriptor) | ООП Python
"""
class Descriptor:
    @classmethod
    def verify_coord(cls, coord):
        if type(coord) != int:
            raise TypeError("Координата должна быть целым числом")

    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        self.verify_coord(value)
        setattr(instance, self.name, value)


class Point3D:
    x = Descriptor()
    y = Descriptor()
    z = Descriptor()

    def __init__(self, x: int, y: int, z: int):
        self.x = x
        self.y = y
        self.z = z


p = Point3D(1, 2, 3)
print(p.__dict__)
print(p.x)
