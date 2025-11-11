import math
import logging

# from os import path
import os
from numerize import numerize

# from core.lessons import greetings, sep_short, sep_polimorf, LESSONS_NUMBER, custom_separator
from core.lessons import *
from core.lessons import LESSONS_NUMBER


# from core.lessons.lesson_7 import funct_base

# funct_base.greetings('Den')
# funct_base.custom_separator()

greetings("Den")
custom_separator()
sep_short()
sep_polimorf()

print(LESSONS_NUMBER)


x = os.path.join("asd", "foiledr_name")

my_list = [1, 2, 3]
print(dir(my_list))
