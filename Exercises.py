# # вложенный цикл for
# colors = ['green', 'yellow', 'red']
# cars = ['bmw', 'audi']
# for color in colors:
#     for car in cars:
#         print(color, car)
#
#
# x = 3
# while x <= 8:
#     print(x)
#     x +=2
# else:
#     print(f'x is less than {x}')
#
#
# flowers = ['rose', 'tulip', 'lilac']
# for flower in flowers:
#     if flower == 'rose':
#         pass
#     else:
#         print(flower)
#
# x = 30
# y = 0
#
# if x > 27:
#     if y > 1:
#         print('x is greater than 27 and y is greater than 1')
#     else:
#         print('x is greater than 27 and y is not greater than 1')
# else:
#     print('x is not greater than 27')
#

x = 33
def count(x):
    if (x % 2 == 0):
        print(f'x is четное')
    else:
        print(f'x is нечетное')
count(x)
x = 55
if x > 13:
    print('x more than 13')
elif x > 51:
    print('x more than 51')
else:
    print('x less or 51')


sum_res = 0
numbers = list(range(1, 5))
for number in numbers:
    sum_res += number
print("Sum is", sum_res)

for i in range(3, 8):
    if i % 2 == 0:
        continue
    print(i)

numbers_first = range(1, 20)
numbers_sec = range(1, 20)

for num1 in numbers_first:
    for num2 in numbers_sec:
        print(num1*num2)


x = 0
while x < 6:
    y = 0
    while y <3:
        print(f'x: {x}, y: {y}')
        y +=1
    x += 1