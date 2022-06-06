first_list = input("Input the number whith " ", please").split()
for i in range(1,len(first_list), 2):
    first_list[i-1], first_list[i] = first_list[i],first_list[i-1]
print("New list", first_list)
