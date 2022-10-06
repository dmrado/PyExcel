def privet():
    return 'Привет Python!'


#
#
# privet()
#
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]
# b = [2, 3]
# for i in range(2, 21, 2):
#     print(a[i])
#
# x = int(input('Введите Х '))
# y = int(input('Введите Y '))
#
#
# def diagram(x, y):
#     if y > 0:
#         if x > 0:
#             print(1)
#         else:
#             print(2)
#     else:
#         if x < 0:
#             print(3)
#         else:
#             print(4)
#     # else:
#     #     print('Never!')
#
#
# diagram(x, y)

print('Золотой фонд Python')
x, y, z = 1, 2, 3

print(x)
print(y)
print(z)

print(f'кортежное присваивание')
print(f'x до присваивания - {x}')
print(f'y до присваивания- {y}')
print(f'{x} {y} = {y} {x}')
def cort(x, y):
    x, y = y, x
    return y


print(f'функция cort() с аргументами x = {3} и y = {2} вернула {cort(3, 2)}')
x, y = y, x
print(f'x после - {x}')
print(f'y после - {y}')

print(f'кортежи')
t = 'a1', 'b2', 'c3', 'd4', 'e5', 'f6'
print(type(t))
print(t)
print('распаковка кортежа в строку t прямо в операторе print разделив его ^_^ и в конце сделать перевод каретки')
print(*t, sep=" ^_^ ", end="\n")
print(type(t))

print(f'распаковать отстатки кортежа t в переменную c')
a, b, *c = t
print(type(a))
print(a, b, c)
print(c)
print(type(c))

d = t[0]
print(d)

print('____________________________________')

print('пробежимся по СПИСКУ картежей')
t = [('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5), ('f', 6)]
# ниже i будет содержать каждый кортеж типа ('a', 1), где a - [0], а 1 - [1]
print('Можно cразу распаковать содержимое i двумя способами')

for i in t:
    print(i[0], i[1])

print('или')
print('далее переменные a и b автоматически присваивают значения a = i[0] b = i[1]')
for a, b in t:
    print(a, b)


print('____________________________________')

print('Словарь похож на объект в JS только доступ по-своему')
a = {'Mos': 1, 'Piter': 2, 'Ufa': 3}
print(f'старый словарь без Орла {a}')

o = 'Orel'
a[o] = 4
print(f'Новый словарь с Орлом {a}')

a['Piter'] = 22
print(f'Новый словарь с с измененным Питером {a}')

for key in a:
    print(key, a[key])

