class Dog:
    """Простая модель собаки"""

    def __init__ (self, name, age):
        """Инициализирует атрибуты name и age"""
        self.name = name
        self.age = age
    
    def sit(self):
        """Команда сидеть"""
        print(f"{self.name} садится.")

    def roll_over(self):
        """Команда перекатиться"""
        print(f"{self.name} перекатывается.")

my_dog = Dog('Willie', 6)
your_dog = Dog('Lucy', 3)

print()

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()
my_dog.roll_over()
print()

print(f"Your dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")
your_dog.sit()
your_dog.roll_over()
print()