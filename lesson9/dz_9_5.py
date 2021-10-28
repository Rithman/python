class Stationery:
    title = 'title'

    def draw(self):
        print(f'Запуск отрисовки {Stationery.__name__}')


class Pen(Stationery):

    def draw(self):
        print(f'Запуск отрисовки {Pen.__name__}')
        Stationery.draw(self)


class Pencil(Stationery):

    def draw(self):
        print(f'Запуск отрисовки {Pencil.__name__}')
        Stationery.draw(self)


class Handle(Stationery):

    def draw(self):
        print(f'Запуск отрисовки {Handle.__name__}')
        super().draw()

stationery_1 = Stationery()
stationery_1.draw()

pen_1 = Pen()
pen_1.draw()

pencil_1 = Pencil()
pencil_1.draw()

handle_1 = Handle()
handle_1.draw()