from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename,asksaveasfile
import os
def newFile():
    global file
    root.title("Untitled-Noteworld")
    file=None
    TextArea.delete(1.0,END)
def openfile():
    global file
    file =askopenfilename(defaultextension=".txt",filetypes=[("all files","*.*"),("Text Documents","*.txt")])
    if file=="":
        file=None
    else:
        root.title(os.path.basename(file)+"-Noteworld")
        TextArea.delete(1.0,END)
        f=open(file,"r")
        TextArea.insert(1.0,f.read())
        f.close()
def saveFile():
    global file
    if file== None:
        file=asksaveasfile(initialfile="Untitled.txt",defaultextension=".txt",filetypes=[("all files","*.*"),("Text Documents","*.txt")])
        
        if file =="":
            file=None
        else:
            f=open(file,"w")
            f.write(TextArea.get(1.0,END))
            f.close()
            root.title(os.path.basename(file)+"-Noteworld")
def quitApp():
    root.destroy()
def cut():
    TextArea.event_generate(("<<Cut>>"))
def copy():
    TextArea.event_generate(("<<Copy>>"))
def paste():
    TextArea.event_generate(("<<Paste>>"))
def about():
    showinfo("Notepad","Noteworld is developed by aditya chandra")
if __name__ == '__main__':
    root=Tk()
    root.title("untitled - Noteworld")
    root.wm_iconbitmap("notepad.ico")
    root.geometry("644x788")

    TextArea=Text(root,font="lucida 13")
    file=None
    TextArea.pack(expand=True,fill=BOTH)
    #let create the menu bar
    MenuBar= Menu(root)
    FileMenu =Menu(MenuBar,tearoff=0)
    FileMenu.add_command(label="New",command=newFile)
    FileMenu.add_command(label="open",command=openfile)
    FileMenu.add_command(label="Save",command=saveFile)
    FileMenu.add_separator()
    FileMenu.add_command(label="Exit",command=quitApp)
    MenuBar.add_cascade(label="File",menu=FileMenu)


    EditMenu=Menu(MenuBar,tearoff=0)
    EditMenu.add_command(label="Cut",command=cut)
    EditMenu.add_command(label="copy",command=copy)
    EditMenu.add_command(label="paste",command=paste)
    MenuBar.add_cascade(label="Edit",menu=EditMenu)


    helpmenu=Menu(MenuBar,tearoff=0)
    helpmenu.add_command(label="about notepad",command=about)
    MenuBar.add_cascade(label="Help",menu=helpmenu)

    root.config(menu=MenuBar)

    scroll=Scrollbar(TextArea)
    scroll.pack(side=RIGHT,fill=Y)
    scroll.config(command=TextArea.yview)
    TextArea.config(yscrollcommand=scroll.set)
    root.mainloop()