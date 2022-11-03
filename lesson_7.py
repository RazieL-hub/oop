class Person:
    def __init__(self, name: str, old: int) -> None:
        self.__name = name
        self.__old = old

    @property
    def old(self):
        return self.__old

    @old.setter
    def old(self, old: int):
        self.__old = old

    @old.deleter
    def old(self):
        del self.__old

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


p = Person(name='Антон', old=20)
print(p.__dict__)
p.old = 35
print(p.__dict__)
p.name = "Картошка"
print(p.__dict__)
del p.old
print(p.__dict__)
