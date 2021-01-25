name = input('Enter a product name: ')
price = input('Enter a product price: ')
currency = input('Enter product currency: ')
quantity = input('Enter product quantity: ')

my_dict= {'1':'1', 'name': name, 'price':price, 'currency':currency, 'quantity':quantity}
for key, value in my_dict.items():
    print(f'{key} - {value}')




