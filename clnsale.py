from tkinter import *
import client as c
import sales as s
def clsl():
    root=Tk()
    root.geometry('400x400')
    l1=Button(root,text="Add Client",command=c.clnt)
    l1.pack()
    l2=Button(root,text="Sold Property",command=s.sale)
    l2.pack()
    root.mainloop()