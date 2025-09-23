my_list = [20,2,15,66,88, 10-4, 8*7]

#print(my_list)

my_list.sort()  # міняємо my_list, сортування, стандартне, від меншого до більшого, by default = reverse=False
#print(my_list)

my_list.sort(reverse=True)  # міняємо my_list, сортування, стандартне, від більшого до меншого
#print(my_list)

my_list.sort(reverse=False)  # міняємо my_list, сортування, стандартне, від меншого до більшого
#print(my_list)


# ----------------
my_list = [20,2,15,66,88, 10-4, 8*7]

sorted_list = sorted(my_list)  #  НЕ міняємо my_list, сортування, стандартне, від меншого до більшого
print('sorted_list', sorted_list)
#print('my_list', my_list)

sorted_list = sorted(my_list, reverse=True)  # НЕ міняємо міняємо my_list, сортування, стандартне, від більшого до меншого
print('sorted_list', sorted_list)
print('my_list', my_list)




