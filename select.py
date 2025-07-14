from tkinter import *
import realtors as r
import properties as p
import clnsale as c
import appointments as a
def property():
    root=Tk()
    root.geometry('400x400')
    l1=Button(root,text="Add Realtor",command=r.realt)
    l1.pack()
    l2=Button(root,text="Add Property",command=p.prop)
    l2.pack()
    l3=Button(root,text="Client",command=c.clsl)
    l3.pack()
    l4=Button(root,text="Book an appointment",command=a.apmnt)
    l4.pack()
    root.mainloop()