from tkinter import *

root = Tk()
root.geometry("250x250")
root.title("first class")
root.config(bg="pink")

btn = Button(root, text="don't click me",bg="blue",fg="white",bd=5,command=root.destroy)
btn.pack(side ="bottom")


root.mainloop()