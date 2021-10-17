from sys import argv

with open('bakery.csv', 'r', encoding='utf-8') as f:
    fline = f.readlines()

if len(argv) == 1:
    with open('bakery.csv', 'r', encoding='utf-8') as f:
        print(f.read())
elif len(argv) == 2:
    with open('bakery.csv', 'r', encoding='utf-8') as f:
        start = str(argv[1])
        print(*fline[int(start)-1:])
elif len(argv) == 3:
    with open('bakery.csv', 'r', encoding='utf-8') as f:
        start = str(argv[1])
        stop = str(argv[2])
        print(*(fline[int(start)-1:int(stop)]))
else:
    print('Must be 2 integer arguments at most ')

# Пробовал в начале открыть файл на чтение просто через f = open(...), чтобы не открывать его каждый раз в if-else,
# но так почему-то не работает. Пришлось открывать в каждом условии.
