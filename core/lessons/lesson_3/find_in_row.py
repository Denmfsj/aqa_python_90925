description = 'Метод .find() використовується для пошуку підстрічки в рядку '


print('find' in description)  # True

company_name = 'apple'

description_in_lower = description.lower()

# перевірка чи почається опис зі слова apple
if not description_in_lower.startswith(company_name):
    print(f'Alarm, Опис товару не починаеться за слова {company_name}')

if company_name not in description_in_lower:
    print(f'Alarm, нема імені {company_name} в описі товару')


search_phase = "для"

index_of_start_of_search_phrase = description.find(search_phase)  # поверне число 31
# print(search_phase, "починаеться з", index_of_start_of_search_phrase, "index" )

index_of_end_of_search_phrase = index_of_start_of_search_phrase + len(search_phase)  # 31 + 3
# index_of_end_of_search_phrase = index_of_start_of_search_phrase + 3  # 31 + 3
# print(description[index_of_start_of_search_phrase: index_of_end_of_search_phrase])  # [31: 34]

description = 'Метод .find() використовується для пошуку підстрічки в рядку '
print('о count is ', description.count('о'))

print(description.find('о', 10, 16))  # -1
print(description[:18])