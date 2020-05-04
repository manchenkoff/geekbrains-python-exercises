"""
В текстовом файле numbers.txt записан набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

with open("numbers.txt") as f:
    numbers = [int(x) for x in f.readline().split()]

print(sum(numbers))
