empty_list = []
names = ['Ann', 'Max', 'Lin', 'Kate']

# Function list
print(list('cat'))
print(list(names))
print(names[-1])

birthday = '29/09/1986'
print(birthday.split('/'))

cats = ['Miy', 'May', 'Say']
dogs = ['Nanny', 'Manny', 'Manny']
all_animals = [cats, dogs]
print(all_animals)
print(all_animals[1][1])
all_animals[1] = 'Larry'
print(all_animals)

# Объединение списков с помощью метода extend или оператора +
cats.extend(dogs)
# cats +=dogs / the same result as above
print(cats)

birds = ['Fly', 'Dry', 'Amy']

# Ф-ия append() добавляет элементы в конец списка
cats.append(dogs)
print(cats)

#  Ф-ия insert() добавляет элемент в нужное место - поиндексу
cats.insert(5, birds)
print(cats)

#  Ф-ия del - удаляет элемент списка по индексу
del cats[-1]
print(cats)

#  Ф-ия remove() удаляет элемент списка по значению
cats.remove('Miy')
print(cats)

#  Ф-ия pop() позволяет получить заданный элемент и удалить его
cats.pop(1)
print(cats)
print(cats.pop(1))

#  Ф-ия index() выводит индекс элемента
print(cats.index('Manny'))

#  Ф-ия in - проверка на наличие элемента в списке
print('Kally' in cats)
print('May' in cats)

#  Ф-ия count - считает кол-во включений
print(cats.count('Manny'))

#  Ф-ия join() - преобразуют список в строку !Противоположна split()
', '.join(birds)
print(', '.join(birds))

#  Ф-ия join() еще вариант использования
separator = ' * '
joined = separator.join(birds)
print(joined)

#  Ф-ия sort сортирует список в алфавитном порядке
print(birds)
sorted_birds = sorted(birds)
print(sorted_birds)

birds.sort()
print(birds)

numbers = [3, 78, 9, 45.3, 0.1]
numbers.sort()
print(numbers)
print(len(birds))


