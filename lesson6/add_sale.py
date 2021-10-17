from sys import argv

sale = argv[1]
with open('bakery.csv', 'a', encoding='utf-8') as f:
    f.write(f'{str(sale)}' + (' ' * (10-len(str(sale)))) + '\n')  # Максимум - число в 10 знаков, включая запятую.
