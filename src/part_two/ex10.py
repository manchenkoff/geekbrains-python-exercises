"""
Есть файл example.txt, в нем записано несколько строк
необходимо выполнить подсчет количества строк и количества слов в каждой строке.

Вывести результат в формате:
строк - X, слов - Y

Пример файла:
```
first
second-line
third line
fourth line
```
"""

with open('example.txt') as f:
    rows = f.readlines()
    words = [row.split() for row in rows]

rows_count, words_count = len(rows), sum([len(word_list) for word_list in words])

print(f"строк - {rows_count}, слов - {words_count}")
