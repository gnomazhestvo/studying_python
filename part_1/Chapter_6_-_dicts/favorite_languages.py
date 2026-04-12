fav_langs = {
    'jen' : 'python',
    'sarah' : 'c',
    'edward' : 'rust',
    'phil' : 'python',
    }

language = fav_langs['jen']

print(f"Jen's favorite language is {language}.")
print()

# вывод через цикл всех пользователей:
for name, language in fav_langs.items():
    print(f"{name.title()}'s favoruite language is {language.title()}")
print()

# перебор ключей в словаре:
for name in fav_langs.keys():
    print(name.title())
print()

fav_friends = ['phil', 'jen']

for name in fav_langs.keys():
    if name in fav_friends:
        language = fav_langs[name]
        print(f'Hi {name.title()}! I also like {language.title()}!')
    elif name not in fav_friends:
        language = fav_langs[name]
        print(f"Oh, it's you again, {name.title()}... I don't like {language.title()}, sorry:(")
print()

# перебор значений в словаре:
print('Following languages have been mentioned:')
for lang in set(fav_langs.values()):
    print(lang.title())
print()

# добавляем в словарь списки:
fav_langs = {
    'jen' : ['python', 'rust', '1', '2', '3'],
    'sarah' : ['c'],
    'edward' : ['rust', 'go'],
    'phil' : ['python', 'haskell'],
    }

for name, languages in fav_langs.items():
    if len(languages) > 1:
        print(f"{name.title()}'s favorite languages are:")
    else:
        print(f"{name.title()}'s favorite language is:")
    for language in languages:
        print(language.title())
    print()