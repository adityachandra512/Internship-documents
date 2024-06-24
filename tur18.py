from tkinter import *
def upload():
    status.set("Busy..")
    sbar.update()
    import time
    time.sleep(2)
    status.set("ready now")

root=Tk()
root.geometry("455x233")
root.title("statusbar tutorial")
status=StringVar()
sbar=Label(root,textvariable=status,relief=SUNKEN,anchor="w")
sbar.pack(side=BOTTOM,fill=X)
Button(root,text="Upload",command=upload).pack()
root.mainloop()