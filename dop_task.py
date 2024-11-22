def calculate_withUsers_sum(data):
    numbers_sum = 0
    strings_length_sum = 0
    all_summ = numbers_sum + strings_length_sum

    # Проверка типа данных
    if isinstance(data, (int, float)):
        # Если данные - число, добавляем его к сумме
        numbers_sum += data
    elif isinstance(data, str):
        # Если данные - строка, добавляем её длину к сумме длин строк
        strings_length_sum += len(data)
    else:
        # Если данные не число и не строка, проверяем их тип
        if isinstance(data, list) or isinstance(data, tuple):
            # Если это список или кортеж, рекурсивно применяем функцию к каждому элементу
            for i in data:
                if i == int():
                    numbers_sum = calculate_withUsers_sum(i)
                else:
                    strings_length_sum = calculate_withUsers_sum(i)
                # if item == str():
                #     strings_length_sum = calculate_withUsers_sum(item)
        elif isinstance(data, dict):
            # Если это словарь, рекурсивно применяем функцию к каждому значению
            for value in data.values():
                if value == int():
                    numbers_sum = calculate_withUsers_sum(value)
                else:
                    strings_length_sum = calculate_withUsers_sum(value)
            for x in data.keys():
                if x == str():
                    numbers_sum = calculate_withUsers_sum(x)
                else:
                    strings_length_sum = calculate_withUsers_sum(x)
    return all_summ


data_withUsers = [(6, {'cube': 7, 'drum': 8})]
result = calculate_withUsers_sum(*data_withUsers)
print(result)

#  [
#
#   [1, 2, 3],
#
#   {'a': 4, 'b': 5},
#
#   (6, {'cube': 7, 'drum': 8}),
#
#   "Hello",
#
#   ((), [{(2, 'Urban', ('Urban2', 35))}])
#
# ]
