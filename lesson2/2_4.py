positions_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']


for person in positions_list:
    tmp_list = person.split()
    name = tmp_list[-1]
    print(f'Привет, {name.capitalize()}!')
    print(f'{name.capitalize()}! Как дела, как семья?')

