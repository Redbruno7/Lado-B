# MENU - REGISTER PRODUCT / LIST OF PRODUCTS / EXIT
# Date: 26/11/2024

import os


os.system('cls')

# Title
print('=' * 70)
print('Menu - E-commerce system')
print('=' * 70)
print()

# Input
product_list = []

# Iteration menu
while True:
    print('=' * 70)
    print('1. Register product')
    print('2. List products')
    print('3. Exit')
    print('-' * 70)
    option = input('Choose an option: ')
    print('=' * 70)
    print()
    
    # Condition menu
    if option == '1':
        print('=' * 70)
        print('Product Register:')
        print('-' * 70)
        name = input('Product: ')
        print('-' * 70)
        value = float(input('Price: '))
        print('-' * 70)
        category = input('Category: ')
        print('=' * 70)
        print()
        
        # Tuple in list
        product = {'name': name, 'value': value, 'category': category}
        product_list.append(product)

    elif option == '2':
        print('=' * 70)
        print('Registered Products:')

        # Condition of listing
        if len(product_list) == 0:
            print('-' * 70)
            print('There is no product registered.')
            print('=' * 70)
            print()
            # continue?
        else:
            # Iteration list
            for i in product_list:
                print('-' * 70)
                print(f"Name: {i['name']} | "
                      f"Value: R$ {i['value']} | Category: {i['category']}")
            print('=' * 70)
            print()
    
    elif option == '3':
        print('=' * 70)
        print('Shutting down the system...')
        print('=' * 70)
        break
    
    else:
        print('=' * 70)
        print('Invalid option. Please, try again.')
        print('=' * 70)
        print()