from tkinter import *
def update():
    print("updating the gui")
    root.geometry(f"{width.get()}x{hight.get()}")
root=Tk()
root.geometry("344x233")
width=StringVar()
hight=StringVar()
Entry(root,textvariable=width).pack()
Entry(root,textvariable=hight).pack()
Button(root,text="apply",command=update).pack()
root.mainloop()