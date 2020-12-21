from random import randint

lst = []
tmp = []
s = 0

while True:
    try:
        m = int(input('Введите число строк: '))
        n = int(input('Введите число столбцов: '))
    except ValueError:
        print('Некорректное значение!')
    else:
        if m > 0 and n > 0: break
        else: print('Некорректная величина!')

for i in range(m):
    lst.insert(i, [randint(1, 50) for _ in range(n)])

tmp = [0] * n

# Считаем и складываем в tmp[] сумму слобцов
for i in range(n):
    for j in range(m):
        tmp[i] += lst[j][i]

for i in range(m):
    s = 0
    for j in range(n):
        s += lst[i][j]
        print('{:>4}'.format(lst[i][j]), end='')
    print('{:>8}'.format(s))
print()
for z in range(n):
    print('{:>4}'.format(tmp[z]), end='')
print()
