def print_params(a, b, c):
    print(a, b, c)


values_list = [3, 'super', True]
values_dict = {'a': values_list[0], 'b': values_list[1], 'c': values_list[2]}

values_list_02 = [117, 'Dsuper']
values_dict_02 = {'c': 44444}

print_params(**values_dict)
print_params(*values_list_02, **values_dict_02)


# values_list_03 = ['super', True]
# print_params(*values_list_2, 42)

