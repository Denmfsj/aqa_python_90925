

class Car:
    def __init__(self, make, model):
        self.make = make          # Public attribute
        self._model = model        # Protected attribute
        self.__year = 2022         # Private attribute

    def display_model(self):
        print(f"Model: {self._model}")

    def update_year(self, new_year):
        self.__year = new_year


class NumbersCompare:

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        self.__coef = 0.01

    def compare(self):
        if abs(self.num1 - self.num2) < self.__coef:
            return True
        else:
            return False

nc = NumbersCompare(1, 1.1)
print(nc.compare())

class Romb:

    def __init__(self):
        pass

r = Romb(side_a='asd')

r.side_a = 'asd'
print(r.side_a)


a = r.angle_a
b = r.angle_b
a + b == 180

r.angle_a + r.angle_b == 180