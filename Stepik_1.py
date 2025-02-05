# print("Hello, it's me", end='!\n')
# print("Hello, it's me!", end='')
# print(end='\n\n\n')
# #
# # my_name = ('Kate')
# # print('I am', my_name,'!', 'What is your name?')
# # your_name = input()
# # print('hi, your name is ', your_name)
# #
# # print('Как тебя зовут?')
# #
# # name = input()
# # print('Привет,', name)
# #
# # name = 'Timur'
# # print('Привет,', name)
# #
# # first = input()
# # second = input()
# #
# # print('I am', first, 'and', second)
#
# # name = input()
# # age = input()
# #
# # print('Мое имя –', name, 'и мне', age, 'лет!')
#
# # Тема урока: sep, end, PEP 8
# print('aa', 'bb', 'cc', sep='*')
# print('aa', 'bb', 'cc', sep='')
# minus = '-'
# print('aa', 'bb', 'cc', sep=minus)
#
# tire = ' — '
# print("A great man doesn't seek to lead", end='\n')
# print("A great man doesn't seek to lead", end=tire)
# print('second line')
#
# print('a', '\n', 'b', '\n', 'c', sep='*', end='#')
# print('a', 'b', 'c', sep='*', end='finish\n')
# print()
# arg1 = 'Hello'
# sep1 = '_-_'
# end2 = '+++\n'
#
# print(arg1, 'everyone', sep=sep1, end='! ')
# print('How', 'are', 'you', 'in', '2024?', sep=' ', end=end2)
#
# print('Python', end='\n\n\n')
# print('Python', end='\n\n\n')


# str1 = input()
# str2 = input()
# str3 = input()
# str4 = input()
#
# print(str2, str3, str4, sep=str1)

# #Множественное присваивание
# print("Print Your name")
# name_input = input()
# print('Print Your last name')
# surname_input = input()
#
# # name, surname = input(), input()
#
# name, surname = name_input, surname_input
# print('Имя:', name, 'Фамилия:', surname)

name1 = 'Timur'
name2 = 'Gvido'

print(name1, name2)

name1 = name2
name2 = name1
print(name1, name2)

length_side = input()
val = int(length_side) ** 3
print('Объем =', val)
square = 6 * (int(length_side) ** 2)
print('Площадь полной поверхности =', square)