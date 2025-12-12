x = """Tom gave up the brush with reluctance in his .... face but alacrity
\b[a-zA-Z]{1,3}\b

\([\d]{3}\)\s[\d]{2}-[\d]{2}-[\d]{3}

(093) 55-66-777

in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little atom while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, tom kom om had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played (093) 55-66-777"""

# \b(price)\s - початок зі слова price, а потім пробіл
# ([a-zA-Z]+\s){0,4}  - слово + пробіл, зустрічаеться від 0 до 4х разів
# [\d]+\s - мінімум 1 цифра + в кінці пробіл
#
# (dollars\s)? - слово dollars + пробіл
#
# ([Uu][Ss][Dd]) - usd велика чи мала будь яка літера



# \b(price)\s([a-zA-Z]+\s){0,4}[\d]+\s(dollars\s)?([Uu][Ss][Dd])
#
# price 250 USD
# price of the company is 22 usd
# price is 56 dollars Usd
# price ololo asd 56 dollars Usd


import re

row = """
price 250 USD
price of the company is 22 usd
price is 56 dollars Usd
price ololo asd 56 dollars Usd
company has 22 usd
price is 67 eur
"""

pattern = r'\b(price)\s([a-zA-Z]+\s){0,4}[\d]+\s(dollars\s)?([Uu][Ss][Dd])'

result = re.findall(pattern, row)
print('Do we find a row', bool(result))

for m in re.finditer(pattern, row):
    print(m.group(0))  # 0 группа - повни збіг

# print(result)