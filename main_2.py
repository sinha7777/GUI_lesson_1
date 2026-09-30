from tkinter import *

root = Tk()
root.geometry("450x300")
root.title("login screen")
root.config(bg="blue")

username_label = Label(root,text="Username:",font=("Arial",16,"bold"),bg="blue",fg="white")
username_label.place(x=50,y=50)

username_entry = Entry(root,width=30)
username_entry.place(x=170,y=55)

password_label = Label(root,text="password:",font=("Arial",16,"bold"),bg="blue",fg="white")
password_label.place(x=50,y=100)

password_entry = Entry(root,width=30,show="*")
password_entry.place(x=170,y=105)

btn = Button(root,bg="pink",fg="white",text="submit",command=root.destroy)
btn.place(x=225,y=275)




root.mainloop()
