my_list = ['a', 'b', 'c', 'd']
#my_list_enum=enumerate(my_list)
#print(list(my_list_enum))
list_enum=""
for counter, value in enumerate(my_list):
    list_enum +=str(value) + " " +str(counter)+", "
print(list_enum)