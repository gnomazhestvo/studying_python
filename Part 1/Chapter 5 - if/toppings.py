requested_topping = 'mushrooms'
needed_topping = 'Anchovies'
if requested_topping != needed_topping:
    print(f'Hold the {needed_topping}!')

requested_toppings = ['mushrooms', 'onions', 'pineapple']

is_mushrooms_in_toppings = 'Mushrooms' in [requested_topping.lower() for requested_topping in requested_toppings]
print(is_mushrooms_in_toppings)
