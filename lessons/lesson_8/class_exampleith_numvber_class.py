

class ApiData:

    def __init__(self, value):
        self.value = value


    def get_modified_for_ui_value(self):
        if self.value == None:
            return '-'
        return str(self.value)



api_v_1 = ApiData(None)
api_v_2 = ApiData(10)
api_v_3 = ApiData('50')
api_v_4 = ApiData('asd')

ui_1 = '-'
ui_2 = '10'
ui_3 = '50'
ui_4 = 'asd'

print(ui_1 == api_v_1.get_modified_for_ui_value(), f'{ui_1} == {api_v_1.value}')
print(ui_2 == api_v_2.get_modified_for_ui_value(), f'{ui_2} == {api_v_2.value}')
print(ui_3 == api_v_3.get_modified_for_ui_value(), f'{ui_3} == {api_v_3.value}')
print(ui_4 == api_v_4.get_modified_for_ui_value(), f'{ui_4} == {api_v_4.value}')