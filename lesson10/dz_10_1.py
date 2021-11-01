class Matrix:
    def __init__(self, array):
        self.array = array

    def __add__(self, other):
        if len(self.array) == len(other.array):
            lenght = len(self.array[0])
            for row in self.array:
                if len(row) != lenght:
                    raise ValueError(self, other)
            for row2 in other.array:
                if len(row2) != lenght:
                    raise ValueError(self, other)
            result = []
            numbers = []
            for i in range(len(self.array)):
                for j in range(len(self.array[0])):
                    summa = other.array[i][j] + self.array[i][j]
                    numbers.append(summa)
                    if len(numbers) == len(self.array[0]):
                        result.append(numbers)
                        numbers = []
            return Matrix(result)
        else:
            raise ValueError(self, other)

    def __str__(self):
        return '\n'.join(['\t'.join([str(el) for el in row]) for row in self.array])


# Почти все по кускам слизано с инета... чуствую себя тупым...
# Изначально в __add__ был генератор списков, и он сам по себе работал, но что бы ни было в __str__ результат выводился
# в виде обычного списка, а не столбиком. Не понимаю почему так...


matrix_1 = Matrix([[1, 2, 3, 4], [2, 4, 6, 8], [2, 4, 3, 1]])
matrix_2 = Matrix([[3, 3, 5, 5], [4, 3, 5, 7], [3, 4, 7, 2]])
matrix_3 = matrix_1 + matrix_2
print(matrix_3)