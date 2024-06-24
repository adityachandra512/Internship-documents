from tkinter import *

def add():
    global i
    lbx.insert(ACTIVE,f"{i}")
    i+=1

i=0
root=Tk()
root.geometry("455x233")
root.title("listbox tutorial")
lbx=Listbox(root)
lbx.pack()
lbx.insert(END,"first items of the list box")
Button(root,text="add item",command=add).pack()
root.mainloop()