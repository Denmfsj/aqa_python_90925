import random
import string


class PasswordGenerator:

    def __init__(self):
        self.pwd = ''


    def add_numbers(self, number_of_numbers=4):
        self.pwd = self.pwd + ''.join(random.choices('0123456789', k=number_of_numbers))
        return self

    def add_special_char(self):
        self.pwd = self.pwd + random.choice("!@#$%^&*()_")
        return self

    def add_letter(self, number_of_letters=3):
        self.pwd = self.pwd + ''.join(random.choices(string.ascii_letters, k=number_of_letters))
        return self

instance_of_cls = PasswordGenerator()
# instance_of_cls.add_numbers()
# PasswordGenerator.add_numbers(instance_of_cls)


generated_pwd = PasswordGenerator().add_letter(6).add_numbers(3).add_special_char().pwd
generated_pwd_with_number = PasswordGenerator().add_letter(6).add_special_char().pwd

print(generated_pwd)
print(generated_pwd_with_number)

