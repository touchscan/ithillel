# Get info from user
n = input('Please enter number of pupils are in the classroom?: ')
k = input('Please enter number of apples are the basket?: ')
pupils = int(n)
apples = int(k)
# Do not hurt children
att = """
Hey man!
        These are children!
                            They won't like this joke!
"""
if k >= n:
    # Some very scientific operations
    print(pupils, ' pupils get ', apples, ' apples')
    print(apples // pupils, ' apple(s) for every pupil')
    print('and ', apples - (apples // pupils) * pupils, ' apples stay in basket')
else:
    print(att)
