from tkinter import *
from tkinter.ttk import *


def clear_display():
    entry_display.delete(0, END)


root = Tk()

# style = Style()
# style.configure('W.TButton', width=3)

number = StringVar()
number.set(0)

entry_display = Entry(textvariable=number, justify=RIGHT)
entry_display.grid(column=0, row=0, columnspan=7, rowspan=1, sticky=NSEW)

# Button(text="MC", style="TButton").grid(column=1, row=1)
Button(text="MC").grid(column=1, row=1)
Button(text="MR").grid(column=2, row=1)
Button(text="MS").grid(column=3, row=1)
Button(text="M+").grid(column=4, row=1)
Button(text="M-").grid(column=5, row=1)

Button(text="<--").grid(column=1, row=2)
Button(text="CE").grid(column=2, row=2)
Button(text="C", command=clear_display).grid(column=3, row=2)
Button(text=chr(177)).grid(column=4, row=2)
Button(text=chr(8730)).grid(column=5, row=2)

Button(text="7").grid(column=1, row=3)
Button(text="8").grid(column=2, row=3)
Button(text="9").grid(column=3, row=3)
Button(text="/").grid(column=4, row=3)
Button(text="%").grid(column=5, row=3)

Button(text="4").grid(column=1, row=4)
Button(text="5").grid(column=2, row=4)
Button(text="6").grid(column=3, row=4)
Button(text="*").grid(column=4, row=4)
Button(text="1/x").grid(column=5, row=4)

Button(text="1").grid(column=1, row=5)
Button(text="2").grid(column=2, row=5)
Button(text="3").grid(column=3, row=5)
Button(text="-").grid(column=4, row=5)
Button(text="=").grid(column=5, row=5, rowspan=2, sticky=NS)

Button(text="0").grid(column=1, row=6, columnspan=2, sticky=EW)
Button(text=".").grid(column=3, row=6)
Button(text="+").grid(column=4, row=6)

root.mainloop()