from tkinter import *
from dbconnect import *
from tkinter.messagebox import showinfo
def apmnt():
    def getinfo():
        y=int(e1.get())
        m=int(e2.get())
        n=int(e3.get())
        p=e4.get()
       
        query=f"insert into appointment details(clientid,agentid,propertyid,appointmentdate) values('{y}','{m}','{n}',{p})"
        alterations(query)
        showinfo(title='Insertion',message='Inserted Success')
        e1.delete(0,END)
        e2.delete(0,END)
        e3.delete(0,END)
        e4.delete(0,END)
    root=Tk()
    root.title("Appointment details")
    root.geometry("500x500")


    frame1=Frame(root,padx=5,pady=5)
    frame1.grid(row=1,column=1)
    Label(root,text="Appointment DETAILS",padx=5).grid(row=0,columnspan=5,pady=7)
    l1=Label(frame1,text="Client ID",padx=30,pady=10).pack()
    l2=Label(frame1,text="Agent ID",padx=30,pady=5).pack()
    l3=Label(frame1,text="Property ID",padx=30,pady=5).pack()
    l4=Label(frame1,text="Appointment Date",padx=30,pady=5).pack()
                

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


    Button(root,text="Submit",padx=5).grid(row=2,columnspan=5,pady=5)
    root.mainloop()