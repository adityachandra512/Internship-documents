from tkinter import *
root=Tk()
root.geometry("250x200")

def resize():
    w=width.get()
    h=height.get()
    root.geometry(f"{w}x{h}")

root.title("window resize")
Label(text="window resizer",font="comicsansms 11 bold",pady=20).grid(column=2)

Label(text="width").grid(row=1,column=1)
Label(text="height").grid(row=2,column=1)
width=StringVar()
height=StringVar()

we=Entry(root,textvariable=width).grid(row=1,column=2)
he=Entry(root,textvariable=height).grid(row=2,column=2)
Button(text="apply",command=resize,pady=2).grid(column=2)
root.mainloop()