from tkinter import *
from tkinter import ttk 
from dbconnect import *
def apdata():
    class TreeviewFrame(ttk.Frame):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.hscrollbar = ttk.Scrollbar(self, orient=HORIZONTAL)
            self.vscrollbar = ttk.Scrollbar(self, orient=VERTICAL)
            self.treeview = ttk.Treeview(
                self,
                xscrollcommand=self.hscrollbar.set,
                yscrollcommand=self.vscrollbar.set
            )
            self.hscrollbar.config(command=self.treeview.xview)
            self.hscrollbar.pack(side=BOTTOM, fill=X)
            self.vscrollbar.config(command=self.treeview.yview)
            self.vscrollbar.pack(side=RIGHT, fill=Y)
            self.treeview.pack()
    def tree():
        query="select * from appointments "
        cur=info(query)
        ws=Tk()
        ws.title('Appointment Data')
        ws.geometry('800x600+100+100')
        ws['bg']='white'
        columns=('clientid','agentid','propertyid','appointmentdate')
        treeview_frame = TreeviewFrame()
        treeview_frame.pack()
        treeview_frame.treeview.config(columns=columns, show="headings")
        treeview_frame.treeview.heading('clientID',text='ID',anchor=CENTER)
        treeview_frame.treeview.heading('agentid',text='agentid',anchor=CENTER)
        treeview_frame.treeview.heading('propertyid',text='pid',anchor=CENTER)
        treeview_frame.treeview.heading('appointmentdate',text='date',anchor=CENTER)
        z=0
        for x in cur:
            treeview_frame.treeview.insert(parent='',index=z,values=x)
            z=z+1  
        ws.mainloop()

