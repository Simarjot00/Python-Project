from tkinter import *
from tkinter import ttk 
from dbconnect import *
def myclients():
     def tree():
          class TreeviewFrame(ttk.Frame):
               def __init__(self, ws):
                    super().__init__(ws)
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
          query="select * from client "
          cur=info(query)
          ws=Tk()
          ws.title('Client Data')
          ws.geometry('800x600+100+100')
          ws['bg']='white'
          columns=('ClientID','Name','phone','email')

          treeview_frame = TreeviewFrame(ws)
          treeview_frame.pack()
          treeview_frame.treeview.config(columns=columns, show="headings")
          treeview_frame.treeview.heading('ClientID',text='ID',anchor=CENTER)
          treeview_frame.treeview.heading('Name',text='Name',anchor=CENTER)
          treeview_frame.treeview.heading('phone',text='Phone',anchor=CENTER)
          treeview_frame.treeview.heading('email',text='Email',anchor=CENTER)
          z=0
          for x in cur:
               treeview_frame.treeview.insert(parent='',index=z,values=x)
               z=z+1  
          ws.mainloop()
     tree()


