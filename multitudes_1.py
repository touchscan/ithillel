# Создаем и заполняем список
import random
lst = [ random.randrange(0, 100)  for _ in range (20) ]
print('lst: ', lst)
# Считаем только уникальные числа в списке
res = len(set(lst))
print('В списке уникальных', res, 'чисел')
