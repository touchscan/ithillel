i = 0
count = 0
mn = 0
mx = 0
odd = 0
even = 0
sum = 0
while i == 0:
	from_user = int(input('Введите целое число(0 - выход): '))
	if from_user == 0:
		mid = sum / count
		print('Количество чисел: ', count)
		print('Сумма чисел: ', sum)
		print('Среднее арифметическое: ', mid)
		print('Минимальное число: ', mn)
		print('Максимальное число: ', mx)
		print('Четных чисел: ', even)
		print('Нечетных чисел: ', odd)
		break
	count += 1
	sum += from_user
	if (from_user % 2):
		odd += 1
	else:
		even += 1
	if (from_user > mx):
		mx = from_user
	if (count == 1):
		mn = from_user
	if (from_user < mn):
		mn = from_user

