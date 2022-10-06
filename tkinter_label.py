from tkinter import *

name = "Dmitrii"
city = "Moscow"
gift = "Мороженное"

root = Tk()
root.title("Привет братва!")
root.geometry('800x600')
label_1 = Label(root, text='It is my first label, \n but is is not yours first \n LAB-e-e-e-l !!!!!')
label_1.pack()
label_2 = Label(root, text=f"Имя - {name} Город - {city} \n Подарок - {gift} ")
label_2.pack()
root.mainloop()

from tkinter import *
