# Tkinter GUI 
from tkinter import *

window = Tk()
window.title('My first programm')
window.geometry('300x300')
window.resizable(False,False)

'''btn = Button(window, text='Click Me!', font=('arail',16), bg='blue', fg='white')
btn.pack()'''
'''
text = Text(window, height=2)
text.pack()
entry = Entry(window)
entry.pack()

label = Label(window, text='Hello world')
label.pack(padx=50, pady=50)

btn_1 = Button(window, text='0', width=5)
btn_1.grid(row=0, column=0)

btn_2 = Button(window, text='1', width=5)
btn_2.grid(row=0, column=1)

btn_3 = Button(window, text='2', width=5)
btn_3.grid(row=0, column=2)'''

e = Entry(window)
e.pack()
e.insert(0,'')

def mybtn():
    hello = 'Hello ' + e.get()
    label = Label(window, text=hello, font=('arial',16))
    label.pack(padx=10, pady=10)

btn = Button(window, text='ok', command=mybtn, width=50)
btn.pack()


window.mainloop()
