from tkinter import * 
from tkinter.messagebox import showerror,showwarning,showinfo
# import select as s
import secondmenu as m
def getinfo():
     if(len(e1.get())==0 and len(e2.get())==0):
        showerror(title='error',message='Please enter the details')
        return
     x=e1.get()
     y=int(e2.get())
     if(x=='simar' and y==123):
        # print("true")
        submit.config(text="correct")
      #   s.property()
        m.menuu()
   #   else:
   #      # print("False")
   #      submit.config(text="Incorrect")
     else:
          print("Incorrect",showwarning(title='error',message='Invalid details'))
parent=Tk()
title=Label(parent,text="Login Form").grid(row=0,columnspan=2,padx=10,pady=10,ipadx=5,ipady=5)
name=Label(parent,text=" Enter Username").grid(row=1,column=0,padx=10,pady=10,ipadx=5,ipady=5)
e1=Entry(parent)
e1.grid(row=1,column=1,padx=10,pady=10,ipadx=5,ipady=5)
password=Label(parent,text="Enter Password").grid(row=2,column=0,padx=10,pady=10,ipadx=5,ipady=5)
e2=Entry(parent,show="*")
e2.grid(row=2,column=1,padx=10,pady=10,ipadx=5,ipady=5)
login=Button(parent,text="login",command=getinfo)
login.grid(row=5,column=0,padx=10,pady=10,ipadx=5,ipady=5)
cancel=Button(parent,text="cancel", command=lambda:parent.quit()).grid(row=5,column=1,padx=10,pady=10,ipadx=5,ipady=5)
submit=Label(parent,text="submit")
submit.grid(row=6,columnspan=2,padx=10,pady=10,ipadx=5,ipady=5)
parent.mainloop()