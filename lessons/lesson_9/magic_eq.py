# в іншйи файл
class NumberWrapper:

    def __init__(self, value):
        self.value = value


    def __eq__(self, other):  #  a == b ==>  a.__eq__(b)
        if self.value is None:
            return '-' == str(other.value)
        elif other.value is None:
            return str(self.value) == '-'
        else:
            return str(self.value) == str(other.value)


api_value = NumberWrapper(33)  # api_value.value = 33
ui_value = NumberWrapper('33')  # ui_value.value = '33'
api_value_2 = NumberWrapper(None)  # api_value_2.value = None
ui_value_2 = NumberWrapper('-')
api_value_3 = NumberWrapper(0)
ui_value_3 = NumberWrapper('-')

api_value_4 = 'Buy'
ui_value_5 = 'Buy'


# test
# NumberWrapper
print(api_value == ui_value)  # api_value.__eq__(ui_value)
print(api_value_2 == ui_value_2)
print(ui_value_2 == api_value_2)
print(api_value_3 == ui_value_3)

# str
print(api_value_4 == ui_value_5)


