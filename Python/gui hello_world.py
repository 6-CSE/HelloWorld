#Gui to say hello world

from tkinter import *


root=Tk()
root.title("Hello world!")
root.geometry("600x400+100+100")
root.config(bg="black")

Label(root,text="Hello World !",fg="lightgreen",font="Arial 40 bold",bg="black").pack(pady=70)


root.mainloop()
