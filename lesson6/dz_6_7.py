from sys import argv

line_num = argv[1]
sale = argv[2]

f = open('bakery.csv', 'r', encoding='utf-8')
list_of_lines = f.readlines()
try:
    list_of_lines[int(line_num)-1] = (f'{str(sale)}' + (' ' * (10-len(str(sale)))) + '\n')
except IndexError:
    print('IndexError: Строки с данным номером не существует')

f = open('bakery.csv', 'w', encoding='utf-8')
f.writelines(list_of_lines)
f.close()
