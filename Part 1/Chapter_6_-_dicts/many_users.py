print()

users = {
    'aenstein' : {
        'first' : 'albert',
        'last' : 'einstein',
        'location' : 'princeton',
    },
    'mcurie' : {
        'first' : 'marie',
        'last' : 'curie',
        'location' : 'paris',
    },
}

for user, datas in users.items():
    print(f'Username: {user}')
    full_name = f'{datas['first']} {datas['last']}'
    location = datas['location']
    print(f'Full name: {full_name.title()}')
    print(f'Location: {location.title()}')
    print()