duration = int(input('Введите количество секунд: '))

if duration >= 0 and duration <= 60:
    print(f'{duration} сек')
elif duration > 60 and duration < 3600:
    print(f'{duration // 60} мин {duration % 60} сек')
elif duration >= 3600 and duration < 86400:
    print(f'{duration // 3600} час {(duration % 3600) // 60} мин {duration % 60} сек')
elif duration >= 86400:
    print(f'{duration // 86400} дн {(duration % 86400) // 3600} час {(duration % 3600) // 60} мин {duration % 60} сек')
else:
    print('Количество секунд должно быть положительным')
