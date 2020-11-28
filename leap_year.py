def is_year_leap(y):
	if ((y % 100 == 0) and (y % 400 == 0))or ((y % 4 == 0) and (y % 100 != 0)): res = True
	else: res = False
	return (res)
year = int(input('Check the year for leap: '))
print(is_year_leap(year))

