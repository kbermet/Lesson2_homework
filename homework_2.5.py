
number = int(input('Enter a rating number from 0 to 9: '))
rating = [9, 7, 5, 4, 4, 2, 1]
# new_rating = []

if number == 1:
    rating.append(1)
    print(rating)

elif number == 9:
    rating.insert(0, 9)
    print(rating)

elif number == 8:
    rating.insert(1, 8)
    print(rating)

elif number == 7:
    rating.insert(2, 7)
    print(rating)

elif number == 6:
    rating.insert(2, 6)
    print(rating)

elif number == 5:
    rating.insert(3, 5)
    print(rating)

elif number == 4:
    rating.insert(4, 4)
    print(rating)

elif number == 3:
    rating.insert(5, 3)
    print(rating)

elif number == 2:
    rating.insert(5, 2)
    print(rating)

