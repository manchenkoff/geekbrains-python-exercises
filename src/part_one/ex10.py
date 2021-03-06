"""
Пользователь вводит строку из нескольких слов, разделённых пробелами.
Вывести каждое слово с новой строки. Строки необходимо пронумеровать с 1.
Если слово длинное (> 10 символов), выводить только первые 10 букв в слове.
"""

words = input().split()

for idx, value in enumerate(words, start=1):
    print(f"{idx}. {value[:10]}")
