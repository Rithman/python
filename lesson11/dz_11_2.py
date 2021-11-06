class MyZeroDivisionErr(Exception):
    def __init__(self, text):
        self.text = text


dividend = input('Введите делимое: ')
divider = input('Введите делитель: ')

try:
    if eval(divider) == 0:
        raise MyZeroDivisionErr('\033[31mОШИБКА: Нельзя делить на ноль!\033[0m')
except (MyZeroDivisionErr, ValueError) as err:
    print(err)
else:
    print(f' {dividend} / {divider} = {eval(dividend) / eval(divider)}')
finally:
    print('Завершение работы программы')
