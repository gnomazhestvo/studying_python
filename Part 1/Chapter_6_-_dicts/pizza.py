print()

pizza = {
    'crust' : 'thick',
    'toppings' : ['mushrooms', 'extra cheese']
}

print(f'You have ordered a {pizza['crust']}-crust pizza')
print(f'with following toppings:')
for topping in pizza['toppings']:
    print('   - ', topping)