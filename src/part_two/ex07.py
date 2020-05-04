"""
Реализовать формирование списка, используя функцию range() и возможности генератора.
В список должны войти четные числа от x до y (включая границы).
Необходимо получить результат вычисления произведения всех элементов списка.

Подсказка: использовать функцию reduce().
"""

from functools import reduce


def main(start: int, stop: int):
    numbers = [x for x in range(start, stop + 1) if x % 2 == 0]
    multiply = reduce(lambda x, y: x * y, numbers, 1)

    return multiply


x = int(input())
y = int(input())

print(main(x, y))
