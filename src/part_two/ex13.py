"""
Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).

Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.

Определить метод расчета массы асфальта в тоннах, необходимого для покрытия всего дорожного полотна.
Метод должен принимать два параметра: масса и толщина в см.

Использовать формулу:
длина*ширина*масса асфальта для покрытия одного кв метра дороги асфальтом,
толщиной в 1 см*число см толщины полотна.

Например: 20м * 5000м * 25кг * 5см = 12500 т
"""


class Road:
    _length: int
    _width: int

    def __init__(self, length: int, width: int):
        self._length = length
        self._width = width

    def calculate(self, mass: int, depth: int):
        return int((self._length * self._width * mass * depth) / 1000)


length, width, mass, depth = [int(x) for x in input().split()]

road = Road(length, width)
result = road.calculate(mass, depth)

print(result)
