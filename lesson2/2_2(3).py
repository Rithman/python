weather = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

for i, elem in enumerate(weather):
    if elem.isdigit():
        elem = elem.zfill(2)
        elem = elem.replace(elem, ('"' + elem + '"'))
    elif '+' in elem:
        elem = elem.replace(elem, ('"+' + (elem[1:].zfill(2))) + '"')
    weather[i] = elem

weather = ' '.join(weather)
print(weather)

# Формально тут не создается второй список. Это считается за 2_3?
