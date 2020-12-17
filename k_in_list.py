import random

lst = [random.randint(0, 100) for _ in range(50)]
print('Исходный список:\n', lst)
while True:
    try:
        k = int(input('Введите индекс числа для удаления (999 - выход): '))
        if k == 999: break
        if k > len(lst):
            print('У нас нет столько значений в списке, попробуйте меньшее число.')
            continue
    except ValueError:
        print('Пожалуйста, укажите числовой индекс.')
    else:
        for i in range(k, len(lst) - 1):
            lst[i], lst[i + 1] = lst[i + 1], lst[i]
        lst.pop()
        print('Обработанный список:\n', lst)
