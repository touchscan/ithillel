import random
# Создаем и наполняем список чисел
lst = [random.randrange(0, 100) for _ in range (10)]
print('lst: ', lst)
# Ищем самые-самые числа и считаем их количество
l = len(lst)
count = 0
for i in range (1, l-1):
	if lst[i-1] < lst[i] > lst[i+1]: count += 1
print('Чисел, которые больше обоих соседей: ', count)
 
