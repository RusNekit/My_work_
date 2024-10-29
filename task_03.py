my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
new_list = []
a = len(my_list)
b = 0
while b < a:
    if my_list[b] > 0:
        print(my_list[b])
        b += 1
        continue
    elif my_list[b] == 0:
        b += 1
        continue
    else:
        break






