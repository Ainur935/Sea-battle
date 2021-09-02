class Dot: #класс для координат точек на поле
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

class Ship:
    def __init__(self, length, beginning, line, amount_life):
        self.length = length
        self.beginning = beginning
        self.line = line
        self.amount_life = amount_life
    def dots(self):
        coord = [self.beginning]
        if self.length == 1:
            return coord
        elif self.line == 'horizont':
            for i in range(1, self.length):
                coord.append([self.beginning[0], self.beginning[1]+i])
            return coord
        else:
            for i in range(1, self.length):
                coord.append([self.beginning[0]+i, self.beginning[1]])
            return coord

ship_1 = Ship(3, [3, 1], 'horizon', 3)
print(ship_1.dots())


