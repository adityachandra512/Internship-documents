from tkinter import *
import tkinter.messagebox as tmsg
root=Tk()
root.geometry("455x233")
root.title("slider tutorial")
def getdoller():
    print(f"we have crediated {myslider1.get()} dollers to your bank account")
    tmsg.showinfo("amount credited",f"we have crediated {myslider1.get()} dollers to your bank account")
# myslider=Scale(root,from_=0,to=455)
# myslider.pack()
Label(root,text="how many dollar do you have ").pack()
myslider1=Scale(root,from_=0,to=100,orient=HORIZONTAL,tickinterval=50)
#myslider1.set(50)
myslider1.pack()
Button(root,text="get dollers",command=getdoller,pady=10).pack()
root.mainloop()