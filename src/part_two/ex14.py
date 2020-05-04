"""
Реализовать базовый класс Worker (работник), в котором определить атрибуты:
- name
- surname
- position (должность)
- income (доход)

Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
например, {"wage": wage, "bonus": bonus}.

Создать класс Position (должность) на базе класса Worker.

В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
и дохода с учетом премии (get_total_income) и вывести их результаты.
"""


class Worker:
    name: str
    surname: str
    position: str
    _income: dict

    def __init__(self, name: str, surname: str, position: str, wage: int, bonus: int):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        return f"{self.name} {self.surname}, {self.position}"

    def get_total_income(self):
        total = sum(self._income.values())
        return f"{total} р"


first_name, last_name, job, salary, bonus = input().split()
salary, bonus = [int(x) for x in (salary, bonus)]

worker = Position(first_name, last_name, job, salary, bonus)

print(worker.get_full_name())
print(worker.get_total_income())
