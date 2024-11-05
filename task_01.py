calls = 0

def count_calls():
    global calls
    calls += 1

def string_info(a):
    count_calls()
    a = len(a), a.upper(), a.lower()
    print(a)

def is_contains(striing, list_):
    count_calls()
    striing = striing.lower()
    for i in list_:
        if i.lower() == striing:
            return True

    return False

string_info('NikiTa')
string_info('cOpibara')

list_ = ['samMmI', 'saM']
striing = 'SaM'
result = is_contains(striing, list_)
print(result)
print(calls)
