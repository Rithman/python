class ComplexNum:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        self.sumX = self.x + other.x
        self.sumY = self.y + other.y
        return f'Сложение: {self.sumX}  {self.sumY}j'

    def __mul__(self, other):
        self.mulX = self.x * other.x - self.y * other.y
        self.mulY = self.y * other.x + self.x * other.y
        return f'Умножение: {self.mulX}  {self.mulY}j'


x = float(input('Введите действительную часть числа "a": '))
y = float(input('Введите мнимую часть числа "a": '))
a = ComplexNum(x, y)
x = float(input('Введите действительную часть числа "b": '))
y = float(input('Введите мнимую часть числа "b": '))
b = ComplexNum(x, y)

print(a + b)
print(a * b)


