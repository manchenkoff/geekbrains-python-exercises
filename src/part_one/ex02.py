"""
Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды
и выведите в формате чч:мм:сс. Используйте форматирование строк.
"""

user_seconds = int(input())

TIME_SEPARATOR: int = 60

hours = user_seconds // TIME_SEPARATOR ** 2
minutes = (user_seconds // TIME_SEPARATOR) - (hours * TIME_SEPARATOR)
seconds = user_seconds - (minutes * TIME_SEPARATOR) - (hours * TIME_SEPARATOR ** 2)

print(f"{hours:0>2}:{minutes:0>2}:{seconds:0>2}")
