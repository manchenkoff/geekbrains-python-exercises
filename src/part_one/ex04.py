"""
Пользователь вводит целое положительное число.
Найдите самую большую цифру в числе.

Для решения используйте цикл while и арифметические операции.
"""

number = int(input())

max_num = 0

while number:
    current = number % 10
    number = number // 10
    max_num = current if current > max_num else max_num

print(max_num)
