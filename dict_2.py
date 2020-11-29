import pprint

# Переменные
lst_in = []
d_out = {}
count = 1
elem = None

# Вариант вводных строк 1
str1 = 'мама мыла раму рама мыла маму мама мыла рама не мыла'
str2 = 'корабли лавировали лавировали и не вылавировали и для чего лавировали'
str3 = 'на дворе трава на траве дрова'
lst_in.append(list(str1.split(' ')))
lst_in.append(list(str2.split(' ')))
lst_in.append(list(str3.split(' ')))

# Вариант вводных строк 2
#hile True:
#	str = input('Введите строку, разделяя слова пробелами (0 - выход): ')
#	if str == '0': break
#	lst_in.append(list(str.split(' ')))

# Подсчет повторяющихся элементов
for i in range (len(lst_in)):
	for j in range (len(lst_in[i])):
		if (lst_in[i])[j] not in d_out: d_out[(lst_in[i])[j]] = 1
		elif (lst_in[i])[j] in d_out: d_out[(lst_in[i])[j]] += 1

# Вывод
for i in d_out:
	if d_out[i] >= count:
		count = d_out[i]
		elem = i
print('* ', elem, ' * ', 'найдено ', d_out[elem], ' раз', sep='')
