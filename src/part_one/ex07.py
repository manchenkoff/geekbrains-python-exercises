"""
Пользователь внес список значений разных типов данных в переменную items.
Реализовать скрипт определения и вывода типа данных каждого элемента на новой строке.
Использовать функцию type() для определения типа.
"""


def is_int(x: str):
    return x.isdigit()


def is_float(x: str):
    try:
        float(x)
        return True
    except ValueError:
        return False


def is_boolean(x: str):
    return x == "True" or x == "False"


def is_none_type(x: str):
    return x == "None"


string_items = input().replace(" ", "").split(",")
items = []

for item in string_items:
    if is_int(item):
        items.append(int(item))
    elif is_float(item):
        items.append(float(item))
    elif is_boolean(item):
        items.append(bool(item))
    elif is_none_type(item):
        items.append(None)
    else:
        items.append(str(item))

# solution starts here
[print(type(x)) for x in items]
