from tkinter import *  
from tkinter.ttk import Combobox
from tkinter.ttk import Checkbutton   

def clicked():  
    res = "Поздравляю с Днём Рождения, {}".format(txt.get())  
    lbl.configure(text=res)  

window = Tk()
window.geometry('400x250') 
window.title("Открытка для бабули")
lbl = Label(window, text="Привет!", font=("Algerian", 16))  
lbl.grid(column=0, row=0) 
txt = Entry(window,width=10)  
txt.grid(column=1, row=0)  
btn = Button(window, text="Нажми!", command=clicked)
btn.grid(column=2, row=0)
combo = Combobox(window)  
combo['values'] = ("Ты", "Лучшая", "Любимая", "Добрая", "Ласковая", "Классная")  
combo.current("0")   
combo.grid(column=0, row=3)
chk_state = BooleanVar()  
chk_state.set(True) 
chk = Checkbutton(window, text="Понравилось?", var=chk_state)  
chk.grid(column=0, row=5) 
window.mainloop()