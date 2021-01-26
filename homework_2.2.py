a = int(input('Enter a: '))
b = int(input('Enter b:'))
d = int(input('Enter d:'))

my_list = [a, b, d]
print(my_list)
var_1, var_2 = a, b
var_1, var_2 = var_2, var_1
print(var_1, var_2, d)
