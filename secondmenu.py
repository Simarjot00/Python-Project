from tkinter import *
from tkinter import Tk,Frame,Menu
import client as c
import realtors as r
import properties as p 
import sales as s 
import transactions as tr
import treeclnt as t
import appointments as a
import treeapp as tp
import treeprop as tpr
import treerealtors as trl
import treesales as ts
import treetrans as tt

def menuu():
    #root window
    root=Tk()
    root.geometry('400x400')
    root.title("Menu")
    #create a menubar
    menubar=Menu(root);root.config(menu=menubar)
    # create the file  menu
    file_menu=Menu(menubar,tearoff=0)
    #add menu items to File Menu
    file_menu.add_command(label='Add Realtor',command=r.realt)
    file_menu.add_command(label='Show Realtor',command=trl.realtr)
    file_menu.add_command(label='Close')
    file_menu.add_separator()
    #add exit menu item
    file_menu.add_command(label='Exit',command=root.destroy)
    #add file to menubar
    menubar.add_cascade(label="Realtor",menu=file_menu)
    #create the help menu
    help_menu=Menu(menubar,tearoff=0)
    help_menu.add_command(label="Add Client",command=c.clnt)
    help_menu.add_command(label="Show Client",command=t.myclients)
    help_menu.add_command(label="Delete Client")
    #add help menu to menubar
    menubar.add_cascade(label="Client",menu=help_menu)
    #create the help menu
    help_menu=Menu(menubar,tearoff=0)
    help_menu.add_command(label="Add Property",command=p.prop)
    help_menu.add_command(label="Show Properties",command=tpr.propty)
    help_menu.add_command(label="Delete Property")
    #add help menu to menubar
    menubar.add_cascade(label="Property",menu=help_menu)
    #create the help menu
    help_menu=Menu(menubar,tearoff=0)
    help_menu.add_command(label="Add Transaction",command=tr.trans)
    help_menu.add_command(label="Show Transactions",command=tt.trans)
    help_menu.add_command(label="Delete Transactions")
    #add help menu to menubar
    menubar.add_cascade(label="Tranactions",menu=help_menu)
    #create the help menu
    help_menu=Menu(menubar,tearoff=0)
    help_menu.add_command(label="Add Property",command=s.sale)
    help_menu.add_command(label="Show Properties",command=ts.salestree)
    help_menu.add_command(label="Delete Property")
    #add help menu to menubar
    menubar.add_cascade(label="Sold properties",menu=help_menu)
    root.mainloop()

