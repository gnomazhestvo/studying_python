# 8.12. Бутерброды.
# Напишите функцию, которая получает список компонентов
# бутерброда. Функция должна иметь один параметр для любого
# количества значений, переданных при вызове функции, и
# выводить описание заказанного бутерброда. Вызовите функцию
# три раза с разными количествами аргументов.

print('\n8.12. Бутерброды.\n')

def sandwich_components(*args):
    print('Компоненты бутерброда:')
    for arg in args:
        print(f'- {arg}')
    print()

sandwich_components('помидоры')
sandwich_components('сыр', 'масло', 'колбаса')
sandwich_components('огурцы', 'лосось', 'крем-чиз', 'креветки')

print('=== === ===')

# 8.13. Профиль.
# Начните с копии программы user_profile.py, приведенной в
# этом подразделе. Создайте собственный профиль с помощью
# вызова build_profile(), укажите имя, фамилию и три другие
# пары «ключ — значение» для вашего описания.
#
# копия программы user_profile.py:
# def build_profile(first, last, **user_info):
#    user_info['first name'] = first
#    user_info['last name'] = last
#    return user_info
#
# user_profile = build_profile('albert', 'einstein',
#                              location = 'princeton',
#                              field = 'physics')
# print(user_profile)

print('\n8.13. Профиль.\n')

def build_profile(name, surname, **user_info):
    user_info['name'] = name
    user_info['surname'] = surname
    return user_info

def print_existing_profile(user):
    print(f'Пользователь: {user['name'].title()} {user['surname'].title()}.')
    for key, value in user.items():
        if key != 'name' and key != 'surname':
            print(f'{key.title()}: {value.title()}')
    print()

user_0 = build_profile('лев', 'волков', location = 'тюмень', work = 'СИБУР', project = 'python')
user_1 = build_profile('макс', 'фрай', location = 'неизвестно', food = 'кошачий', drink = 'вода')
user_2 = build_profile('роман', 'смирнов', mother = 'best', respubliki = '204k3', girl = 'nastya', car = 'empty', birthday = 'january')
user_3 = build_profile('ганн', 'флад', race = 'ufo', suit = 'human', money = '8')

print_existing_profile(user_0)
print_existing_profile(user_1)
print_existing_profile(user_2)
print_existing_profile(user_3)

print('=== === ===')

# 8.14. Автомобили.
# Напишите функцию для сохранения данных об автомобиле в
# словаре. Она всегда должна возвращать информацию о
# производителе и названии модели, но при этом может получать
# произвольное количество именованных аргументов. Вызовите
# функцию с передачей обязательной информации и еще двух пар
# «имя — значение» (например, цвет и комплектация). Ваша
# функция должна работать для вызовов следующего вида:
#   car = make_car('subaru', 'outback', color='blue',
#       tow_package=True)
# Выведите возвращаемый словарь и убедитесь в том, что вся
# информация была сохранена правильно.

print('\n8.14. Автомобили.\n')

def return_car_info(make, model, **car_info):
    car_info['Марка'] = make
    car_info['Модель'] = model
    return car_info

car_0 = return_car_info('subaru', 'outback', color = 'blue', tow_package = True)
print(car_0)

print('=== === ===')