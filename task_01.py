calls =0
def count_calls():
    global calls
    sum(calls)
    print(calls)




def string_info(a):
    global calls
    calls += 1
    a = len(a), a.upper(), a.lower()
    print(a)


#def is_contains(s, d):


string_info('NikiTa')
string_info('cOpibara')