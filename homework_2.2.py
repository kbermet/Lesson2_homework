a = int(input('Enter a: '))
b = int(input('Enter b:'))
c = int(input('Enter c:'))

my_list = [a, b, c]
print(my_list)
var_1, var_2 = a, b
var_1, var_2 = var_2, var_1
print(var_1, var_2, c)
