import time


class TraficLight:
    __color = 'color'

    def running(self):  # __init__ здесь смысла делать не вижу, т.к. значений никаких не передаем при инициализации
        # объекта класса

        for i in range(3):
            color_dict = {'\033[31mКрасный\033[0m': 7, '\033[33mЖёлтый\033[0m': 2, '\033[32mЗелёный\033[0m': 7}
            for k, v in color_dict.items():
                self.__color = k
                print(f'Сигнал светофора: {k}')
                time.sleep(v)
            print(f'Сигнал светофора: \033[33mЖёлтый\033[0m')  # пытался через while вернуться на жельый свет,
            time.sleep(2)  # но получается большая вложенность, кода еще больше, и до конца так и работает


tl = TraficLight()
tl.running()
