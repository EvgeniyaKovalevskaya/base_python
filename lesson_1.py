# Типы данных
# int
a = 5
b = 6

NAME = "Anna" #const

print(a)
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a**b)
print(a%2)

# comment

print(f"Hello. a= {a}")
print(f"Hello. a+b = {a+b}")

""" 
comment for a function
"""

c=5.7
d=7.0

print(type(a))
print(type(c))

# boolean
print(7<10)

# string
age = "24"
print(int(age)+1)
last_name = ("Ivanov"
            "Smirnov")
text = """
dododo
dodood
"""
print(text)

city = "Moscow\ncity"
print(city)

# список используется для хранения данных в одной переменной
numbers = [] # список создан через литерал
new_numbers = [1, 2, 3] # 0 1 2 3 - индексы элементов
elements = [1, "e", True, [2, 3]]
print(elements)

cars = list() # создание списков с помощью list

# кортеж - неизменяемый список
colors = tuple() # не используем этот способ
new_colors = ("red", "blue")

# словарь - в нем индексов нет - СТРУКТУРА ДАННЫХ
car = {}
my_car = dict()

# хранит данные в формате ключ: значение,
# ! в словаре не может быть двух одинаковых ключей
# ключом словаря может быть только неизменяемый тип данных (строка, число, кортеж)
info = {"name": "Misha",
        "age":26,
        "city": "Moscow",
        ("1", 2, 3): 24}
print(info)

# множества - перечисление через запятую - СТРУКТУРА ДАННЫХ
set_of_names = {"Masha", "Sasha", "Dima", "Masha"}
print(type(set_of_names))
print(set_of_names)


cars = ["bmw", "audi", "bmw"]

# list -> set
print(list(set(cars)))

txt = "helllo"
print(set(txt))

# Управляющие конструкции
# if - else

age = 12
if (age < 11 and age !=0):
    print("error")
elif age == 0:
    print("age == 0")
elif age == 12:
    print("age == 12")
else:
    print("ok")
print("Next block") #выполнится вне зависимости от условий

in_name = input("Insert your name: ")
in_age = input("Insert your age: ")

print(f"Your name is {in_name}")
print(f"Your age is {in_age}")

print(12 == int(in_age))








