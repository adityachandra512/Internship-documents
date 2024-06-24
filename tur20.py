from tkinter import *
root=Tk()
root.geometry("655x444")
root.title("title of my gui")
#root.wm_iconbitmap("")
root.configure(background="red")
width=root.winfo_screenwidth()
hight=root.winfo_screenheight()
print(f"{width}x{hight}")
Button(text="close",command=root.destroy).pack
root.mainloop()