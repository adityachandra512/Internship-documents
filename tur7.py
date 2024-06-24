from tkinter import *
root = Tk()
def getvalues():
    print("It works!")
root.geometry("655x333")
#heading
Label(root,text="welcome to aditya travel",font="comicsansms 13 bold",pady=15).grid(row=0,column=1)
#text for our form
name=Label(root,text="name")
phone=Label(root,text="phone")
gender=Label(root,text="gender")
emengency=Label(root,text="emengency Contact")
paymentmode=Label(root,text="payment mode")

#pack for our form
name.grid(row=1,column=0)
phone.grid(row=2,column=0)
gender.grid(row=3,column=0)
emengency.grid(row=4,column=0)
paymentmode.grid(row=5,column=0)

#tkinter variable for storing entries
namevalue=StringVar()
Phonevalue=StringVar()
gendervalue=StringVar()
emengencyvalue=StringVar()
paymentmodevalue=StringVar()
foodservicevalue=IntVar()

#entries for our form
nameentry=Entry(root,textvariable=namevalue)
phoneentry=Entry(root,textvariable=Phonevalue)
genderentry=Entry(root,textvariable=gendervalue)
emergencyentry=Entry(root,textvariable=emengencyvalue)
paymentmodeentry=Entry(root,textvariable=paymentmodevalue)

#packing the entries
nameentry.grid(row=1,column=2)
phoneentry.grid(row=2,column=2)
genderentry.grid(row=3,column=2)
emergencyentry.grid(row=4,column=2)
paymentmodeentry.grid(row=5,column=2)

foodservice=Checkbutton(text="want to prebook your meals",variable=foodservicevalue)
foodservice.grid(row=6,column=2)

Button(text="submit to aditya travels",command=getvalues).grid(row=7,column=2)

root.mainloop()