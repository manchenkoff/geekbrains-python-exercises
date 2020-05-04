"""
В файле workers.txt записаны фамилии сотрудников и величина их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.

Пример файла:
```
Иванов 23543.12
Петров 13749.32
```
"""

with open("workers.txt") as f:
    worker_list = [worker_line.split() for worker_line in (f.readlines())]

workers_with_info = [{"name": worker[0], "salary": float(worker[1])} for worker in worker_list if len(worker) > 1]

print("\n".join(
    map(
        lambda item: item["name"],
        filter(lambda item: item["salary"] < 20_000, workers_with_info)
    )
))
