from tkinter import *
from dbconnect import *
from tkinter.messagebox import showinfo
def clnt():
    def getinfo():
        # x=int(e1.get())
        y=e2.get()
        m=int(e3.get())
        n=e4.get()
        query=f"insert into client(name,phone,email) values('{y}','{m}','{n}')"
        alterations(query)
        showinfo(title='Insertion',message='Inserted Success')
        e2.delete(0,END)
        e3.delete(0,END)
        e4.delete(0,END)

    root=Tk()
    root.title("Client details")
    root.geometry("300x300")


    frame1=Frame(root,padx=5,pady=5)
    frame1.grid(row=1,column=1)
    Label(root,text="Client DETAILS",padx=5).grid(row=0,columnspan=5,pady=7)
    # l1=Label(frame1,text="client ID",padx=5,pady=5).pack()
    l2=Label(frame1,text="Enter NAME",padx=5,pady=5).pack()
    l3=Label(frame1,text="phone",padx=5,pady=5).pack()
    l4=Label(frame1,text="Email",padx=5,pady=5).pack()
                

    frame2=Frame(root,padx=5,pady=5)
    frame2.grid(row=1,column=2)
    # e1=Entry(frame2)
    # e1.pack(padx=5,pady=5)
    e2=Entry(frame2)
    e2.pack(padx=5,pady=5)
    e3=Entry(frame2)
    e3.pack(padx=5,pady=5)
    e4=Entry(frame2)
    e4.pack(padx=5,pady=5)

    Button(root,text="ADD",command=getinfo).grid(row=2,columnspan=5,padx=5,pady=5)
    root.mainloop()
# clnt()