def cycle(num, step, vector=False):
    if num == 0 or step == 0: return (num)
    l = len(num)
    if l < step: step = step // l
    if vector: return (int(num[(l - step):] + num[:(l - step)]))
    else: return (int(num[step:] + num[:step]))

n = input('Введите число, в котором выполним сдвиг: ')
s = int(input('Укажите на сколько разрядов сдвигаемся: '))
v = bool(input('Сдвиг влево - нажать enter\nСдвиг вправо - ввести любой символ\nИтак: ' ))
print('Результат операции:', cycle(n, s, v))
