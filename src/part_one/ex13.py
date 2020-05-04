"""
Реализовать функцию main, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.

Функция должна принимать параметры как именованные аргументы.

Реализовать вывод данных о пользователе одной строкой.
"""


def main(first_name, last_name, year, city, email, phone):
    return f"{first_name} {last_name} ({year}), {city}, {phone}, {email}"


first_name = input()
last_name = input()
year = int(input())
city = input()
email = input()
phone = input()

print(main(first_name, last_name, year, city, email, phone))
