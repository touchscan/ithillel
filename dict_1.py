s = input('Введите строку, разделяя слова пробелами: ')
lst = list(s.split(' '))
d = {i: lst[i] for i in range(len(lst))}
dd = {lst[i]:0 for i in range(len(lst))}
for a in range(len(lst)):
	count = 1
	for b in range(len(lst)):
		if (d[a] == d[b] and a != b): count += 1
	if (count > int(dd.get(d[a]))): dd[d.get(a)] = count
for i in dd: print('* ', i, ' *  найдено ', dd[i], sep='')
