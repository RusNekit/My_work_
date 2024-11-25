def test_function(ls):
    def inner_function(ls):
        print('Я в области видимости функции', test_function)

    inner_function(ls)
    return ls


g = inner_function('Я в области видимости функции')
print(g)
