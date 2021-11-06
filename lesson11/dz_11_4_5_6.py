# Понимаю, что тут много копипаста и как-то можно было бы это оптимизировать, но моё психическое здоровье и так уже
# пошатнулось, пока я это писал) Плюс, не все переменные-счетчики задействованы, но это типа на будущее.



eq_list = {}


class Store:
    pr_in_store_count = 0
    sc_in_store_count = 0
    pc_in_store_count = 0
    eq_in_store = {}

    @staticmethod
    def check_value(num):
        if num.isdigit():
            return True
        else:
            return False

    @classmethod
    def receive_eq(cls):
        try:
            eq_type = input(f'Enter the equipment to get {Printer.instances}{Scanner.instances}{PC.instances}): ')
            if eq_type in Printer.instances:
                eq_num = input('Enter the number of equipment to get to the Store: ')
                if Store.check_value(eq_num):
                    if int(eq_num) > eq_list[eq_type]:
                        raise ValueError(f'\033[31mError: Only {eq_list[eq_type]} printer(s) available \033[0m')
                    else:
                        Store.pr_in_store_count += int(eq_num)
                        eq_list[eq_type] -= int(eq_num)
                        Printer.printer_count -= int(eq_num)
                        if eq_type in Store.eq_in_store:
                            Store.eq_in_store[eq_type] += int(eq_num)
                        else:
                            Store.eq_in_store[eq_type] = int(eq_num)
                        info()
                else:
                    raise ValueError(f'\033[31mError: Incorrect number\033[0m')
            elif eq_type in Scanner.instances:
                eq_num = input('Enter the number of equipment to get to the Store: ')
                if int(eq_num) > eq_list[eq_type]:
                    raise ValueError(f'\033[31mError: Only {eq_list[eq_type]} scanner(s) available \033[0m')
                else:
                    Store.sc_in_store_count += int(eq_num)
                    eq_list[eq_type] -= int(eq_num)
                    Scanner.scanner_count -= int(eq_num)
                    if eq_type in Store.eq_in_store:
                        Store.eq_in_store[eq_type] += int(eq_num)
                    else:
                        Store.eq_in_store[eq_type] = int(eq_num)
                    info()
            elif eq_type in PC.instances:
                eq_num = input('Enter the number of equipment to get to the Store: ')
                if int(eq_num) > eq_list[eq_type]:
                    raise ValueError(f'\033[31mError: Only {eq_list[eq_type]} PC(s) available \033[0m')
                else:
                    Store.pc_in_store_count += int(eq_num)
                    eq_list[eq_type] -= int(eq_num)
                    PC.pc_count -= int(eq_num)
                    if eq_type in Store.eq_in_store:
                        Store.eq_in_store[eq_type] += int(eq_num)
                    else:
                        Store.eq_in_store[eq_type] = int(eq_num)
                    info()
            else:
                raise ValueError('\033[31mError: Incorrect equipment\033[0m')
        except ValueError as e:
            print(e)


class Equipment:
    eq_overall_count = 0

    def __int__(self, name, price):
        self.name = name
        self.price = price
        Equipment.eq_overall_count += 1


class Printer(Equipment):
    printer_count = 0
    instances = set()

    def __init__(self, name, price, dpi):
        self.name = name
        self.price = price
        self.dpi = dpi
        self.instances.add(self.name)
        Printer.printer_count += 1
        Equipment.eq_overall_count += 1
        if self.name in eq_list:
            eq_list[self.name] += 1
        else:
            eq_list[self.name] = 1

    def __str__(self):
        return f"name: {self.name}, price: {self.price}, dpi: {self.dpi}"


class Scanner(Equipment):
    scanner_count = 0
    instances = set()

    def __init__(self, name, price, ppi):
        self.name = name
        self.price = price
        self.ppi = ppi
        self.instances.add(self.name)
        Scanner.scanner_count += 1
        Equipment.eq_overall_count += 1
        if self.name in eq_list:
            eq_list[self.name] += 1
        else:
            eq_list[self.name] = 1

    def __str__(self):
        return f"name: {self.name}, price: {self.price}, ppi: {self.ppi}"


class PC(Equipment):
    pc_count = 0
    instances = set()

    def __init__(self, name, price, cpu, ram):
        self.name = name
        self.price = price
        self.cpu = cpu
        self.ram = ram
        self.instances.add(self.name)
        PC.pc_count += 1
        Equipment.eq_overall_count += 1
        if self.name in eq_list:
            eq_list[self.name] += 1
        else:
            eq_list[self.name] = 1

    def __str__(self):
        return f"name: {self.name}, price: {self.price}, cpu: {self.cpu}, ram: {self.ram}"


class Department:
    instances = set()

    def __init__(self, name):
        self.name = name
        self.eq_in_department = {}
        self.instances.add(self.name)

    def receive_eq_from_store(self):
        try:
            eq_type = input(f'Enter the equipment to transfer from the Store {Store.eq_in_store}: ')
            if eq_type in Store.eq_in_store:
                eq_num = input('Enter the number of equipment to receive: ')
                if Store.check_value(eq_num):
                    if int(eq_num) > Store.eq_in_store[eq_type]:
                        raise ValueError(f'\033[31mError: Only {eq_list[eq_type]} available in the Store\033[0m')
                    else:
                        Store.eq_in_store[eq_type] -= int(eq_num)
                        if eq_type in self.eq_in_department:
                            self.eq_in_department[eq_type] += int(eq_num)
                        else:
                            self.eq_in_department[eq_type] = int(eq_num)
                        info()
                        print(f'Equipment in the {self.name} department : {self.eq_in_department}')
                else:
                    raise ValueError(f'\033[31mError: Incorrect number\033[0m')
            else:
                raise ValueError('\033[31mError: Incorrect equipment\033[0m')
        except ValueError as e:
            print(e)


pr_1 = Printer('Canon LBP 2900', 6000, 600)
pr_2 = Printer('Canon LBP 2900', 6000, 600)
pr_3 = Printer('Canon LBP 2900', 6000, 600)
sc_1 = Scanner('Epson V19', 8500, 4800)
sc_2 = Scanner('Epson V19', 8500, 4800)
sc_3 = Scanner('Epson V19', 8500, 4800)
pc_1 = PC('Office PC', 60000, 'Intel Core i5', 16)
pc_2 = PC('Office PC', 60000, 'Intel Core i5', 16)
pc_3 = PC('Office PC', 60000, 'Intel Core i5', 16)

dep_1 = Department('Accounting')
dep_2 = Department('Supply')


def info():
    print(f'Available Equipment: {eq_list}')
    print(f'\tPrinters: {Printer.printer_count}')
    print(f'\tScanners: {Scanner.scanner_count}')
    print(f'\tPCs: {PC.pc_count}')
    print(f'Equipment in the Store: {Store.eq_in_store}')


print(pr_1)
print(sc_1)
print(pc_1)

info()

if __name__ == '__main__':
    Store.receive_eq()
    dep_2.receive_eq_from_store()
