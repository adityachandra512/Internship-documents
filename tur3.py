from tkinter import *
from PIL import Image,ImageTk
aditya_root=Tk()
aditya_root.geometry("500x500")
#photo=PhotoImage(file="flag.jpg")
image=Image.open("flag.jpg")
photo=ImageTk.PhotoImage(image)
adi_label=Label(image=photo)
adi_label.pack()
aditya_root.mainloop()