immutable_var = (4, 'good boy', True)
print(immutable_var)

immutable_var[1] = 3
print(immutable_var)
# immutable_var[1] = 3
#     ~~~~~~~~~~~~~^^^
# TypeError: 'tuple' object does not support item assignment

mutable_list = ['appple', 'coconat', 'banana']
mutable_list[0] = 44
mutable_list[1] = 'nice job'
print(mutable_list)







