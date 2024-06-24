from tkinter import *
def harry(event):
    print(f"you click on the button at {event.x}, {event.y}")
def quit(event):
    root.destroy()

root=Tk()
root.title("event handling")
root.geometry("644x334")
widget = Button(root,text="click me pl")
widget.pack()
widget.bind('<Button-1>',harry)
widget.bind('<Double-1>',quit)

root.mainloop()