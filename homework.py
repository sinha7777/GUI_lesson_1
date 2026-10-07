from tkinter import *

root = Tk()
root.geometry("300x300")
root.title("traffic light")
root.config(bg="white")

btn_1 = Button(root, text="STOP",bg="red",fg="white",command=root.destroy)
btn_1.pack(side="right")

btn_2 = Button(root,text="WAIT",bg="yellow",fg="black",command= root.destroy)
btn_2.pack(side="bottom")

btn_3 = Button(root,text="GO",bg="green",fg="white",command=root.destroy)
btn_3.pack(side="left")

root.mainloop()