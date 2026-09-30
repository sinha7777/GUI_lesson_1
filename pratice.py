from tkinter import *

root = Tk()
root.geometry("250x250")
root.title("4 buttons")
root.config(bg="white")

btn_1 = Button(root, text="click the other one",bg="blue",fg="white",command=root.destroy)
btn_1.pack(side="right")

btn_2 = Button(root,text="Why me??",bg="pink",fg="white",command= root.destroy)
btn_2.pack(side="bottom")

btn_3 = Button(root,text="Choose the other 3",bg="green",fg="white",command=root.destroy)
btn_3.pack(side="left")

btn_4 = Button(root,text="Not me please",bg="orange",fg="white",command=root.destroy)
btn_4.pack(side="top")

root.mainloop()