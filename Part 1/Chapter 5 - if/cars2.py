cars = ['audi', 'bMw', 'subaru', 'toyotA']
cars = [car.lower() for car in cars]
for car in cars:
    if car.lower() == 'bmw':
        print(car.upper())
    else:
        print(car.title())
    