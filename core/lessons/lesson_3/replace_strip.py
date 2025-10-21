

row = "    Привіт, світ!    "

cut_all = row.strip(row)
print(cut_all)

print(row.rstrip())  # відкине пробіліи з правої стоорни
print(row.lstrip())  # відкине пробіліи з лівої стоорни
print(row.strip())  # відкине пробіліи з обох сторін



row = "Start: bla-bla"
cut_chars = 'Sar'

updated_row = row.strip(f'{cut_chars}b')  # ==> updated_row = row.strip('Sarb')
print(updated_row)
print(row.strip('Sar'))
# -----------------------------------------

row = ('Метод .replace() використовується для заміни '
       'входжень певної підстрічки іншою підстрічкою в рядку. Ось приклад використання:')



replaced_row = row.replace('о', '|')
print(replaced_row)

my_numbers = '1, two, 3, four'

updated_numbers = my_numbers.replace('two', '2').replace('four', '4').replace(' ', '')
print(updated_numbers)

my_numbers = '1, two, two, two, 3, four'

print(my_numbers.replace('two', '|||', 2))

replaced_word = 'two'

first_i = my_numbers.find(replaced_word)

my_numbers = my_numbers[:first_i] + '2' + my_numbers[first_i + len(replaced_word):]
print(my_numbers)

second_i = my_numbers.find(replaced_word)
third_i = my_numbers.find(replaced_word, second_i + 1)
my_numbers = my_numbers[:third_i] + '2' + my_numbers[third_i + len(replaced_word):]
print(my_numbers)