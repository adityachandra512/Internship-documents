from tkinter import *
aditya_root=Tk()
aditya_root.geometry("655x333")
def hello():
    print("hello world")
f1=Frame(aditya_root,borderwidth=6,bg="blue",relief=SUNKEN)
f1.pack(side=LEFT,anchor="nw")
b1=Button(f1,fg="red",text="Print Now",command=hello)
b1.pack(side=LEFT,padx=20)

b2=Button(f1,fg="red",text="Print Now")
b2.pack(side=LEFT,padx=20)


b3=Button(f1,fg="red",text="Print Now")
b3.pack(side=LEFT,padx=20)

b4=Button(f1,fg="red",text="Print Now")
b4.pack(side=LEFT,padx=20)
aditya_root.mainloop()