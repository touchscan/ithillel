from random import randint
from pprint import pprint

lst = []
tmp = []

def sorter(l):
	for i in range (len(l)):
		for j in range (len(l)):
			tmp[i] += lst[j][i]
	for y in range (m):
		for x in range (m - 1):
			if tmp[x] > tmp[x+1]:
				tmp[x], tmp[x+1] = tmp[x+1], tmp[x]
				for z in range (m):
					l[z][x], l[z][x+1] = l[z][x+1], l[z][x]
	
			

def output():
	return

while True:
	try:
		m = int(input('Введите размер матрицы, целое число, большее 5: '))
	except ValueError:
		print('Некорректная величина!')
	else:
		if m > 5: break

for i in range (m):
	lst.insert(i, [randint(1, 50) for _ in range (m)])

tmp = [0] * m

sorter(lst)

pprint(lst)
print()
pprint(tmp)
