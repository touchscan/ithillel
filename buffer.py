
class Buffer:

	def __init__(self):
		self.lst = []

	def add(self, *a):
		for i in a:
			for j in i:
				self.lst.append(int(j))
		print(self.lst)
		
	def get_current_part(self):
		while len(self.lst) > 4:
			self.res = 0
			self.count = 4
			print(self.lst)
			while (self.count > -1):
				self.res += int(self.lst.pop(self.count))
				self.count -= 1
			print(self.res)
		print(self.lst)

obj = Buffer()
while True:
	lst = []
	d = input('Введите целое(ые) число(а), разделяя пробелами (q - выйти): ')
	if d == 'q': break
	obj.add(d.split())
	obj.get_current_part()