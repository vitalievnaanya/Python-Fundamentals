n = input()
n_list = n.split(" ")
new_list = []

for i in range (len(n_list)):
    current_num = int(n_list[i])
    current_num = -current_num
    new_list.append(current_num)
print(new_list)
