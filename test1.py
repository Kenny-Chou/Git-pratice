list_a = [1, 2, 3, 4, 5]

filter_obj = filter(lambda x: x % 2 == 0, list_a) 

even_num = list(filter_obj) 

print(even_num)

genex_example2 = (n**2 for n in [1, 2, 3, 4, 5] if n >= 3)
for x in genex_example2:
    print(x)










