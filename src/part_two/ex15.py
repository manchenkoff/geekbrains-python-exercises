"""
Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».

В рамках класса реализовать метод __str__ для перегрузки отображения через print в формате "ГГГГ.ММ.ДД"
"""


class Date:
    year: int
    month: int
    day: int

    def __init__(self, date_string: str):
        self.day, self.month, self.year = map(int, date_string.split("-"))

    def __str__(self):
        return f"{self.year}.{self.month:0>2}.{self.day:0>2}"


my_date = Date(input())

print(my_date)
