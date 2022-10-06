name = 'Peter Pig'
city = 'London'
age = 16.5
ass = 'ass hole'

  # print('This is Любое имя. Любое имя lives in Москва. Любое имя is 16.5 years old')
  # print(f'This is {name}. {name} lives in {city}. {name} is {age} years old')
  # print('This is {0}. {0} lives in {1}. {0} is {2} years old'.format(name, city, age, ass))

line_1 = 'This is Любое имя. Любое имя lives in Москва. Любое имя is 16.5 years old'
line_2 = f'This is {name}. {name} lives in {city}. {name} is {age} years old'
line_3 = 'This is {0}. {0} lives in {1}. {0} is {2} years old'.format(name, city, age, ass)


from tkinter import *

root = Tk()
Label(text=line_1).pack()
Label(text=line_2).pack()
Label(text=line_3).pack()
root.mainloop()