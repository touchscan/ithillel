class Counter:
	def __init__(self, start, stop, position=None):
		self.start = start
		self.stop = stop
		if (position == 'None') or (position > self.stop) or (position < self.start):
			self.position = start
		else:
			self.position = position

	def run(self):
		if (self.position == self.stop):
			self.position = self.start
		else:
			self.position += 1
		
	def show(self):
		print(self.position)


tmp = input('Введите начало и конец диапазона (start:stop): ')
tmp = (tmp.split(':'))
a = int(tmp[0])
b = int(tmp[1])
c = input('Введите позицию счетчика (enter - пропустить): ')
if c.isalnum():
	c = int(c)
	counter = Counter(a, b, c)
else:
	counter = Counter(a, b)
print('\nНачат бесконечный цикл\n + увеличить\n* вывести состояние\n0 выход\n')
while True:
	s = input('Действие: ')
	if s == '+': counter.run()
	elif s == '*': counter.show()
	elif s == '0': break
