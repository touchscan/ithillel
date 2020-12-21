from random import randint

lst = []
tmp = []

def sorter(l, t):
# Сумма элементов в столбцах
	for i in range (len(l)):
		for j in range (len(l)):
			t[i] += lst[j][i]
	
# Сотрировка положения столбцов по возрастанию сумм
	for y in range (m):
		for x in range (m - 1 - y):
			if t[x] > t[x+1]:
				t[x], t[x+1] = t[x+1], t[x]
				for z in range (m):
					l[z][x], l[z][x+1] = l[z][x+1], l[z][x]

# Сортировка элементов в столбцах по условию

# четный растет сверху вниз
	for x in range (1, m, 2):
		for y in range (m - 1):
			for z in range (m - 1):
				if lst[z][x] > lst[z+1][x]:
					lst[z][x], lst[z+1][x] = lst[z+1][x], lst[z][x]

# нечетный - снизу вверх
	for x in range(0, m, 2):
		for y in range (m - 1):
			for z in range (m-1):
				if lst[z][x] < lst[z+1][x]:
					lst[z][x], lst[z+1][x] = lst[z+1][x], lst[z][x]


def output(l, t):
	for y in range (m):
		for x in range (m):
			if l[y][x] < 10:
				print(l[y][x], '    ', end='')
			else:
				print(l[y][x], '   ' , end='')
		print()
	print()
	for z in range (m):
		if t[z] < 10:
			print(t[z], ' ', end='')
		else:
			print(t[z], '  ', end='')
	print()

while True:
	try:
		m = int(input('Введите число строк: '))
		n = int(input('Введите число столбцов: '))
	except ValueError:
		print('Некорректное значение!')
	else:
		if m > 0 or n > 0: break
		else: print('Некорректная величина!')

for i in range (m):
	lst.insert(i, [randint(1, 50) for _ in range (n)])

tmp = [0] * m
sorter(lst, tmp)
output(lst, tmp)
