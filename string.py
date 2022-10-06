print("Варинаты переноса строк:")
print("""Children peace
Peace!!!
Pee-Peace!!!
""")
print("Hi\nHi\nHi")
print('Отступ в одну табуляцию.')
print('Отступ\tв одну табуляцию')

print('"Текст в кавычках"')

print("Буква в тексе в кавычках \"в\" кавычках")

text1 = 'Привет'
text2 = 'Мир'
print(text1 + ' ' + text2 + "!")

print(text1*5)

print(text1[0])

print(text1[0:3])
print(text1[-1])

print(text1.upper())
print(text1.lower())
text3 = 'привет'
print('capitalize: ' + text3.capitalize())
text4 = 'split зазбивает строку на объекты внутри списка, в качестве аргумента передаем разграничитель, по которому он определяет начало и окончание элемента списка'
print(text4)
print(text4.split(" "))

text5 = 'Быр-быр-быр'
print(text5.split("-"))

text6 = ["Метод", "join", "метод", "обратный", "split", "соединяет", "элементы", "списка", "в", "строку" ]
print(",".join(text6))
spisok = ["a", "b", "c"]
print(" ".join(spisok))

text7 = "      удаление пробелов строке начиная с нулевого до первого символа в строке "
print(text7.strip())

text8 = "      метод lstrip удаляет пробелов строке начиная с нулевого до первого символа в строке - слева"
print(text8.lstrip())

text9 = "метод rstrip удаляет пробелы в строке справа "
print(text8.rstrip())

text10 = "ololololo!"
print(text10.replace("o", "a"))

import privet
print((privet.privet()).replace("i", "y"))