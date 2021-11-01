from abc import ABC, abstractmethod


class Clothing(ABC):
    @abstractmethod
    def value(self):
        pass

    def __add__(self, other):
        return self.value() + other.value()


class Coat(Clothing):
    def __init__(self, value):
        self.v = value

    # если тут прикрутить @property получаю ошибку float objeсt is not callable
    def value(self):
        return self.v / 6.5 + 0.5


class Costume(Clothing):
    def __init__(self, height):
        self.h = height

    # а тут с @property ошибки нет, но она есть при суммировании
    def value(self):
        return self.h * 2 + 0.3


coat_1 = Coat(11)
print(f'Расход ткани на пальто: {coat_1.value()}')

costume_1 = Costume(12)
print(f'Расход ткани на костюм: {costume_1.value()}')
print(f'Суммарный расход ткани: {costume_1 + coat_1}')

# в итоге суть @property и setter понять не удалось... Нигде не объясняется почему используются приватные переменные
# без приватных __value у меня в тестах откуда-то появлялась рекурсия. Как видимость переменной на это влияет
# категорически не понятно. Все действо же происходит в рамках класса.