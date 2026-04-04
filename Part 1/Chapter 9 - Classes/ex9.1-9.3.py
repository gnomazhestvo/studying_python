# 9.1. Ресторан.
# Создайте класс Restaurant. Его метод __init__() должен
# содержать два атрибута: restaurant_name и cuisine_type.
# Создайте метод describe_restaurant(), который выводит два
# атрибута, и метод open_restaurant(), который выводит
# сообщение о том, что ресторан открыт.
# 
# Создайте на основе своего класса экземпляр restaurant.
# Выведите два атрибута по отдельности, затем вызовите оба
# метода.

print("9.1. Ресторан.\n")

class Rest:
    """класс ресторан..."""
    
    def __init__(self, rest_name, cuisine_type, time_from, time_to):
        """инициализирует атрибуты"""
        self.rest_name = rest_name
        self.cuisine_type = cuisine_type
        self.time_from = time_from
        self.time_to = time_to
    
    def describe_rest(self):
        print(f'Ресторан "{self.rest_name}", кухня - {self.cuisine_type}.')

    def open_rest(self):
        print(f'Ресторан открыт с {self.time_from} до {self.time_to}')

rest_0 = Rest('Nomi', 'китайская', '9:00', '18:00')

print(rest_0.rest_name)
print(rest_0.cuisine_type)
print()

rest_0.describe_rest()
rest_0.open_rest()