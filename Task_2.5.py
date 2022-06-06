my_list = [7, 5, 3, 3, 2]
rating = int(input("Input the new position"))
i1 = len(my_list) #счётчик позиции элемента листа
flag = True
for i in range(len(my_list), 0, -1):
    if my_list[i-1] >= rating and flag:
        my_list.insert(i1, rating)
        flag = False
    i1 -= 1
if flag:
    my_list.insert(0, rating)
print(my_list)
