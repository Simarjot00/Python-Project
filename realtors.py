from tkinter import *
from dbconnect import *
from tkinter.messagebox import showinfo
def realt():
    def getinfo():
        y=int(e1.get())
        m=e2.get()
        n=int(e3.get())
        p=int(e4.get())
        q=e5.get()
        query=f"insert into realtors(realtor_id,name,phone,licenseno,email) values('{y}','{m}','{n}',{p},{q})"
        alterations(query)
        showinfo(title='Insertion',message='Inserted Success')
        e1.delete(0,END)
        e2.delete(0,END)
        e3.delete(0,END)
        e4.delete(0,END)
        e5.delete(0,END)
    root=Tk()
    root.title("Realtor details")
    root.geometry("300x300")


    frame1=Frame(root,padx=5,pady=5)
    frame1.grid(row=1,column=1)
    Label(root,text="REALTOR DETAILS",padx=5).grid(row=0,columnspan=5,pady=7)
    l1=Label(frame1,text="Realtor ID",padx=5,pady=5).pack()
    l2=Label(frame1,text="Enter NAME",padx=5,pady=5).pack()
    l3=Label(frame1,text="phone",padx=5,pady=5).pack()
    l4=Label(frame1,text="License",padx=5,pady=5).pack()
    l5=Label(frame1,text="Email",padx=5,pady=5).pack()
                

    frame2=Frame(root,padx=5,pady=5)
    frame2.grid(row=1,column=2)
    e1=Entry(frame2)
    e1.pack(padx=5,pady=5)
    e2=Entry(frame2)
    e2.pack(padx=5,pady=5)
    e3=Entry(frame2)
    e3.pack(padx=5,pady=5)
    e4=Entry(frame2)
    e4.pack(padx=5,pady=5)
    e5=Entry(frame2)
    e5.pack(padx=5,pady=5)
    Button(root,text="ADD",padx=5).grid(row=2,columnspan=5,pady=5)
    root.mainloop()
# realt()