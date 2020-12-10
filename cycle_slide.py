def cycle(num, step, vector=False):
	if num == 0 or step == 0: return (num)
	if vector:
		for _ in range (step):
			num *= 10
	else:
		for _ in range (step):
			num //= 10
	return (num)

n = int(input('Введите число, в котором выполним сдвиг: '))
s = int(input('Укажите на сколько разрядов сдвигаемся: '))
v = bool(input('Сдвиг влево - нажать enter\nСдвиг вправо - ввести любой символ\nИтак: '))
print('Результат операции:', cycle(n, s, v))
