# Списки
names = []
# append "method"
names.append(2)
names.append("Alex")
names.append("Anna")
my_name = "Elena"
names.append(my_name)
#
# # Получить элемент из списка (с удалением его из списка)
# last_name = names.pop()
# print(last_name)
# print(names)
#
#
# # подсчет кол-ва элементов в списке
# print(names.count("234fj"))
#
# names.index("Alex")
# print(names)
# ind = names.index("Alex")
# print(ind)
#
# # Добавление элемента в произвольное место списка
# names.insert(0, "Masha")
# print(names)
#
# # Удаление элемента по его значению из списка
# names.remove("Masha")
# print(names)
#
# # Подсчет элементов в списке
# print(len(names))
#
# # Получение элементов списка (!). Указать индекс элемента.
# print(names[0])
# print(names[-1])
#
# # Срезы - получение нескольких элементов
# print(names[1:])
#
# names.extend(["Dima", "Anna", "Olga"])
# print(names[5:1:-1])
#
# # Как вернуть список с элементами в обратном порядке
# print(names[::-1])
#
# # for
# for i in names:
#     print(i)
#
# # range(6) = (0, 1, 2, 3, 4, 5)
# # range(1, 5) = (1, 2, 3, 4)
# a = 5
# a +=1
# print(a)
#
# for i in range(len(names)):
#     print(f"{i+1}, {names[i]}")
#
# a = 10
# while a > 0:
#     print("HellO")
#     a -=1

# while True:
#     print("Choose an action")
#     print("1. Add a book")
#     print("2. Del a book")
#     print("Put 0 to exit")
#
#     action = input(">>>")
#     if action == "1":
#         print("Book is added")
#     elif action == "2":
#         print("Book is deleted")
#     elif action == "0":
#         print("Bye")
#         break
#     else:
#         print("Try again")

# print(names)
# names.append("Nastya")
# print(names)
#
# for i in range (1, 10):
#     print(i)
#
#
# a = 1
# while a <=9:
#     print(a)
#     a+=1
# # Кортеж  tuple   используется для хранения констант
# numbers = (1, 2, 3, 4)
# status = (
# ("in_progress"),
# ("success")
# )
#
# print("Hello")
# print(len("Dima"))
#
# # Словари
# person = {}
info = {"name": "Dima",  "age": 16}
#
# # получение элемента словаря (значения по ключу)
# name = info["name"]
# print(info["name"])
#
# # добавление элемента в словарь
# info["phone"] = "89213456776"
# info["name"] = "Sergey"
# print(info)
#
#
# # Размер словаря равен кол-ву элементов (пар, ключей)
# print(len(info))
# info["lang"] = ["russian", "eng"]
#
info["edu"] = {"high": "MGU", "medium": "ITMO"}
# print(info)
#
#
# cars = {("bmw", "audi"): "germany"}
#
# age = info.pop("age")
# print(age)
# # print(info.get("age", "error").get("high2", {})
#
# print(info)
#
# info_copy = info
# print(info_copy)
#
# print(id(info))
# print(id(info_copy))
# info["xxx"] ="yyy"
# print(info_copy)
#
# users = []
# for i in range(3):
#     name = input("Enter the name")
#     phone = input("Enter the phone")
#     info_person = {"name": name, "phone": phone}
#
#     users.append(info_person)
#
# print(users)

#
# print(list(info.keys()))
# print(list(info.values()))
# print(list(info.items()))
# info.update({"name": "sasha"})
#
# for i in info.keys():
#     print(f"{i} - {info[i]}")
#
for key , value in info.items():
    print(f"{key} --- {value}")
