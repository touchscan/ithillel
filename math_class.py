# Число мест за одной партой
desk_seat = 2
# Инфа от пользователя
stud_a = int(input('Please, enter how many studs in class a:'))
stud_b = int(input('Please, enter how many studs in class b:'))
stud_c = int(input('Please, enter how many studs in class c:'))
# Берем счеты и пытаемся считать
desk_a = stud_a - ((stud_a // desk_seat) * 2) + (stud_a // desk_seat)
desk_b = stud_b - ((stud_b // desk_seat) * 2) + (stud_b // desk_seat)
desk_c = stud_c - ((stud_c // desk_seat) * 2) + (stud_c // desk_seat)
total_desk = desk_a + desk_b + desk_c
print('Your classes need ', total_desk, ' desks')
