for i in range(1, 101):
    if i % 10 == 1 and i != 11:
        print(f'{i} процент')
    elif (i >= 11 and i <= 14) or (i % 10 >= 5 and i % 10 <= 9) or i % 10 == 0:
        print(f'{i} процентов')
    elif i % 10 >= 2 and i % 10 <= 4:
        print(f'{i} процента')