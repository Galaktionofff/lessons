s = 0
my_list = [42, 69, 0, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
while (my_list[s]) >= 0:
    if my_list[s] > 0:
        print(my_list[s])
        s = s + 1
    elif my_list[s] == 0:
        s = s + 1
        continue
    else:
        break
