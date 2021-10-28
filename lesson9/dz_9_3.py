class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = str(name)
        self.surname = str(surname)
        self.position = str(position)
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):
    def get_full_name(self):
        print(f'Full name: {self.name} {self.surname}\nPosition: {self.position}')

    def get_total_income(self):
        print(f'Total income: {sum(x for x in self._income.values())}')


worker_1 = Position('John', 'Wick', 'Boogeyman', 100000, 50000)
worker_1.get_full_name()
worker_1.get_total_income()
