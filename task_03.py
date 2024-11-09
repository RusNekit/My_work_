def print_params(a=1, b='строка', c=True):
    print(a, b, c)


values_list = [3, 'super', True]
values_dict = {'a': values_list[0], 'b': values_list[1], 'c': values_list[2]}

print_params(**values_dict)


values_list_2 = ['super', True]
print_params(*values_list_2, 42)

# Важно!
#
# Не передавайте списки задавая по умолчанию пустой список или другой изменяемый тип данных!
#
# В таком случае, если этот список будет изменён внутри функции, то на следующий вызов функции он останется в том же состоянии.
#
# def a(my_list = [])) – это приводит к ошибкам!
#
#
#
# Можно передавать вот так(список создаётся локально, мы не влияем на его изменение вне функции)
#
# def append_to_list(item, list_my=None):
#
#   if list_my is None:
#
#    list_my = []
#
#   list_my.append(item)
#
# print(list_my)