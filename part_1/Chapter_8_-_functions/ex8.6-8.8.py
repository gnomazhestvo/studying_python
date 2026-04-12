# 8.6. Названия городов.
# Напишите функцию city_country(), которая получает название
# города и страну. Функция должна возвращать строку в формате:
# "Santiago, Chile" .Вызовите свою функцию по крайней мере
# для трех пар «город — страна» и выведите возвращенное
# значение.

print()
print('----- 8.6. Названия городов -----')
print()

def city_country(country, city):
    formatted_text = f'{country.title()}, {city.title()}.'
    return formatted_text

city_0 = city_country('santiago', 'chile')
city_1 = city_country('chelyabinsk', 'russia')
city_2 = city_country('bekabad', 'uzbekistan')

print(city_0)
print(city_1)
print(city_2)

# 8.7. Альбом.
# Напишите функцию make_album(), которая создает словарь с
# описанием музыкального альбома. Функция должна получать имя
# исполнителя и название альбома и возвращать словарь,
# содержащий эти два вида информации. Используйте функцию для
# создания трех словарей, представляющих разные альбомы.
# Выведите все возвращаемые значения, чтобы показать, что
# информация правильно сохраняется во всех трех словарях.
# Добавьте в make_album() дополнительный параметр для
# сохранения количества дорожек в альбоме, имеющий значение
# по умолчанию None. Если в строке вызова есть значение
# количества дорожек, то добавьте это значение в словарь
# альбома. Создайте как минимум один новый вызов функции,
# который передает количество дорожек в альбоме.

print()
print('----- 8.7 Альбом -----')
print()

def make_album(artist, album, songs = ''):
    discography = {
            'Исполнитель' : artist,
            'Название альбома' : album,
        }
    if songs:
        discography['Количество дорожек'] = songs
    return discography

albums = []

albums.append(make_album('Cold Karti', 'Снова'))
albums.append(make_album('Gruppa Skryptonite', 'Дом с нормальными явлениями'))
albums.append(make_album('Oxxxymiron', 'Волна'))
albums.append(make_album('Boulevard Depo', 'Футуроархаика', 9))

for album in albums:
    album_items = []

    for key, value in album.items():
        album_items.append(f'{key}: {value}')

    for i in range(len(album_items)):
        if i == len(album_items) - 1:
            print(f'{album_items[i]}.')
        else:
            print(f'{album_items[i]},')

# 8.8. Пользовательские альбомы.
# Начните с программы из упражнения 8.7. Напишите цикл while,
# в котором пользователь вводит данные об исполнителе и
# название альбома. Затем в цикле вызывается функция
# make_album() для введенных пользователем данных и выводится
# созданный словарь. Не забудьте предусмотреть признак
# завершения в цикле while.

print()
print('----- 8.8 Пользовательские альбом -----')
print()

albums = []

def make_album(artist, album, songs = ''):
    discography = {
            'Исполнитель' : artist,
            'Название альбома' : album,
        }
    if songs:
        discography['Количество дорожек'] = songs
    return discography

while True:
    artist = input('Введите исполнителя альбома:\n')
    album = input('Введите название альбома:\n')
    songs = input('Введите количество дорожек:\n')

    albums.append(make_album(artist, album, songs))

    print('\nНа текущий момент добавлены альбомы:')
    for album in albums:
        print(f'{album['Название альбома']}')
    print()

    continue_flag = input('Продолжить выбор? (y/n)\n')
    if continue_flag == 'y':
        print()
        continue
    else:
        print()
        break

    
print()
for album in albums:
    album_items_1 = []

    for key, value in album.items():
        album_items_1.append(f'{key}: {value}')

    for i in range(len(album_items_1)):
        if i == len(album_items_1) - 1:
            print(f'{album_items_1[i]}.')
        else:
            print(f'{album_items_1[i]},')

    print()
print()