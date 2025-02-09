def echo(a):

    if a == 'Ho ho':
        return a + ' ' + a
    else:
        print('Try again')
print(echo('Ho ho'))

def commentary(color):
    if color == "red":
        return "It's tomato"
    elif color == "green":
        return ("It's green")
    else:
        return "I don't know this color"
comment = commentary("red")
print(comment)


def menu(wine, entree, dessert):
# def menu(wine, entree, dessert='pudding): аргумент по умолчанию
    return {'wine': wine, 'entree': entree, 'dessert': dessert}
# result = menu('red', 'chicken', 'cake') # Позиционные аргументы
result = menu(entree = 'beef', dessert = 'chocolate', wine = 'white') # Аргументы - ключевые слова
# result = menu('chardonnay', dessert = 'flan', entree = 'fish')
print(result)

def works(arg):
    result = []
    result.append(arg)
    return result
print(works('a'))
print(works('b'))

def buggy(arg, result=[]):
    result.append(arg)
    print(result)
buggy('h')