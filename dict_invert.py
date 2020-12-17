import pprint
d = {
    'apple': ['malum', 'pomum', 'popula'],
    'fruit': ['baca', 'bacca', 'popum'],
    'punishment': ['malum', 'multa']
}
print('Исходный словарь:')
pprint.pprint(d)
p = {}
for i in d:
	j = tuple(d.get(i))
	p[j] = i
print('Инвертированный словарь:')
pprint.pprint(p)
