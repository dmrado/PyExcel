from tkinter import *

root = Tk()
button = Button(root, text="Click me!", fg="red", bg="green")
button.pack()  # дает увидеть созданную кнопку
# root.mainloop()

from tkinter import *

root = Tk()
imagetest = PhotoImage(file="fullcolour.gif")
button_ok = Button(root, text="OK", fg="yellow", bg="green", underline=1, image=imagetest, compound="top")
button_ok.pack()
button_not_ok = Button(root, text="NOT OK", fg="yellow", bg="green", underline=1)
button_not_ok.pack()
root.mainloop()