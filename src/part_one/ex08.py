"""
Для списка items реализовать обмен значений соседних элементов,
т.е. значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
"""

items = input().split(",")

max_idx = len(items) - 1

for idx in range(0, max_idx, 2):
    next_idx = idx + 1
    items[idx], items[next_idx] = items[next_idx], items[idx]

print(",".join(items))
