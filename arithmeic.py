# Готовим функцию
def arithmetic(num_a, num_b, action):
	res = 'Неизвестная операция!'
	if action == '+': res = num_a + num_b
	if action == '-': res = num_a - num_b
	if action == '*': res = num_a * num_b
	if action == '/': res = num_a / num_b
#	else: res == 'Неизвестная операция!'
	return (res)

# Получаем исходные данные
print('Программа выведет результат действий над двумя числами')
a = float(input('Введите первое число: '))
b = float(input('Введите второе число: '))
c = input('Введите действие(+,-,*,/): ')
if ((a % 1) == 0) and ((b % 1) == 0):
	a = int(a)
	b = int(b)
print('Результат вашего запроса', a, c, b,': ', end='')
print(arithmetic(a, b, c))
