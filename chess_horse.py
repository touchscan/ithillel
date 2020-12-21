from string import ascii_lowercase, digits

lst = ['■', '□', '☉', '♞', '☒']
brd = []
hx = hy = bx = by = None

def board():
    for y in range(9):
        for x in range(9):
            if x == 0 and y != 8:
                brd[y][x] = digits[8 - y]
            elif x != 0 and y == 8:
                brd[y][x] = ascii_lowercase[x - 1]
            elif ((y % 2) == 0 and (x % 2) != 0) or ((y % 2) != 0 and
                                                     (x % 2) == 0):
                brd[y][x] = lst[0]
            elif x == 0 and y == 8:
                brd[y][x] = ''
            else:
                brd[y][x] = lst[1]


def out():
	print()
	for y in range(9):
		for x in range(9):
			if x == 0 and y != 8:
				print('{:<3}'.format(brd[y][x]), end='')
			elif x != 0 and y == 8:
				print('{:>2}'.format(brd[y][x]), end='')
			elif ((y % 2) == 0 and (x % 2) != 0) or ((y % 2) != 0 and (x % 2) == 0):
				print('{:>2}'.format(brd[y][x]), end='')
			elif x == 0 and y == 8:
				print('{:<3}'.format(brd[y][x]), end='')
			else:
				print('{:>2}'.format(brd[y][x]), end='')
		print()


def move(hx, hy, bx, by):
	brd[hy][hx] = lst[3]
	if ((bx - (hx + 1)) == 0 and (by - (hy + 1)) == 1) or ((bx - (hx + 1)) == 1 and (by - (hy + 1)) == 0):
		brd[by][bx] = lst[2]
	elif ((bx - (hx + 1)) == 0 and ((hy - 1) - by) == 1) or ((bx - (hx + 1)) == 1 and ((hy - 1) - by) == 0):
		brd[by][bx] = lst[2]
	elif (((hx - 1) - bx) == 0 and ((hy - 1) - by) == 1) or (((hx - 1) - bx) == 1 and ((hy - 1) - by) == 0):
		brd[by][bx] = lst[2]
	elif (((hx - 1) - bx) == 0 and (by - (hy + 1)) == 1) or (((hx - 1) - bx) == 1 and (by - (hy + 1)) == 0):
		brd[by][bx] = lst[2]
	else:
		brd[by][bx] = lst[4]
	

brd = [[0 for _ in range(9)] for _ in range(9)]
board()
out()
test = input('\nЗакажите ход конем, и мы бесплатно проверим его доступность!\nВведите координаты (например ход с a8 на с7: a8-c7): ')
hx = int(ascii_lowercase[0:8].find(test[0])) + 1
hy = 8 - int(test[1])
bx = int(ascii_lowercase[0:8].find(test[3])) + 1
by = 8 - int(test[4])
move(hx, hy, bx, by)
out()
if  '☉' in brd[by][bx]:
	print('\nЗаданный ход возможен!')
else:
	print('\nЗаданный ход невозможен!')
