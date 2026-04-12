print()

### словари могут быть заключены в списки:

# alien_0 = {
#     'color' : 'green',
#     'points' : '5',
# }
# alien_1 = {
#     'color' : 'yellow',
#     'points' : '10',
# }
# alien_2 = {
#     'color' : 'red',
#     'points' : '15',
# }
# 
# aliens = [alien_0, alien_1, alien_2]
# 
# for alien in aliens:
#     print(alien)
# print()

### Создание армады из 30 пришельцев:
aliens = []
points = 0

for alien_number in range (0, 119):
    alien = {
        'color' : 'green',
        'points' : 5,
        'speed' : 'slow',
    }
    aliens.append(alien)

# ускорение первых трех пришельцев:
for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = 10
        alien['speed'] = 'medium'

for alien in aliens[0:2]:
    if alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['points'] = 15
        alien['speed'] = 'fast'        

print(f'На нас надвигаются пришельцы:')
print()

# вывод информации о первых пяти пришельцах:
for alien in aliens[0:5]:
    print(alien)
if len(aliens) > 5:
    print('...')
    print('И еще ', len(aliens)-5, ' шт.')

print()
print('Общее количество очков за всех пришельцев:')
for alien in aliens:
    for key, value in alien.items():
        if key == 'points':
            points = points + value
print(points)