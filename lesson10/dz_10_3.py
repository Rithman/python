class Cell:
    def __init__(self, num):
        self.num = int(num)

    def __add__(self, other):
        return self.num + other.num

    def __sub__(self, other):
        if self.num < other.num:
            raise ValueError("Количество не может быть отрицтельным!")
        else:
            return self.num - other.num

    def __mul__(self, other):
        return self.num * other.num

    def __floordiv__(self, other):
        if other.num == 0:
            raise ZeroDivisionError("Нельзя делить на ноль!")
        else:
            return self.num // other.num

    def __truediv__(self, other):
        if other.num == 0:
            raise ZeroDivisionError("Нельзя делить на ноль!")
        else:
            return self.num / other.num

    def make_order(self, in_row):
        nl = '\n'
        return f'Упорядоченный вид клеток ({self.num} по {in_row} в ряд):{nl}' + f'{"*" * in_row}{nl}' * \
               (self.num // in_row) + f'{"*" * (self.num % in_row)}'



cell_1 = Cell(20)
cell_2 = Cell(10)
print(f'Результат сложения: {cell_1 + cell_2}')
print(f'Результат вычитания: {cell_1 - cell_2}')
print(f'Результат умножения: {cell_1 * cell_2}')
print(f'Результат целочисленного деления: {cell_1 // cell_2}')
print(f'Результат деления: {cell_1 / cell_2}')

print(cell_1.make_order(6))