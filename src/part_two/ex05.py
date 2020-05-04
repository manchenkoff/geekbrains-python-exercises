"""
Для чисел в пределах от X до Y найти числа, кратные 20 или 21. Необходимо решить задание в одну строку.

Подсказка: использовать функцию range() и генератор.
"""

start = int(input())
stop = int(input())

items = [x for x in range(start, stop) if x % 20 == 0 or x % 21 == 0]

print(" ".join(map(str, items)))
