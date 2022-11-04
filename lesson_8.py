"""
Пример использования объектов property
"""
from string import ascii_letters, ascii_uppercase


class Person:

    def __init__(self,
                 name: str,
                 surname: str,
                 patronymic: str,
                 old: int,
                 weight: float,
                 serial_passport: str):

        self.name = name
        self.surname = surname
        self.patronymic = patronymic
        self.old = old
        self.weight = weight
        self.serial_passport = serial_passport

    @classmethod
    def validate_name(cls, name: str) -> None:
        if type(name) != str:
            raise TypeError("Недопустимый тип данных. Ожидаю строку")

    @classmethod
    def validate_surname(cls, surname: str) -> None:
        if not isinstance(surname, str):
            raise TypeError("Недопустимый тип данных. Ожидаю строку")

    @classmethod
    def validate_patronymic(cls, patronymic: str) -> None:
        if not isinstance(patronymic, str):
            raise TypeError("Недопустимый тип данных. Ожидаю строку")

    @classmethod
    def validate_old(cls, old: int) -> None:
        if 0 < old < 125:
            raise ValueError("Недопустимый возраст. >0 < 125")
        if not isinstance(old, int):
            raise TypeError("Недопустимый тип данных. Ожидаю целое число")

    @classmethod
    def validate_weight(cls, weight: float) -> None:
        if not isinstance(weight, float):
            raise TypeError("Недопустимый тип данных. Ожидаю вещественное число")
        if weight > 125:
            raise ValueError("Надо похудеть")
        if weight < 40:
            raise ValueError("Надо потолстеть")

    @classmethod
    def validate_serial_passport(cls, serial_passport: str) -> None:
        if not isinstance(serial_passport, str):
            raise TypeError("Недопустимый тип данных. Ожидаю строку")
        if serial_passport[0] and serial_passport[1] not in ascii_letters:
            raise TypeError("Серийный номер начинается с букв")
        check_digit = serial_passport[2:]
        for letter in check_digit:
            if not letter.isdigit():
                raise TypeError("Введен некоректный номер паспорта")

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        self.validate_name(name=name)
        self.__name = name

    @name.deleter
    def name(self) -> None:
        del self.__name

    @property
    def surname(self) -> str:
        return self.__surname

    @surname.setter
    def surname(self, surname: str) -> None:
        self.validate_surname(surname=surname)
        self.__surname = surname

    @surname.deleter
    def surname(self) -> None:
        del self.__surname

    @property
    def patronymic(self) -> str:
        return self.__patronymic

    @patronymic.setter
    def patronymic(self, patronymic: str) -> None:
        self.validate_patronymic(patronymic=patronymic)
        self.__patronymic = patronymic

    @patronymic.deleter
    def patronymic(self) -> None:
        del self.__patronymic

    @property
    def old(self) -> int:
        return self.__old

    @old.setter
    def old(self, old: int) -> None:
        self.validate_old(old=old)
        self.__old = old

    @old.deleter
    def old(self) -> None:
        del self.__old

    @property
    def weight(self) -> float:
        return self.__weight

    @weight.setter
    def weight(self, weight: float) -> None:
        self.validate_weight(weight=weight)
        self.__weight = weight

    @weight.deleter
    def weight(self) -> None:
        del self.__weight

    @property
    def serial_passport(self) -> str:
        return self.__serial_passport

    @serial_passport.setter
    def serial_passport(self, serial_passport) -> None:
        self.validate_serial_passport(serial_passport=serial_passport)
        self.__serial_passport = serial_passport

    @serial_passport.deleter
    def serial_passport(self) -> None:
        del self.__serial_passport


person_1 = Person(name='Anton',
                  surname='Baton',
                  patronymic='Alexandrovich',
                  old=29,
                  weight=99.0,
                  serial_passport='MP360780')

print(person_1.__dict__)

person_2 = Person(name='Artem',
                  surname='Hudoy',
                  patronymic='Kishka-tonka',
                  old=80,
                  weight=60.0,
                  serial_passport='MP36078P')

print(person_2.__dict__)
