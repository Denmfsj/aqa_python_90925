users = [
    {'id': 1, 'name': 'Den', 'age': 20, 'job': [{'id': 1, 'title': 'QA'}]},
    {'id': 2, 'name': 'Alex', 'age': 30},
    {'id': 3, 'name': 'Igor', 'age': 40, 'job': None},
    {'id': 4, 'name': 'Ivan', 'age': 50, 'job': [{'id': 2, 'title': 'CEO'}]},
    {'id': 5, 'name': 'Mor', 'age': 60, 'job': [{'id': 1, 'title': 'QA'}]},
    {'id': 6, 'name': 'Viktor', 'age': 70, 'job': [{'id': 3, 'title': 'Retired'}]},
    {'id': 7, 'name': 'Maria', 'age': 20, 'job': [{'id': 1, 'title': 'QA'}]},
    {'id': 8, 'name': 'Anna', 'age': 20, 'job': []},
    {'id': 9, 'name': 'Inna', 'job': [{'id': 1, 'title': 'QA'}]},
]

# вік від 0 до  60 - ok, інакше - warning
# всі повинні мати job, якщо нема то  error
# друкувати user_id, status

titles = set()

for user in users:
    status = None

    user_age = user.get('age', 999)
    user_job = user.get('job')

    if user_age < 60:
        status = 'ok'
    else:
        status = 'warning'

    if not user_job:  # тут значення по замовчуванню = None
        status = 'error'

    else:
         #  user_job = [{'id': 1, 'title': 'QA'}]
         # j = {'id': 1, 'title': 'QA'}
        for j in user_job:  # по кожному елементу(словник) не порожнього списка
            titles.add(j.get('title'))



    print(user.get('id'), status)

print('titles', titles)