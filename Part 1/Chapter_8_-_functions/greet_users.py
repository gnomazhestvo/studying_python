print()

def greet_users(names):
    """Выводит простое приветствие для каждого из пользотелей"""
    for name in names:
        msg = f'Hello, {name.title()}!'
        print(msg)

usernames = 'hannah'

greet_users(usernames)