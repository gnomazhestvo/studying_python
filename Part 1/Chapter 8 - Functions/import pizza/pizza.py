def make_pizza(size, *toppings):
    print(f'Make {size}-inch pizza with following toppings:')
    for topping in toppings:
        print(f'- {topping}')