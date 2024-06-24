from tkinter import *
import tkinter.messagebox as tsmg
root=Tk()
root.geometry("455x233")
root.title("radio button tutorial")
def order():
    tsmg.showinfo("order recieved",f"we have recieve the order of {var.get()} .you meal will be ready soon!!")
#var=IntVar()
var=StringVar()
var.set("radio")
#var.set(1)
Label(root,text="what would you like to have sir",padx=14,justify=LEFT,font="Monterrat 19 bold").pack()
radio=Radiobutton(root,text="Dosa",padx=14,variable=var,value="dosa").pack(anchor="w")
radio=Radiobutton(root,text="uttapam",padx=14,variable=var,value="uttapam").pack(anchor="w")
radio=Radiobutton(root,text="samber vada",padx=14,variable=var,value="samber vada").pack(anchor="w")
radio=Radiobutton(root,text="idli chutney",padx=14,variable=var,value="idli chutney").pack(anchor="w")
Button(text="Order Now",command=order).pack()
root.mainloop()