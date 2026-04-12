print()

def get_formatted_name(name, surname, patronymic = ''):
    """Возвращает отформатированное полное имя"""
    if patronymic:
        full_name = f'{name} {patronymic} {surname}'
    else:
        full_name = f'{name} {surname}'
    return full_name.title()

while True:
    print('\n\nPlease tell me your name:')
    print('press "q" any time to quit\n')
    name = input('Name:\n')
    if name == 'q':
        break
    surname = input('Surname:\n')
    if surname == 'q':
        break
    patronymic = input('Patronymic:\n')
    if patronymic == 'q':
        break
    
    formatted_name = get_formatted_name(name, surname, patronymic)
    
    print()
    print(f'Hello there, {formatted_name}!')
print()