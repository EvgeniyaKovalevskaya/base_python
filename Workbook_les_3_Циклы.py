# WHILE

# count = 1
# while count <= 5:
#     print(count)
#     count += 1
#
# while True:
#     word = input("String to capitalize [type q to quit]: ")
#     if word == 'q':
#         break
#     print(word.capitalize())
#
# while True:
#     value = input('Integer, please [q to quit]: ')
#     if value == 'q':
#         break
#     number = int(value)
#     if number % 2 == 0:
#         continue
#     print(number, 'squared is', number*number)

# FOR
rabbits = ['Koy', 'Foggy', 'Loo']
# current = 0
# while current < len(rabbits):
#     print(rabbits[current])
#     current += 1

for rabbit in rabbits:
    print(rabbit)

sentence = ['Hi', 'How are you']
for phrase in sentence:
    print(phrase)

# Итерирование по ключам
family = {'mom': 'Ann', 'dad': 'Joe', 'son': 'Alex'}
for role in family:
    print(role)

# Итерирование по значениям
for name in family.values():
    print(name)

# Чтобы вернуть как ключ, так и значение в виде кортежа
for pare in family.items():
    print(pare)

for key_word, value_word in family.items():
    print('Key word is', key_word, 'and the name is', value_word)

# cheeses = ['Camamber', 'Brie']
cheeses = []
for cheese in cheeses:
    print('This shop has some lovely', cheese)
    break
else:
    print('There is no cheese in it')

# zip() параллельное итерирование по нескольким последовательностям
eng = 'Monday', 'Tuesday', 'Wednesday'
fr = 'Lundi', 'Mardi', 'Mercredii'
print(list(zip(eng, fr)))
print(dict(zip(eng, fr)))

# range()
for x in range(0, 12, 3):
    print(x)

print(list(range(0, 12, 3)))

