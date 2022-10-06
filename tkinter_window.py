from tkinter import *
root = Tk()
root.title('Окно-1')  # заголовок окна
root.geometry('350x200')
root.mainloop()  # команда не дает окну открыться, пока открыто предыдущее, должна быть в конце

from tkinter import *
root = Tk()
root.title('Окно-2')
root.geometry('750x200+1090-400')
root.mainloop()


from tkinter import *
root = Tk()
root.title('Окно-3')
root.geometry('500x800+500-500')
root.mainloop()