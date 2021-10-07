num = {'zero': 'ноль', 'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять',
       'six': 'шесть', 'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}


def num_translate(digit):
    if digit[0].isupper():
        num_cap = dict((k.capitalize(), v.capitalize()) for k, v in num.items())
        print(f'Перевод: {num_cap.get(digit.capitalize())}')
    else:
        print(f'Перевод: {num.get(digit)}')


num_translate(input('Введите на английском числительное от 0 до 10 : '))

# не могу понять почему не работает такой вариант?
#
# def num_translate(digit):
#     if digit[0] .isupper():
#         num.setdefault(digit.capitalize(), num[digit].capitalize())
#         print(f'Перевод: {num.get(digit.capitalize())}')
#     else:
#         print(f'Перевод: {num.get(digit)}')
