# 6.7. Люди.
# Начните с программы, написанной для упражнения 6.1.
# Создайте два новых словаря, представляющих разных людей,
# и сохраните все три словаря в списке people. Переберите
# элементы списка людей. В процессе перебора выведите всю
# имеющуюся информацию о каждом человеке.
print()
print('6.7. Люди.')
print()

person_0 = {
    'first_name' : 'nastya',
    'last_name' : 'shkurina',
    'age' : 25,
    'city' : 'tyumen',
    'sex' : 'female'
    }
person_1 = {
    'first_name' : 'lev',
    'last_name' : 'konstantinov',
    'age' : 29,
    'city' : 'tyumen',
    'sex' : 'male'
}
person_2 = {
    'first_name' : 'boris',
    'last_name' : 'the cat',
    'age' : 6,
    'city' : 'yekaterinburg',
    'sex' : 'animal'
}

people = [person_0, person_1, person_2,]

for person in people:
    if person['sex'] == 'male':
        pronoun = 'He'
    elif person['sex'] == 'female':
        pronoun = 'She'
    else:
        pronoun = 'It'
    print(f"{person['first_name'].title()} {person['last_name'].title()}"
          f" is {person['age']} years being. {pronoun} lives in {person['city'].title()}.")
    print()
print()

# 6.8. Домашние животные.
# Создайте несколько словарей, имена
# которых представляют клички домашних животных. В каждом
# словаре сохраните информацию о виде животного и имени
# владельца. Сохраните словари в списке pets. Переберите
# элементы списка. В процессе перебора выведите всю имеющуюся
# информацию о каждом животном.
print('6.8. Домашние животные.')
print()

boris = {
    'name' : 'boris',
    'type' : 'cat',
    'age' : '6',
    'sex' : 'male',
    'owner' : 'lev',
    'location' : 'yekaterinburg',
}
rex = {
    'name' : 'rex',
    'type' : 'dog',
    'age' : '4',
    'sex' : 'male',
    'owner' : 'alex',
    'location' : 'sidelnikovo',
}
fogli = {
    'name' : 'fogli',
    'type' : 'turtle',
    'age' : '4',
    'sex' : 'female',
    'owner' : 'mom',
    'location' : 'pavlodar',
}

animals = [boris, rex, fogli,]

for animal in animals:
    name = animal.get('name', 'Unknown')
    print(name.title())

    for key, value in animal.items():
        if key == 'name':
            continue
        print(f'  {key.title()}: {value.title()}')
    print()
print()