original_list = [1,2,3,5,4,-1]

original_str_list = 'Hell my name asd     asdhljaslhflkadfj'.split()  # список слів


def sort_srt_by_hash(row):

    hash_value = hash(row)
    return hash_value # поверне число

sorted_row_list = sorted(original_str_list, key=sort_srt_by_hash)
print(original_str_list)
print(sorted_row_list)

# new_list = sorted(original_list)
# print(original_list)
# print(new_list)
#
# original_list.sort(reverse=True)  # від max do min
# print('-----------------')
# print(original_list)
# print(new_list)