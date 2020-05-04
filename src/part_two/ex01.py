"""
Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
но с прописной первой буквой (остальные буквы не менять).

Например,
print(int_func(‘text’)) -> Text.
print(int_func(‘tExT’)) -> TExt.
"""


def int_func(word: str):
    return "".join([
        word[0].upper(), word[1:]
    ])


print(int_func(input()))
