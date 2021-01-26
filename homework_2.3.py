my_dict = {'Winter': (1, 2, 12),
           'Spring': (3, 4, 5),
           'Summer': (6, 7, 8),
           'Autumn': (9, 10, 11)}

num = int(input('Enter month number from 1 to 12: '))
for key in my_dict.keys():
    if num in my_dict[key]:
        print('This month is in ', key)
