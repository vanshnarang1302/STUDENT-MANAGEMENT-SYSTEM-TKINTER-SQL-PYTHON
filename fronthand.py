import tkinter as tk
from tkinter import Button

import database
from database import *
mainWindow=tk.Tk()
mainWindow.title("add data")

mainheadinglabel=tk.Label(mainWindow,text='STUDENT MAGANGEMENT SYSTEM',padx=(30),pady=(30), fg='red')
mainheadinglabel.grid(row=0 , column=2)

headinglabel1=tk.Label(mainWindow,text='name',padx=(10),pady=(10))
headinglabel1.grid(row=1 , column=0)

name_field=tk.Entry(mainWindow)
name_field.grid(row=1 , column=3,padx=(10),pady=(10))



headinglabel2=tk.Label(mainWindow,text='college name',padx=(10),pady=(10))
headinglabel2.grid(row=2 , column=0)

college_field=tk.Entry(mainWindow )
college_field.grid(row=2 , column=3,padx=(10),pady=(10))

headinglabel3=tk.Label(mainWindow,text='address',padx=(10),pady=(10))
headinglabel3.grid(row=3 , column=0)

address_field=tk.Entry(mainWindow)
address_field.grid(row=3 , column=3,padx=(10),pady=(10))

headinglabel4=tk.Label(mainWindow,text='phone',padx=(10),pady=(10))
headinglabel4.grid(row=4 , column=0)

phone_field=tk.Entry(mainWindow)
phone_field.grid(row=4 , column=3,padx=(10),pady=(10))
def get():
    name1=name_field.get()
    college1=college_field.get()
    address1=address_field.get()
    phone1=phone_field.get()
    insert(name1,college1,address1,phone1)
    name_field.delete(0,tk.END)
    college_field.delete(0,tk.END)
    address_field.delete(0,tk.END)
    phone_field.delete(0,tk.END)




insert1=tk.Button(mainWindow,text='insert',command =lambda : get())
insert1.grid(row=5 , column=0)

show1=tk.Button(mainWindow,text='show',command =lambda : show())
show1.grid(row=5,column=3)

mainWindow.mainloop()








