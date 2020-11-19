str_a = '''
   *
  * *
 *   *
*******
'''
str_b = '''
   *
  ***
 *****
*******
'''
str_c = '''
   *
  ***
 *****
*******
 *   *
  * *
   *
'''
str_d = '''
   *
  ***
 *****
*******
 * * *
  ***
   *
'''
while True:
	print('\n\n\n')
	print('1)', str_a)
	print('2)', str_b)
	print('3)', str_c)
	print('4)', str_d)
	figure = int(input('Выберите фигуру для отображения (0 - выход): '))
	if (figure == 0):
		break
	if (figure == 1):
		print(str_a)
		height = int(input('Какой высоты в знаках (0 - выбрать фигуру): '))
		if (height == 0):
			continue
		if (height < 0):
			height = - (height)
		if (height > 0):
			for y in range (height):
				for x in range (height * 2 - 1):
					if (y == height - x - 1
					or y == x - height + 1
					or y == height - 1):
 						print('*  ', end='')
					else:
						print('   ', end='')
				print()
	if (figure == 2):
		print(str_b)
		height = int(input('Какой высоты в знаках (0 - выбрать фигуру): '))
		if (height == 0):
			continue
		if (height < 0):
			height = - (height)
		if (height > 0):
			for y in range (height):
				for x in range ((height * 2) - 1):
					if (y >= height - 1 - x
					and y >= x - height + 1
					or y == height - 1):
						print('*  ', end='')
					else:
						print('   ', end='')
				print()

	if (figure == 3):
		print(str_c)
		height = int(input('Какой высоты в знаках (0 - выбрать фигуру): '))
		if (height == 0):
			continue
		if (height < 0):
			height = - (height)
		if (height > 0):
			for y in range (height):
				for x in range (height):
					if (y >= height // 2 - x
					and y >= x - height // 2
					and y <= height // 2
					or y == (x - height // 2) + height - 1
					or y == (height // 2 - x) + height - 1):
						print('*  ', end='')
					else:
						print('   ', end='')
				print()
	if (figure == 4):
		print(str_d)
		height = int(input('Какой высоты в знаках (0 - выбрать фигуру): '))
		if (height == 0):
			break
		if (height < 0):
			height = - (height)
		if (height > 0):
			for y in range (height):
				for x in range (height):
					if (y >= height // 2 - x
					and y >= x - height // 2
					and y <= height // 2
					or y == (x - height // 2) + height - 1
					or y == (height // 2 - x) + height - 1
					or y >= height // 2
					and y ==  (y - x) + height // 2):
						print('*  ', end='')
					else:
						print('   ', end='')
				print()
