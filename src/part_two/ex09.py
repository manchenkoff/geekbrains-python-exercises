"""
Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
После успешной записи необходимо вывести все строки на экран.
"""

strings = []

while True:
    try:
        string = input()
        strings.append(f"{string}\n")
    except EOFError:
        break

with open('file.txt', 'w') as f:
    f.writelines(strings)

with open('file.txt') as f:
    for line in f.readlines():
        print(line.strip())
