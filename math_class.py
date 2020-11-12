# Число мест за одной партой
desk_seat = 2
# Инфа от пользователя
stud_a = input('Please, enter how many studs in class a:')
stud_b = input('Please, enter how many studs in class b:')
stud_c = input('Please, enter how many studs in class c:')
# Преобразуем str в int
stud_a = int(stud_a)
stud_b = int(stud_b)
stud_c = int(stud_c)
# Берем счеты и пытаемся считать
total_stud = stud_a + stud_b + stud_c
total_desk = total_stud // desk_seat
if total_stud % desk_seat:
    total_desk += 1
print('Your classes need ', total_desk, ' desks')
