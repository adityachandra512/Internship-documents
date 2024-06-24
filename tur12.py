from tkinter import *
import tkinter.messagebox as tmsg
root=Tk()
root.geometry("733x566")
root.title("pycharm")
def myfunc():
    print("mai ek bahut he waste function hu ma kuch diserve nahi karta")

def help():
    print("i will help you")
    a=tmsg.showinfo("harry","harry will help you in this gui")
def rateus():
    print("rate us ")
    value=tmsg.askquestion("how is your experience","it is good")
    if value=="yes":
        msg="greate rating us appstore"
    else:
        msg="tell us what went wrong.we will try to resolve it "    
        tmsg.showinfo("show me experience",msg)

def divya():
    ans=tmsg.askretrycancel("divya sa dosti kar lo","sorry divya nahi bangi apki dost")
    if ans:
        print("retry kanna pa such nahi hoga")
    else:
        print("acha hu nahi kiya ")    
        
# mymenu=Menu(root)
# mymenu.add_command(label="file",command=myfunc)
# mymenu.add_command(label="file",command=quit)
# root.config(menu=mymenu)

mainmenu=Menu(root)
m1=Menu(mainmenu,tearoff=0)
m1.add_command(label="new project",command=myfunc)
m1.add_command(label="save",command=myfunc)
m1.add_command(label="save as",command=myfunc)
m1.add_command(label="print",command=myfunc)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="File",menu=m1)


m2=Menu(mainmenu,tearoff=0)
m2.add_command(label="cut",command=myfunc)
m2.add_command(label="copy",command=myfunc)
m2.add_separator()
m2.add_command(label="Paste",command=myfunc)
m2.add_command(label="Find",command=myfunc)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="Edit",menu=m2)

m3=Menu(mainmenu,tearoff=0)
m3.add_command(label="Help" ,command=help)
m3.add_command(label="Rate us " ,command=rateus)
m3.add_command(label="befriend divya " ,command=divya)
mainmenu.add_cascade(label="Help",menu=m3)
root.config(menu=mainmenu)
root.mainloop()