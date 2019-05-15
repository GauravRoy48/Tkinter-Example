from tkinter import *

window = Tk()

def convert_kg():
    grams = float(e2_value.get())*1000
    pounds = float(e2_value.get())*2.20462
    ounces = float(e2_value.get())*35.274
    
    t1.delete("1.0", END)
    t2.delete("1.0", END)
    t3.delete("1.0", END)
    t1.insert(END, str(grams))
    t2.insert(END, str(pounds))
    t3.insert(END, str(ounces))

b1 = Button(window, text='Convert', command=convert_kg)
b1.grid(row=0, column=2, rowspan=1)

e1=Label(window,text="Kg")
e1.grid(row=0,column=0)

e2_value = StringVar()
e2 = Entry(window, textvariable=e2_value)
e2.grid(row=0, column=1)

e3=Label(window,text="Grams")
e3.grid(row=1,column=0)
t1 = Text(window, height=1, width=20)
t1.grid(row=2, column=0)

e4=Label(window,text="Pounds")
e4.grid(row=1,column=1)
t2 = Text(window, height=1, width=20)
t2.grid(row=2, column=1)

e5=Label(window,text="Ounces")
e5.grid(row=1,column=2)
t3 = Text(window, height=1, width=20)
t3.grid(row=2, column=2)

window.mainloop()