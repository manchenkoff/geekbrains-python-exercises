"""
Узнайте у пользователя положительное число n. Найдите сумму чисел n + nn + nnn.

Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
"""

number = int(input())

numbers = [int(str(number) * x) for x in range(1, 4)]

print(sum(numbers))
