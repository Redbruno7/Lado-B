# PRODUCT REGISTER AND LISTING
# Date: 26/11/2024

import os


os.system('cls')

# Title
print('=' * 70)
print('Product Register')
print('=' * 70)
print()

# Input
product_list = []

# Products Iteration
while True:
    print('-' * 70)
    name = input('Product: ')
    print('-' * 70)
    price = float(input('Price: '))
    print('-' * 70)
    category = input('Category: ')
    print('-' * 70)

    # Tuple in list
    product = {'name': name, 'price': price, 'category': category}
    product_list.append(product)

    # Condition break loop
    again = input('Deseja cadastrar outro produto? (s/n): ').strip().lower()

    if again != 's':
        print('-' * 70)
        print()
        break

    print('-' * 70)
    print()

# Output
print('=' * 70)
print('Registered Products')
for p in product_list:
    print('-' * 70)
    print(f"Name: {p['name']} | "
          f"Price: R$ {p['price']:.2f} | Category: {p['category']}")
print('=' * 70)