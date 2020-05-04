"""
Реализовать функцию my_func(), которая принимает три позиционных аргумента
и возвращает сумму наибольших двух аргументов.
"""


def my_func(first, second, last):
    items = [first, second, last]
    items.remove(min(items))

    return sum(items)


a, b, c = int(input()), int(input()), int(input())

print(my_func(a, b, c))
