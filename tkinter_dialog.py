# from tkinter import messagebox
#
# response = messagebox.askquestion('Message title', 'Message ask content')  #задает вопрос
# print(response)
# response = messagebox.askyesno('Message title', 'Message y/n content')
# print(response)
# response = messagebox.askyesnocancel('Message title', 'Message y/n/cancel content')
# print(response)
# response = messagebox.askokcancel('Message title', 'Message ok/cancel content')
# print(response)
# response = messagebox.askretrycancel('Message title', 'Message retry/cancel content')  #повтор и отмена
# print(response)

from tkinter import filedialog
from tkinter import *

root = Tk()
document_open = filedialog.askopenfilename()
print(document_open)
document_save = filedialog.asksaveasfilename()
print(document_save)
root.mainloop()