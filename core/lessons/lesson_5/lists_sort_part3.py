
# [(id, score), (...)]
user_data = [
    (1, 90),
    (2, 57),
    (10, 94),
    (6, 77)
]


sorted_user_data = sorted(user_data)
print(sorted_user_data)

# хочу відсортувати по score

sorted_score_user_data = sorted(user_data, key=lambda x: x[1])
print(sorted_user_data)


#  - кожний елемент, tuple
# кожний елемент повинен повернути score

