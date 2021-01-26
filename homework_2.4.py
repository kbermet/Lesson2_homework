string = input('Enter several words: ')

my_list = string.split()

for ind, el in enumerate(my_list, 1):
    print(ind, el)
