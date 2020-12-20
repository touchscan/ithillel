gradebook = {}
file_in = open('src_14.txt', encoding='utf-8')
while True:
    name = file_in.readline(30)
    if name != '':
        grade = file_in.readline()
        grade = grade.strip('\n')
        grade = grade.split()
        gradebook.setdefault(name, grade)
    else:
        break
file_in.close()


def average_score(book, val=1):
    t = c = res = 0
    for n, g in book.items():
        tmp = count = 0
        if val:
            for i in range(len(g)):
                tmp += int(g[i])
                count += 1
            book[n] = round(tmp / count, 2)
        else:
            t += g
            c += 1
            res = round(t / c, 2)
    return (res)


def output(x, y, z, s, t=1):
    if t:
        print(x + s * (z - len(x)), y)
    else:
        x = x.split()
        y = str(y)
        return (x[1] + ' ' + x[0][0:1] + '.' + s * (z - len(x[1])) + y + '\n')


average_score(gradebook)
for name, grade in gradebook.items():
    if grade < 5: output(name, grade, 30, ' ')

output('-', '', 30, '-')
output('Средний балл класса', average_score(gradebook, 0), 30, ' ')

file_out = open('src_14_out.txt', 'w', encoding='utf-8')
for name, grade in gradebook.items():
    data = output(name, grade, 20, ' ', 0)
    file_out.write(data)

file_out.close()
