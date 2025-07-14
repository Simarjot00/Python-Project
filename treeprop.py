from tkinter import *
from tkinter import ttk 
from dbconnect import *
def propty():
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
               query="select * from properties"
               cur=info(query)
               ws=Tk()
               ws.title('Properties Data')
               ws.geometry('800x600+100+100')
               ws['bg']='white'
               columns=('propertyid','title','price','address','realtor_id','listingdate','type','amenities','bedrooms','washrooms','parking')
               treeview_frame = TreeviewFrame()
               treeview_frame.pack()
               treeview_frame.treeview.config(columns=columns, show="headings")
               treeview_frame.treeview.heading('propertyid',text='pid',anchor=CENTER)
               treeview_frame.treeview.heading('title',text='title',anchor=CENTER)
               treeview_frame.treeview.heading('price',text='title',anchor=CENTER)
               treeview_frame.treeview.heading('address',text='title',anchor=CENTER)
               treeview_frame.treeview.heading('realtor_id',text='rid',anchor=CENTER)
               treeview_frame.treeview.heading('listingdate',text='date',anchor=CENTER)
               treeview_frame.treeview.heading('type',text='type',anchor=CENTER)
               treeview_frame.treeview.heading('amenities',text='amenities',anchor=CENTER)
               treeview_frame.treeview.heading('bedrooms',text='bed',anchor=CENTER)
               treeview_frame.treeview.heading('washrooms',text='bath',anchor=CENTER)
               treeview_frame.treeview.heading('parking',text='parking',anchor=CENTER)
               
               z=0
               for x in cur:
                    treeview_frame.treeview.insert(parent='',index=z,values=x)
                    z=z+1  
               ws.mainloop()

