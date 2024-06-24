from tkinter import *
root =Tk()
root.geometry("300x300")
root.title("My GUI With Harry")
#IMPORTANT LABLE OPTIONS
# text = adds the text
# bd = background
# fg = forground
# font = ("comidsansms",19,"bold")
# font "comidsansms",19,"bold"
# padx = x padding
# pady = y padding
# relif = border styling -sunken, raised, groove, ridge

title_lable = Label(text="hello world",bg="red",fg="white",padx=113,pady=44,font=("comicsansms",9,"bold"),borderwidth=3,relief=SUNKEN )
#IMPORTANT PACK OPTIONS
#ANCHOR=NW
#side=top,bottom,left,right
# fill
# padx
# pady
title_lable.pack(side=BOTTOM,anchor="nw",fill=X)
root.mainloop()