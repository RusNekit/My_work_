my_dict = {'city': 'Moscow',
            'adress': 'street_01',
            'home': 69,
            'room': 4}
print(my_dict)
print(my_dict['city'])
print(my_dict.get('garag'))   # медот .get выдает значение ключа, если ключа нет выдача будет None
my_dict.update({'Kictchen': 1,
                 'bathroom': 2})   # медот .update добавляет ключи в указанный словарь
a = my_dict.pop('room')           # метод .pop удаляет(вытаскиевает) ключ и значение из словаря и держит в себе.
print(a)
print(my_dict)
from struct import pack_into


# 3. Работа с множествами:

my_set = {2, 4, '4', 8, 9, '4', 9, True, False}
print(my_set)
my_set.add('55')
my_set.add('11')
print(my_set)
my_set.remove(1)
print(my_set)


# phone_book = {'Nik': 123456789, 'Kik': 1312312}    # словарь
# phone_book['Nik'] = 131231231
# phone_book['Giz'] = 5554
# phone_book.update({'Shasha': 77777,
#                    'Bil': 12312})
# print(phone_book)
# a = phone_book.pop('Kik')
# print(phone_book.keys())
# print(phone_book.values())

# set_ = {2, 4, 4, 8, 9, 9, True, False}                # множество
# list_ = [ 4, 8, 9, 9, True, False, 2, 4, 4, 8, 9, 9, True, False, 4, 4, 8, 9, 9, True, False]            # список
# #print((set(list_)))  # их списка делается упорядоченное множество
# list_ = set(list_)   # их списка делается упорядоченное множество
# print(list_)
# print(list_.remove(2))
