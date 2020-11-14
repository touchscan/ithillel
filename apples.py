# Get info from user
n = input('Please enter number of pupils are in the classroom?: ')
k = input('Please enter number of apples are the basket?: ')
pupils = int(n)
apples = int(k)
# Some very scientific operations
print(pupils, ' pupils get ',(apples - (apples - pupils)), ' apples and ', apples - (apples // pupils) * pupils, ' apples stay in basket')
