from tkinter import *
def getval():
    print(f"The value of username {uservalue.get()}")
    print(f"the value of the password {passvalue.get()}")
aditya_root=Tk()
aditya_root.geometry("655x333")
user=Label(aditya_root,text="Username")
password=Label(aditya_root,text="Password")
user.grid()
password.grid(row=1)

#variable classess in tkinter
#BooleanVar, DoubleVar,IntVar,StringVar
uservalue=StringVar()
passvalue=StringVar()
userentry=Entry(aditya_root,textvariable=uservalue)
passentry=Entry(aditya_root,textvariable=passvalue)
userentry.grid(row=0, column=1)
passentry.grid(row=1, column=1)

Button(text="Submit", command=getval).grid()
aditya_root.mainloop()