from tkinter import *
root = Tk()
Canvas_width=800
Canvas_height= 600
root.geometry(f"{Canvas_width}x{Canvas_height}")
can_width=Canvas(root, width=Canvas_width,height=Canvas_height)
can_width.pack()
# can_width.create_line(0, 0, 800, 400, fill="red")
# can_width.create_line(0, 400, 800, 0,fill="red")
# can_width.create_rectangle(3,5,700,300)
can_width.create_text(200,200,text="python")
can_width.create_oval(344,233,244,355)
root.mainloop()