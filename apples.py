# Get info from user
n = input('Please enter number of pupils are in the classroom?: ')
k = input('Please enter number of apples are the basket?: ')
pupils = int(n)
apples = int(k)
# Some very scientific operations
print('Every of', pupils, ' pupils get ', (apples // pupils), ' apple(s) and ', apples - (apples // pupils) * pupils, ' apples stay in basket')
