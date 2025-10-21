

class Car:
    _BRAND = 'Unknown'


class Nissan(Car):

    _BRAND = 'Nissan'

    def __init__(self, model, wheels, fuel):

        self.model = model
        self.wheels = wheels
        self.fuel = fuel


    def __repr__(self):
        return f'{self.model}, {self._BRAND}'

    def drive(self, distance):
        if self.fuel - distance >= 0:
            print(f'Driving, {distance}. Left {self.fuel}')
            self.fuel = self.fuel - distance

y60 = Nissan('y60', 4, 50)
y61 = Nissan('y61', 4, 50)


Nissan._BRAND = 'Misssan'
print(y60._BRAND, id(y60._BRAND))  # instance
print(Nissan._BRAND, id(Nissan._BRAND))  # class

print('-----------')
y60._BRAND = 'Toyota'  # self._BRAND
print('instance y60', y60._BRAND, id(y60._BRAND))  # instance  = 'Toyota'
print('class of y60', y60.__class__._BRAND, id(y60.__class__._BRAND))  # instance  = 'Misssan'
print(y61._BRAND, id(y60._BRAND))  # instance  = 'Misssan'
print(Nissan._BRAND, id(Nissan._BRAND))  # class


# 1) self  -> class -> Parents

class Supra(Nissan):

    def get_base_brand(self):
        return super(Nissan, self)._BRAND  # батько Nissan


# print(Supra('y60', 4, 50).get_base_brand())


# print(y60._BRAND, id(y60._BRAND))
# print(Nissan._BRAND, id(Nissan._BRAND))
#
# y61 = Nissan('y61', 4, 50)
#
# print(y61._BRAND)



    #
    #
    # @classmethod
    # def print_brand(cls):
    #     print(f"Godlike {cls._BRAND}")
    #
    #
    # @classmethod
    # def get_brand(cls):
    #     cls.print_brand()
    #     return cls._BRAND
    #
    # @staticmethod
    # def get_price(model):
    #     if model is not None and len(model) == 0:
    #         print('Say the model')
    #         return
    #     print(f'Come and see the price of {model}')
    #
    # @staticmethod
    # def make_noize():
    #     print('Rrrr')




# y60 = Nissan('y60', 4, 50)
# y60.get_price('ololo')
# Nissan.get_price('asdasdasd')
