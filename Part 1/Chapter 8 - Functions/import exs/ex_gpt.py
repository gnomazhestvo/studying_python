# Задача: “Заказы в кафе”
# 🎯 Суть
# Ты пишешь систему, которая хранит заказы клиентов. Функция
# должна выводить в формате:
# Заказ для Alex:
#  Позиции: coffee, cake
#  size: large
#  sugar: False

print('\nЗадача: “Заказы в кафе”\n')

import ex_gpt_functions as f

lev = f.get_order('lev', 'coffe', 'cake', 'shit', size = 'large', sugar = 'none')
alex = f.get_order('alex', 'coffee', 'cake', size = 'large', sugar = False)
roman = f.get_order('roman', 'americano')

f.print_order(alex)
f.print_order(lev)
f.print_order(roman)