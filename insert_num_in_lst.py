import random
# Создаем, наполняем и выводим список
lst = [ random.randrange(0, 100) for _ in range(20)]
print('Список:\n', lst)
# Считаем длину списка и получаем данные от пользователя
l = len(lst)
c = int(input('Какое число вставим в список?: '))
k = int(input('В какую позицию списка?: '))
# Добавляем элемент в конец списка, чтобы было куда сдвигать элементы
lst.append(0)
# Двигаем
for i in range (l-1, k-1, -1):
	lst[i+1] = lst[i]
lst[k] = c
print()
print('Результат:\n', lst)
