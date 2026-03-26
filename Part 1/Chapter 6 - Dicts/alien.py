print()

alien_0 = {
        'color':'green',
        'points':5,
           }

### обращение к ключам в словаре:
print(alien_0['color'])
print(alien_0['points'])

new_points = alien_0['points']
print(f'You have just earned {new_points} points!')
print()

### добавление ключей в словарь:
print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)
print()

### создрание пустого словаря и его заполнение:
empty_dict = {}
for key in range (1, 6):
    empty_dict[key] = key**2
print(empty_dict)
print()

### изменение значений в словаре:
alien_0 = {'color' : 'green'}
print(f'The alien is {alien_0['color']}.')

alien_0['color'] = 'yellow'
print(f'The alien is damaged and is {alien_0['color']} now!')
print()


### отслеживание позиции пришельца:
alien_0 = {
    'x_position' : 0,
    'y_position' : 25,
    'speed' : 'medium'
}

alien_0['speed'] = 'fast'

print(f"Alien's position: [{alien_0['x_position']}, {alien_0['y_position']}].")

if alien_0['speed'] == 'slow':
    x_increment = 1
    y_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
    y_increment = 2
elif alien_0['speed'] == 'fast':
    x_increment = 3
    y_increment = 3

print(f'Alien moves with {alien_0['speed']} speed.')
print()

alien_0['x_position'] = alien_0['x_position'] + x_increment
alien_0['y_position'] = alien_0['y_position'] + y_increment

print(f"Alien's position: [{alien_0['x_position']}, {alien_0['y_position']}]")
print()


### удаление пар "ключ - значение":
alien_0['color'] = 'green'
print(alien_0)

del alien_0['color']
print(alien_0)