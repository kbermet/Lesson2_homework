# number = 0
# while number < 3:
#     name = input('Enter a product name: ')
#     price = input('Enter a product price: ')
#     currency = input('Enter product currency: ')
#     quantity = input('Enter product quantity: ')
#     number +=1
#
#     my_dict= [
#                 (1, {'name': name, 'price': price, 'currency': currency, 'quantity': quantity}),
#                 (2, {'name': name, 'price': price, 'currency': currency, 'quantity': quantity}),
#                 (3, {'name': name, 'price': price, 'currency': currency, 'quantity': quantity})
#         ]
#
# for key, value in my_dict:
#     print(f'{key} - {value}')
# выше это как я пыталась сделать, ниже это адаптация из интернета, времени не хватило разобрать до конца самостоятельно. Простите )

products, order = [], 1
title, price, amount = None, None, None

while True:
    if title is None:
        tmp = input('Enter product name: ')
        if not tmp.isalnum():
            print('Enter produc name. Try again.')
            continue

        title = tmp

    if price is None:
        tmp = input('Enter product price: ')
        if not tmp.isdigit():
            print('Enter product price, please try again.')
            continue

        price = int(tmp)

    if amount is None:
        tmp = input('Enter quantity: ')
        if not tmp.isdigit():
            print('Enter quantity number, try again.')
            continue

        amount = int(tmp)

    tmp = input('Enter item title: ')
    if not tmp.isalpha():
        print('Try again.')
        continue

    unit = tmp

    products.append((
        order,
        {
            'title': title,
            'price': price,
            'amount': amount,
            'unit': unit
        }
    ))

    title, price, amount = None, None, None
    order += 1

    print(products)

    q = input('Did you enter all products? (y/N)) ')
    if q.lower() == 'y':
        break

analitics = {
    'title': [],
    'price': [],
    'amount': [],
    'unit': set()
}

for _, item in products:
    analitics['title'].append(item['title'])
    analitics['price'].append(item['price'])
    analitics['amount'].append(item['amount'])
    analitics['unit'].add(item['unit'])

print(analitics)

