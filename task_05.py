def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])
    if len(str_number) <= 1:
        return first
    else:
        first = int(str_number[0])
    return first * get_multiplied_digits(int(str_number[1:]))


result007 = get_multiplied_digits(233332032)
print(result007)