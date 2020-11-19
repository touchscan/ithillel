str = input('Введите любую строку: ')
strlen = len(str)
first = str.find('h', 0, strlen-1)
last = str.rfind('h', first+1, strlen)
tmp = str[first+1: last].replace('h', 'H')
result = str[first] + tmp + str[last:strlen]
print(result)

