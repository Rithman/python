class Road:

    def __init__(self, len, wid):
        self._length = float(len)
        self._width = float(wid)

    def count(self):
        return self._length * self._width * 25 * 5 / 1000  # не понял формулу из задания. 5 и 25 это константы?


r_1 = Road(20, 5000)
print(r_1.count())
