from random import choice


class Car():

    def __init__(self, speed, color, name, is_police=False):
        """Creates a car object with the following attributes: speed(int), color(str), name(str), is_police(bool)"""
        self.speed = int(speed)
        self.color = str(color)
        self.name = str(name)
        self.is_police = is_police

    def go(self):
        print(f'The {self.name} car has started to move')

    def stop(self):
        print(f'The {self.name} car has stopped')

    def turn(self, direction=choice(('left', 'right', 'backwards'))):
        self.direction = direction
        print(f'The {self.name} car turns {self.direction}')

    def show_speed(self):
        print(f'The {self.name} car has a speed of {self.speed}')


class TownCar(Car):

    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)  # не совсем понятно есть ли разница - работать с атрибутами
        # родительского класса или создавать такие же дочерние, если мы будем пересылать все атрибуты при создании

    def show_speed(self):
        if self.speed > 60:
            print(f'The {self.name} car has exceeded the speed limit of 60!')
        else:
            print(f'The {self.name} car has a speed of {self.speed}')

class WorkCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            print(f'The {self.name} car has exceeded the speed limit of 60!')
        else:
            print(f'The {self.name} car has a speed of {self.speed}')


class SportCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)

class SportCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name, is_police)

car_1 = Car(40, 'red', 'Mazda', False)
car_1.turn()
car_1.show_speed()

town_car_1 = TownCar(65, 'green', 'LADA')
town_car_1.show_speed()