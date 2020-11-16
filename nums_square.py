num = int(input('Введите целое число: '))
count = 1
res=0
while res <= num:
	res = count ** 2
	if (res <= num):
		print(res, end=' ')
	count += 1
print()

