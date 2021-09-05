class MyException(Exception):
    pass

class BoardOutException(MyException):
    def __str__(self):
        return 'Выстрел за пределы доски'

class BoardReturnException(MyException):
    def __str__(self):
        return 'Вы уже стреляли сюда'

class BoardPassException(MyException):
    pass

class Dot: #класс для координат точек на поле
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

class Ship: #класс кораблей
    def __init__(self, length, beginning, line, amount_life):
        self.length = length
        self.beginning = beginning
        self.line = line
        self.amount_life = amount_life
    @property
    def dots(self):#метод для определения всех координат корабля
        coord = [self.beginning]
        if self.length == 1:
            return coord
        elif self.line == 'horizont':
            for i in range(1, self.length):
                coord.append([self.beginning[0], self.beginning[1]+i])
            return coord
        elif self.line == 'vertikal':
            for i in range(1, self.length):
                coord.append([self.beginning[0]+i, self.beginning[1]])
            return coord
    def shooten(self, shot):
        return shot in self.dots


class Board: #класс игровой доски
    def __init__(self, hid = False, size = 6):
        self.hid = hid
        self.size = size
    self.field = [['O']* size for i in range(size)]





