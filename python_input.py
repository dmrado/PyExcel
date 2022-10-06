from tkinter import messagebox

from tkinter import *

name = input('What is your name?')
age = input(f'How old are you, {name}?')
city = input(f'Where do you live, {name}?')

print(f'Your name is {name}. You are {age} yo. You live in {city} ')
print(f'nice to meet you {name}, would you like to play?')
response = messagebox.askyesno('Message title', 'Message y/n content')
if response:
    print(f'Wow {name}! I`m very glad to play with you! ')
else:
    print(f'{name} I`m crying! I want to play with you on a chess')

from tkinter import messagebox
from tkinter import *

response2 = messagebox.askyesno('Message title', 'Message y/n content')
if response2:
    print(f'Wow {name}! Thank you let`s play ')
else:
    print(f'{name} I`m crying! I want to play with you on a chess')