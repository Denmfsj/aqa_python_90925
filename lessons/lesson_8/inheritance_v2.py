

class Phone:


    def __init__(self, brand, model):
        self.brand = brand
        self.model = model


    def send_sms(self, number):
        pass


class Smart(Phone):

    def __init__(self, brand, model, ram, size):
        super().__init__(brand=brand, model=model)
        self.ram = ram
        self.size = size

    def isntall_app(self, app_name):
        print(f'{app_name} as installed on you phone')



class IPhone(Smart):

    def __init__(self, model, ram, size):
        super().__init__(brand='Apple', model=model, ram=ram, size=size)
        # Smart.__init__(brand='Apple', model=model, ram=ram, size=size)

    def isntall_app(self, app_name):
        print(f'{app_name} as installed on you Iphone')


class IPhone15ProMax64GB(IPhone):

    def __init__(self):
        super().__init__(model='15ProMax', ram=8, size=64)
        # IPhone.__init__(model='15ProMax', ram=8, size=64)


class Samsung(Smart):

    def __init__(self, model, ram, size):
        super().__init__(brand='Samsung', model=model, ram=ram, size=size)
        # Phone.__init__(brand='Samsung', model=model, ram=ram, size=size)


iphone_15 = IPhone15ProMax64GB()

print(iphone_15.brand)
print(iphone_15.model)
print(iphone_15.ram)
print(iphone_15.size)
iphone_15.isntall_app('Angry birds')


# iphone_14 = IPhone(model='14', ram=8, size=128)
# print(iphone_14.brand)
# print(iphone_14.model)
# print(iphone_14.ram)
# print(iphone_14.size)
# iphone_14.isntall_app('Angry birds')

