import tkinter as tk
import math
def click(value):
    entry.insert(tk.END,value)

def clear():
    entry.delete(0,tk.END)
def calculate():
    try:
        result=eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0,str(result))
    except :
        entry.delete(0, tk.END)
        entry.insert(0,"Error")
window= tk.Tk()
window.title("Artin calculator 1.2.1")
entry= tk.Entry(window,width=30,font=("Arial",20),borderwidth=1,relief="solid",justify="right")
entry.grid(row=0, column=0,columnspan=4
, padx=4,pady=8)
buttons=[("7",1,0),("8",1,1),("9",1,2)
          ,("/",1,3),("4",2,0),("5",2,1)
          ,("6",2,2),("*",2,3),("1",3,0)
          ,("2",3,1),("3",3,2),("-",3,3)
          ,("0",4,0),(".",4,1),("+",4,2),("=",4,3),("C",5,0),("**",5,3)]

for (text, row, col) in buttons:
    if text=="=":
        tk.Button(window,font=("Arial",15),text=text, width=8, height=3,command=calculate).grid(row=row,column=col)
    elif text=="C":
        tk.Button(window,font=("Arial",15),text=text,width=19,height=3,command=clear).grid(row=row, column=col, columnspan=8)
    else:
        tk.Button(window,font=("Arial",15), text=text,width=8,height=3, command=lambda t=text: click(t)).grid(row=row,column=col)

window.mainloop()