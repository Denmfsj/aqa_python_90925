

class CheckApiVsUi:


    def check_ui_and_api_fields(self, api_data, ui_data, description):
        """

        :param api_data: string for number from API endpoint. Can be None
        :param ui_data: string, can be None in this case is '-'
        :param description: name of checking field + area
        :return: None
        """

        if api_data is None:
            self.check_api_none(ui_data, description)


        if type(api_data) is int:
            self.check_api_int(api_data, ui_data, description)


        if type(api_data) is str:
            self.check_api_str(api_data, ui_data, description)


    def check_api_none(self,  ui_data, description):

        if ui_data != '-':
            print(f'{description}. Ui data has value {ui_data} but should have -')


    def check_api_int(self,  api_data, ui_data, description):

        if not ui_data.isdigit():
            print(f'{description}. Ui data has value {ui_data} but should have {api_data}')
            return

        if int(ui_data) != api_data:
            print(f'{description}. Ui data has value {ui_data} but should have {api_data}')


    def check_api_str(self,  api_data, ui_data, description):

        if ui_data != api_data:
            print(f'{description}. Ui data has value {ui_data} but should have {api_data}')


checker = CheckApiVsUi()

checker.check_ui_and_api_fields(api_data=None, ui_data='-', description='Correct check')
checker.check_ui_and_api_fields(api_data=None, ui_data='asdasd', description='wrong UI value witn empty row')
checker.check_ui_and_api_fields(api_data='', ui_data='-', description='wrong UI value with str')
checker.check_ui_and_api_fields(api_data=6, ui_data='6', description='Correct check')
checker.check_ui_and_api_fields(api_data=7, ui_data='7$', description='wrong UI value ith int')

# дeсь в тесті

# ui_data = ....  # дістав з  UI
# api_data = .... # api, db

# for field in ui_data:
#
#     checker.check_ui_and_api_fields(api_data=api_data.get(field), ui_data=ui_data.get(field),
#                                     description='Correct check')

