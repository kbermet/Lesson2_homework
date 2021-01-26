string = input('Enter some words: ')

my_list = string.split()

for ind, el in enumerate(my_list, 1):
    print(ind, el)
