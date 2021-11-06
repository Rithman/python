class Date:
    def __init__(self, date):
        self.date_str = date

    @classmethod
    def get_date(cls, obj):
        d, m, y = obj.date_str.split('-')
        return int(d), int(m), int(y)

    @staticmethod
    def validate(obj):
        d, m, y = Date.get_date(obj)
        if (y % 4 == 0) and (y % 100 != 0) or (y % 400 == 0):
            leap_y = True
        else:
            leap_y = False

        try:
            if d > 31 or (d > 30 and m in (4, 6, 9, 11) or (d > 29 and m == 2 and leap_y == True)
                            or (d > 28 and m == 2 and leap_y == False) or m > 12):
                raise ValueError('\033[31mОшибка: Некорректная дата!\033[0m')
        except ValueError as err:
            print(err)
        else:
            print(f'Корректная дата: {d:02}.{m:02}.{y}')


d_1 = Date('05-11-2021')
Date.validate(d_1)

# О наболевшем: не поянл из условия можно ли передавать объект в метод валидации. Можно было бы передавать данные через
# staticmethod и работать потом с ними, но в условии, вроде как, написано, что именно конструктор должен принимать их...
