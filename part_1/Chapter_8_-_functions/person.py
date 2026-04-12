print()

def build_person(first_name, last_name, age = '', sex = '', country = ''):
    """Возвращет словарь с информацией о человеке"""
    person = {
        'first' : first_name,
        'last' : last_name,
    }
    if age:
        person['Возраст'] = age
    if sex:
        person['Пол'] = sex
    if country:
        person['Происхождение'] = country
    return person

musicians = []

musicians.append(build_person('jimmi', 'hendrix'))
musicians.append(build_person('lev', 'volkov', 29, 'M', 'Uzb'))
musicians.append(build_person('oxxxy', 'miron', 43, 'm', 'Россия'))

print('Список музыкантов:')
for musician in musicians:
    print(f'{musician['first'].title()} {musician['last'].title()}. \nИнформация:')
    for key, value in musician.items():
        if key == 'first' or key == 'last':
            continue
        else:
            print(f'{key.title()}: {value}')
    print()