# empty_list = []
# names = ['Ann', 'Max', 'Lin', 'Kate']
#
# # СПИСКИ
# print(list('cat'))
# print(list(names))
# print(names[-1])
#
# birthday = '29/09/1986'
# print(birthday.split('/'))
#
# cats = ['Miy', 'May', 'Say']
# dogs = ['Nanny', 'Manny', 'Manny']
# all_animals = [cats, dogs]
# print(all_animals)
# print(all_animals[1][1])
# all_animals[1] = 'Larry'
# print(all_animals)
#
# # Объединение списков с помощью метода extend или оператора +
# cats.extend(dogs)
# # cats +=dogs / the same result as above
# print(cats)
#
# birds = ['Fly', 'Dry', 'Amy']
#
# # Ф-ия append() добавляет элементы в конец списка
# cats.append(dogs)
# print(cats)
#
# #  Ф-ия insert() добавляет элемент в нужное место - поиндексу
# cats.insert(5, birds)
# print(cats)
#
# #  Ф-ия del - удаляет элемент списка по индексу
# del cats[-1]
# print(cats)
#
# #  Ф-ия remove() удаляет элемент списка по значению
# cats.remove('Miy')
# print(cats)
#
# #  Ф-ия pop() позволяет получить заданный элемент и удалить его
# cats.pop(1)
# print(cats)
# print(cats.pop(1))
#
# #  Ф-ия index() выводит индекс элемента
# print(cats.index('Manny'))
#
# #  Ф-ия in - проверка на наличие элемента в списке
# print('Kally' in cats)
# print('May' in cats)
#
# #  Ф-ия count - считает кол-во включений
# print(cats.count('Manny'))
#
# #  Ф-ия join() - преобразуют список в строку !Противоположна split()
# ', '.join(birds)
# print(', '.join(birds))
#
# #  Ф-ия join() еще вариант использования
# separator = ' * '
# joined = separator.join(birds)
# print(joined)
#
# #  Ф-ия sort сортирует список в алфавитном порядке
# print(birds)
# sorted_birds = sorted(birds)
# print(sorted_birds)
#
# birds.sort()
# print(birds)
#
# numbers = [3, 78, 9, 45.3, 0.1]
# numbers.sort()
# print(numbers)
# print(len(birds))
#
# # #  Ф-ия копирования - copy(), присвоения - list()
# # a = [1, 2, 3]
# # b = a.copy()
# # print(b)
# #
# # c = list(a)
# # print(c)
# #
# # d = a[:]
# # print(d)
# # d[1] = 'two'
# # print(d)
#
# ## КОРТЕЖИ - неизменяемы!!!
# empty_tuple = ()
# one_marx = 'Groo'
# print(one_marx)
#
# marx_tuple = 'Groo', 'Choo', 'Miy'
# print(marx_tuple)
# a, b, c = marx_tuple # распаковка кортежа
# print(a)
# print(b)
#
# #  Ф-ия tuple() создает кортежи из других объектов
# marx_list = ['Anny', 'Kenny']
# print(tuple(marx_list))
#
# ## СЛОВАРИ - порядок эл-в не имеет значения, ключ - значение
# empty_dict = {}
#
# lot = [('a', 'b'), ('c', 'd')]
# print(dict(lot))
#
# my_dict = {
#     'name': 'Ann',
#     'age': '23',
#     'job': 'Manager',
# }
#
# my_dict['hobby'] = 'music'
# my_dict['age'] = '38'
# print(my_dict)
#
# #  Ф-ия  update() - объединение словарей
# new_dict = {
#     'lang': 'RUS',
#     'theme': 'Maths'
# }
#
# my_dict.update(new_dict)
# print(my_dict)
#
# del my_dict['lang']
# print(my_dict)
#
# # #  Ф-ия  clear()
# # my_dict.clear()
# # print(my_dict)
#
# print('lang' in my_dict) # проверка на наличие
#
# print(my_dict['age'])
# print(my_dict.get('them', 'it is not in'))
#
# #  Ф-ия  keys()
# print(my_dict.keys())
#
# # Использовать list() - чтобы преобразовать ключи в список, values() - значения, items() - пары ключ-значение
# print(list(my_dict.keys()))
# print(list(my_dict.values()))
# print(list(my_dict.items()))
#
# second_dict = my_dict.copy()
# print(my_dict.copy())
#
# # МНОЖЕСТВА - имеют только ключи
# empty_set = set()
# print(empty_set)
#
# even_numbers = {0, 2, 4, 6, 8}
# print(even_numbers)
#
# print(set('kal'))
# print(set(('kal', 'mas')))
#
# print(set({'apple': 'red', 'orange': 'orange'})) # выводит только ключи из словаря
#
# # Проверка на наличие значения с помощью in
# drinks = {
#     'martini': {'vodka', 'vermouth'},
#     'white russian': {'vodka', 'kahlua'},
#     'screwdriver': {'orange juice', 'vodka'}
# }
#
# for name, contents in drinks.items():
#     if 'vodka' in contents and not ('kahlua' in contents):
#         print(name)
#
# martin= drinks['martini']
# wruss = drinks['white russian']
#
# print(martin & wruss)
# print(martin.intersection(wruss))
#
# print(martin | wruss)
# print(martin.union(wruss))
#
# print(martin.difference(wruss))
#
# years_list = [1986, 1987, 1988, 1989, 1990]
# print(years_list[3])
# print(years_list[-1])
#
# things = ['moz', 'cind', 'salm']
# things[1] = 'Cind'
# print(things)
#
# things[0] = things[0].upper()
# print(things)
#
# things.pop(2)
# print(things)
#
# surprise = ['Groucho', 'Chico', 'harpo']
# surprise[2] = 'Harpo'
# print(surprise)

e2f = {
    'dog': 'chien',
    'cat':'chat',
    'walrus': 'morse',
}
print(e2f.get('walrus'))

f2e = {}
for english, french in e2f.items():
    f2e[french] = english
print(f2e)

dfr = {
    'one': 'one1',
    'two': 'two1',
    'three': 'three1',
}
dfr1 = {}
for dict, dict1 in dfr.items():
    dfr1[dict1] = dict
print(dfr1)

print(f2e.get('chien'))
print(e2f.keys())

dict_5 = {}
dict_4 = {}
dict_3 = {}
dict_2 = {}
list_1 = ['Henry', 'Grumpy', 'Lucy']
dict_1 = {
    'cats': list_1,
    'octopi': dict_2,
    'emus': dict_3,
}
life = {
    'animals': dict_1,
    'plants': dict_4,
    'others': dict_5,
}
print(life)

print(life.keys())
print(life['animals'].keys())
print(life['animals']['cats'])































