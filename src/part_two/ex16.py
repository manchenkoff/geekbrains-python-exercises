"""
Создайте свой класс IntegerList, унаследованный от list.
Переопределите методы append и insert так, чтобы перед добавлением элемента выполнялась проверка
и привидение типа к int.

Создайте собственный класс-исключение InvalidObjectType, который принимает в кострукторе два параметра:
expected - тип ожидаемого класса
actual - тип класса переданного значения

Если при добавлении элемента в IntegerList не удалось привести к типу int, нужно бросать исключение InvalidObjectType,
но при этом вывести сообщение "Неверный тип объекта, передан <class 'str'> вместо <class 'int'>" и пропустить значение.
"""


class InvalidObjectType(ValueError):
    expected: type
    actual: type

    def __init__(self, expected: type, actual: type):
        self.expected = expected
        self.actual = actual

    def __str__(self):
        return f"Неверный тип объекта, передан {self.actual} вместо {self.expected}"


class TypedList(list):
    class_type: type

    def __init__(self, cls, seq=()):
        super().__init__(seq)
        self.class_type = cls

    def __str__(self):
        return f"{self.class_type} {super().__str__()}"

    def __check_value(self, value) -> bool:
        try:
            return self.class_type(value)
        except ValueError:
            raise InvalidObjectType(self.class_type, type(value))

    def append(self, __object) -> None:
        value = self.__check_value(__object)
        super().append(value)

    def insert(self, __index: int, __object) -> None:
        value = self.__check_value(__object)
        super().insert(__index, value)


my_list = TypedList(int, [1, 2, 3, 4])

try:
    my_list.append(input())
    print(my_list)
except InvalidObjectType as error:
    print(error)
