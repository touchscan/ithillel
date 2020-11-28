import random
# Создаем и заполняем список
lst1 = [ random.randrange(0, 100)  for _ in range (10) ]
lst2 = [ random.randrange(0, 100) for _ in range (10) ]
print('lst1: ', lst1)
print('lst2: ', lst2)
# Считаем только уникальные числа в списке
res = len(set(lst1) ^ set(lst2))
print('Для обоих списков уникальных', res, 'чисел')
