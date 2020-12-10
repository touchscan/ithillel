import random


def func_rev(lst):
    if len(lst) < 2: return (lst)
    for i in range(len(lst) // 2):
        lst[i], lst[len(lst) - 1 - i] = lst[len(lst) - 1 - i], lst[i]
    return (lst)


lst = [random.randint(0, 100) for _ in range (30)]
print('Сгенерированный список:\n', lst)
print('Перевернутый список:\n', func_rev(lst))
