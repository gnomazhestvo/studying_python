### 5.1. Проверка условий.
print(1)
car = 'subaru'
print('Is car Subaru? I predict True.')
print(car == 'subaru')
print()

print(2)
print('Is car - Audi? I predict False.')
print(car == 'Audi')
print()

print('3. Проверка равенства и неравенства строк')
string_1 = 'hello'
string_2 = 'world'
string_3 = 'hello'
string_4 = 'world'
print(string_1 == string_2)
print(string_1 == string_2 or string_1 == string_3)
print(string_1 == string_3 and string_2 == string_4)
print()

print('4. Проверка с использованием метода .lower()')
asses = ['Andrew', 'bootie', 'momnster', 'SKRILLEX']
print('skrillex' in [ass.lower() for ass in asses])