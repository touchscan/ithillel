def func_convert(num, to):
	res = ''
	from string import ascii_uppercase
	if num == 0 or to == 10: return (str(num))
	while num > 0:
		res = str(ascii_uppercase[(num % to) - 10] if (num % to) > 9 else (num % to)) + res
		num //= to
	return (res)

n = int(input('Введите число для конвертации: '))
t = int(input('Введите систему счисления (2 - 36): '))
print('Результат:', func_convert(n, t))
