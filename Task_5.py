from random import randint
my_list = ["a", "b", "c", "d"]
size = len(my_list)
new_list = []
for i in range(size+10):
    j = randint(0,len(my_list)-1)
    if my_list[j] not in new_list:
       new_list.append(my_list[j])
print(new_list)
