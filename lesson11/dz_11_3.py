class MyIsDigit(Exception):
    def __init__(self, text):
        self.text = text


digit_list = []
print("Для завершения работы программы и формирования списка введите 'q' (без кавычек)")

while True:
    try:
        num = input('Введите число: ')
        if num == 'q':
            result = [eval(i) for i in digit_list]
            print(result)
            break
        elif num.replace(".", "").isdigit() == False:
            raise MyIsDigit('\033[31mОШИБКА: Можно вводить только числа!\033[0m')
        else:
            digit_list.append(num)
    except MyIsDigit as err:
        print(err)
