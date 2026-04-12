print()

def make_pizza(*toppings):
    print('Make pizza with following toppings:')
    for topping in toppings:
        print(f'- {topping.title()}')

make_pizza('mushrooms', 'blue cheese', 'pepper')

print()

def make_pizza_size(size, *toppings):
    print(f'Make {size}-inch pizza with following toppings:')
    for topping in toppings:
        print(f'- {topping}')

make_pizza_size(14, 'pepperoni', 'mushrooms')